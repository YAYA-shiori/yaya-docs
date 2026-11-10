# yaya_shiori3.dic

## 什么是系统词典

系统词典是由一组 YAYA 脚本文件组成的集合，包含一系列功能，旨在让 YAYA「能够轻松地用作人格的 SHIORI」。目前，系统词典由以下文件构成（位于 `yaya_base` 文件夹内）。

| 文件 | 说明 |
|---------|------|
| `shiori3.dic` | SHIORI 核心词典。实现了作为 SHIORI 运行所需的最低限度功能。本页面将介绍此文件 |
| `compatible.dic` | 旧版兼容词典。实现了与 AYA4、5 兼容运行所需的功能（如果不需要，可以不加载） |
| `optional.dic` | 附加功能词典。并非必需，但实现了一些实用功能（[yaya_optional.dic](./yaya-optional-dic.md)） |
| `lint.dic` | 提供 `SHIORI3FW.Lint.Run`，用于从已加载的词典中查找未定义或未使用的变量和函数（YAYA Tc574-1 及更高版本） |
| `config.dic` | 用于设置和更改 `shiori3.dic` 参数的词典。此词典由用户（人格作者）修改。详细内容请参阅文件本身 |

除 `config.dic` 外，用户通常不需要修改这些词典。

最新稳定版由「[你好 YAYA 世界（紺野ややめ (Konnoyayame)）](http://ms.shillest.net/yayame.xhtml)」提供。请根据需要更新。更新时，建议同时更新 `yaya.dll`。最新开发版可在 [yaya-dic](https://github.com/YAYA-shiori/yaya-dic) 查看。

使用 `yaya-dic` 时，请在基础设置文件中添加以下行（[基础设置](../grammar/01-basic-settings.md)）。

```
dicdir, yaya_base
```

编辑 `_loading_order.txt`，可以禁用 `optional.dic` 或启用 `compatible.dic`。

## 概述

`yaya_shiori3.dic` 是为基于 YAYA 的人格提供 SHIORI/3.0 核心功能的系统词典。

## SHIORI 事件的输入和输出

baseware 传递的 SHIORI 事件是如下所示的字符串。

```
GET SHIORI/3.0
Sender: SSP
Charset: UTF-8
SecurityLevel: local
ID: OnSecondChange
Status: talking
Reference0: 107
Reference1: 0
Reference2: 0
Reference3: 1
Reference4: 0
```

`yaya_shiori3.dic` 会解析此字符串，并执行以下操作。

| 标头 | 操作 |
|--------|------|
| `ID: OnSecondChange` | 将其作为事件名解析，并调用 `OnSecondChange` 函数。对于开头不带 `On` 的 ID，会调用加上 `On_` 的函数（例如：`hwnd` → `On_hwnd`） |
| `Sender: SSP` | 将值（`"SSP"`）存入全局变量 `basewarename`、`sender` |
| `Charset: UTF-8` | 字符编码。会进行适当解析，并在输出时转换为该字符编码 |
| `Status: talking` | 将值（`"talking"`）存入全局变量 `status` |
| `Reference0: 107` | 将值（107）存入全局变量 `reference[0]` |

经过上述处理，在 `OnSecondChange` 函数中完成处理后，`yaya_shiori3.dic` 会将结果作为如下字符串返回给 baseware。

```
SHIORI/3.0 200 OK
Sender: AYA
Charset: UTF-8
Value: \0\s[0]あ、エミリさん。\1\s[10]テディも元気そうだな。
Reference0: Emily
```

| 标头 | 内容 |
|--------|------|
| `SHIORI/3.0 200 OK` | 自动返回适当的代码 |
| `Sender: AYA` | 自动添加 |
| `Charset: UTF-8` | 自动返回适当的代码 |
| `Value: ～` | 存放函数的执行结果（也就是对话内容） |
| `Reference0: Emily` | 如果存在名为 `res_reference*`（`*` 为数字）的全局变量，则将其放在这里（baseware 会将 SHIORI 返回的 Reference0 识别为交流对象的人格名称） |

## 随机对话

为了能够轻松进行随机对话，本系统词典具有每隔 `aitalkinterval` 秒调用一次 `OnAiTalk` 函数的功能。原本 `OnAiTalk` 并不是 baseware 提供的功能，而是由 `yaya_shiori3.dic` 添加的。

## 内部转换

本系统词典具有在处理完所有事件后调用 `OnTranslateInternal` 函数的功能。此时传入的参数（`_argv[0]`）是即将输出到 baseware 的对话内容。该函数返回的内容会成为实际输出到 baseware 的对话。因此，可以在 `OnTranslateInternal` 中适当处理 `_argv[0]` 并将其返回，以便对所有对话统一进行转换等操作。

## 连锁对话

连锁对话是指「以某段对话为契机，按照指定顺序连续进行一系列对话」的功能。此功能也由 `yaya_shiori3.dic` 实现。

在对话的 `\e` 后写上 `:chain=○○`，即可启动连锁对话（`○○` 是用于区分连锁对话的标识符，除 `end` 外可以是任意字符串）。连锁对话启动后，`OnAiTalk` 不会执行随机对话，而是调用上文提到的 `○○` 函数（连锁函数）（此功能不是在 `yaya_shiori3.dic` 中，而是在人格模板中实现的）。

连锁函数与普通函数不同，写法如下（假设使用 `:chain=hoge`）。

```
hoge
{{CHAIN
    "\0\s[0]りんご\e"
    "\0\s[1]ごりら\e"
    "\0\s[0]らっぱ\e:chain=end"
}}CHAIN
```

普通函数会从「りんご」「ごりら」「らっぱ」中随机选择一条，而连锁函数会从上到下依次连锁播放对话。在 `\e` 后写上 `:chain=end`，即可停止连锁对话。

### 链接分隔符（`:chain=`）

在对话脚本的末尾添加 `:chain=事件名`，即可在下次随机对话的机会到来时调用指定事件。

```
OnMyEvent
{
	'\0\s[0]続きがあるよ。\e' + ':chain=' + 'OnMyEventPart2'
}

OnMyEventPart2
{
	'\0\s[0]これが続きです。\e'
}
```

## 延迟 EVAL

在 `\e` 后写入 `:eval=表达式`，即可执行该表达式（实际效果与写入 `EVAL(表达式)` 相同）。例如，写入 `"\0\s[0]はじめまして。\e:eval=aisatu=1"`，即可轻松实现类似“以说出某段对话为契机进行标志处理”的功能。

出于安全原因，此功能默认处于禁用状态。若要启用，请充分了解相关安全风险，然后将 `config.dic` 中的 `SHIORI3FW.ENABLE_DELAYED_EVAL` 设置为 1。

## 已安装人格列表

解析 `ID: installedghostlist`，并创建全局变量 `installedghostlist`（人格名称的通用数组）等。

收到 `OnNotifyInstalledGhostName` 等事件时，以下变量会自动更新。索引彼此对应，`installedghostlist[i]` 中人格的 Sakura 名称就是 `installedsakuralist[i]`。

| 变量名 | 内容 |
|--------|------|
| `installedghostlist` | 已安装人格的人格名称数组 |
| `installedsakuralist` | 已安装人格的 Sakura 名称数组 |
| `installedkerolist` | 已安装人格的 Kero 名称数组 |

## SAORI 调用

为了简化 SAORI 调用，`yaya_shiori3.dic` 提供了以下函数。使用 `FUNCTIONEX` 时，也会自动加载和卸载 SAORI。

### FUNCTIONEX

```
FUNCTIONEX( dllname [, Argument0 , Argument1 , ... ] )
```

| 参数 | 说明 |
|------|------|
| `dllname` | 要调用的 SAORI 的 DLL 名称。指定相对于 `yaya.dll` 的路径 |
| `Argument0, 1, ...` | 传递给 SAORI 的参数（可省略） |

`FUNCTIONEX` 的返回值是 SAORI 的返回值（Result 的值）。如果 SAORI 还返回了其他返回值（Value0、1、…），则会存入 `valueex` 数组以及全局变量 `valueex0`、`valueex1`、… 中。

```
_result = FUNCTIONEX('kawari8.dll', 'こんにちは')
// 追加の戻り値は valueex[0], valueex[1], ... で参照
```

详情请参阅 [FUNCTIONEX](../functions/FUNCTIONEX.md)。

#### baseware 内置模块（SAORI over DirectSSTP）

当 `dllname` 以 `internal_` 开头时（例如 `internal_crypto`、`internal_time.dll` 等；不区分大小写，末尾的 `.dll` 可以省略），不会加载 DLL，而是通过 `DIRECTSSTP` 调用 baseware（SSP 2.9.13 及更高版本）的内置模块。写法、返回值、`valueex` 和 `LIB.STATUSCODE` 均与 DLL 的 SAORI 相同。模块和函数请参阅 [SAORI over DirectSSTP](https://ssp.shillest.net/ukadoc/manual/spec_saori_ex.html)。

```
_hash = FUNCTIONEX('internal_crypto', 'Digest', 'sha256', 'abc')
_text = FUNCTIONEX('internal_time', 'Format', 0, '%Y/%m/%d', '--tz=+09:00')
```

- 模块不可用时（旧版 SSP、SSP 以外的 baseware、未知模块），返回 0。每个模块仅在首次使用时通过 `GET Version SAORI/1.0` 检查并记住是否可用。启动后、尚未获取人格窗口（`SHIORI3FW.HWnd[0]`）时，不会记住结果，而是返回 0
- 调用失败时（400、500），Result 为空，`LIB.STATUSCODE` 中会存入 `400 Bad Request` 等内容。失败原因（`ErrorDescription`）可从 `var.lib.key` / `var.lib.value` 读取
- 参数中包含换行符（CR、LF）时，可能会被追加为标头，因此不会发送，并返回 0。包含换行符或前后空格的数据，请使用 `--data-in=base64` 等形式传递
- 字符编码固定为 UTF-8
- 对于耗时较长的处理（如 `DeriveKey`、`HashPassword`），请添加 `--async=标识符`。结果之后会通过事件（如 `OnInternalSaoriComplete`）传回，`FUNCTIONEX` 的返回值为空（`LIB.STATUSCODE` 为 `204 No Content`）

### SAORI

`FUNCTIONEX` 的同义名称（别名）。写法与 `FUNCTIONEX` 相同（`internal_` 内置模块也相同）。由于多了一层封装，速度比 `FUNCTIONEX` 慢，但差异通常不必在意。

### FUNCTIONLOAD

加载 SAORI 的 DLL。参数为 SAORI 的 DLL 文件名。成功时返回 1，失败时返回 0。

```
FUNCTIONLOAD('kawari8.dll')
```

### SHIORI3FW.SaoriUnloadAll

卸载当前已加载的所有 SAORI DLL。没有参数，也没有返回值。

## baseware 属性函数

读取或写入 SSP 等支持 DIRECTSSTP 的 baseware 的属性，也可以执行 EXECUTE SSTP 命令。

| 函数 | 说明 |
|------|------|
| `EXECUTE_SSTP(命令名, 参数0, 参数1, ...)` | 向 baseware 发送 `EXECUTE SSTP/1.1`，并返回结果（附加数据） |
| `GET_PROPERTY(属性名)` | 获取属性值。成功时返回属性值字符串，失败时返回空字符串 |
| `SET_PROPERTY(属性名, 值)` | 设置属性值。成功时返回 1，失败时返回 0 |

```
_vol = GET_PROPERTY('volume')
SET_PROPERTY('volume', '80')
```

### EXECUTE_SSTP

```
EXECUTE_SSTP( コマンド名 [, 引数0 , 引数1 , ... ] )
```

通过 DIRECTSSTP 向 baseware 发送 `EXECUTE SSTP/1.1` 请求，并返回结果。第二个及之后的参数会作为 `Reference0`、`Reference1`、… 发送。可用命令请参阅 baseware 的 SSTP 规范（`GetVersion`、`GetGhostNameList`、`GetStatus`、`GetCookie` 等）。

- 返回值：成功时（状态为 2xx），返回空行之后的附加数据（会去除末尾换行符）。失败时返回空字符串。返回列表的命令会以 `C_CRLF` 分隔结果
- 结果变量：`SSTP.STATUSCODE` 中存入状态行结果（如 `200 OK`、`501 Not Implemented`），`SSTP.STATUS` 中存入对应数值。无法发送时，两者分别为 `''` 和 0
- 命令或参数中包含换行符（CR、LF）时，可能会被追加为标头，因此不会发送，并返回空字符串（`SSTP.STATUS` 为 0）

没有附加数据的命令即使成功也会返回空字符串，因此请通过 `SSTP.STATUS` 确认是否成功。

```
_ver = EXECUTE_SSTP('GetShortVersion')
_ghosts = SPLIT(EXECUTE_SSTP('GetGhostNameList'), C_CRLF)

_dummy = EXECUTE_SSTP('SetCookie', 'mykey', 'value')
if SSTP.STATUS == 200 || SSTP.STATUS == 204 {
	// 成功
}
```

`GET_PROPERTY` 与 `EXECUTE_SSTP('GetProperty', 属性名)` 相同，`SET_PROPERTY` 与 `EXECUTE_SSTP('SetProperty', 属性名, 值)` 相同；`SSTP.STATUSCODE` 和 `SSTP.STATUS` 也会以同样的方式赋值。

## 数组操作

| 函数 | 说明 |
|------|------|
| `JOIN(値0, 値1, ..., 区切り文字)` | 将最后一个参数作为分隔符，连接其他值（传入数组时会依次连接各元素），并返回字符串 |
| `REVERSE(値0, 値1, ...)` | 返回参数顺序反转后的数组 |
| `UNIQUE(値0, 値1, ...)` | 返回去除参数中重复项后的数组（[ARRAYDEDUP](../functions/ARRAYDEDUP.md) 的封装函数） |
| `SPLITEX(文字列, 区切り文字)` | 与 [SPLIT](../functions/SPLIT.md) 相同，但不会将内容为空的元素转换为数组 |
| `MAX(値0, 値1, ...)` | 返回参数中的最大值。如果包含字符串，则返回按字典顺序排列的最后一个 |
| `MIN(値0, 値1, ...)` | 返回参数中的最小值。如果包含字符串，则返回按字典顺序排列的第一个 |
| `AVERAGE(値0, 値1, ...)` | 返回参数的平均值。如果包含字符串，则返回空字符串 |

```
_配列 = ("A","B","C","D","E")
結果 = JOIN(_配列, "★")   // "A★B★C★D★E"
```

## 文本处理与状态确认

### SHIORI3FW.RemoveAllTags

返回删除所有 Sakura Script 标签（`\0`、`\s[0]` 等）后的字符串。

```
_plain = SHIORI3FW.RemoveAllTags('\0\s[0]こんにちは。\e')
// → "こんにちは。"
```

如果不想删除标签，而是希望将其转义后显示，请使用 [SHIORI3FW.EscapeAllTags](./yaya-optional-dic.md#shiori3fwescapealltags)。

### SHIORI3FW.CanTalk

返回当前人格是否处于可以说话的状态。如果 `status` 标头中包含 `talking`、`choosing`、`minimizing` 或 `timecritical`，则判断为无法说话。可以说话时返回 1，无法说话时返回 0。

```
if SHIORI3FW.CanTalk {
	// ランダムトーク発動
}
```

## 延迟事件（“延迟说话”事件）

在指定秒数后，仅触发一次特定事件。事件会在 `OnSecondChange`（每秒一次）时处理。

### SHIORI3FW.SetDelayEvent

```
SHIORI3FW.SetDelayEvent( '発生させるイベント名' , 遅れる秒数 [, Reference0, ...] )
```

注册延迟事件。如果事件名为空字符串，则取消事件。第 3 个及之后的参数为事件触发时设置的 Reference 值（可省略）。

```
// 10秒後に OnMyDelayedEvent を発動
SHIORI3FW.SetDelayEvent('OnMyDelayedEvent', 10)

// キャンセル
SHIORI3FW.SetDelayEvent('', 0)
```

### SHIORI3FW.GetDelayEvent

以 `(事件名, 剩余秒数, Reference 的数组)` 的形式返回当前已注册的延迟事件信息。

## 添加响应标头

可以向事件处理器的响应中添加任意标头。设置会在每个请求结束后重置。

| 函数 | 说明 |
|------|------|
| `SHIORI3FW.PushAdditionalReturn(ヘッダ名, 値)` | 添加任意响应标头 |
| `SHIORI3FW.Push_X_SSTP_PassThru(名前, 値)` | 添加 `X-SSTP-PassThru-名前` 标头（用于 SSTP 透传） |

在事件处理器中为以下变量赋值后，值会自动附加到响应标头中。

| 变量名 | 标头 | 内容 |
|--------|--------|------|
| `res_reference` 或 `res_reference0` 〜 `res_reference31` | `Reference0:` 〜 | 事件响应的 Reference 值。可以通过数组或单独的变量指定 |
| `marker` 或 `res_marker` | `Marker:` | SSTP 标记值 |
| `res_securitylevel` | `SecurityLevel:` | 安全级别 |
| `res_valuenotify` | `ValueNotify:` | ValueNotify 值 |

```
OnMyEvent
{
	res_reference0 = 'value0'
	res_reference1 = 'value1'
	'\0\s[0]処理しました。\e'
}
```

`res_reference` 的最大索引由 `config.dic` 中的 `SHIORI3FW.RES_REF_MAX` 决定（初始值为 32）。

## 变量管理工具

### SHIORI3FW.RegisterTempVar

```
SHIORI3FW.RegisterTempVar( 変数名, ... )
```

注册在结束时（unload 时）自动删除的全局变量。可用于管理无需保存的临时全局变量。

```
myTempVar = '一時データ'
SHIORI3FW.RegisterTempVar('myTempVar')
```

## 伪事件

在人格的词典中定义这些函数后，它们会在特定时机被调用。

| 函数 | 调用时机 |
|------|------------------|
| `OnSHIORI3FW.SurfaceRestore` | AI 对话间隔经过 2/3 时。可用于在对话前将表面恢复为默认状态等 |
| `OnSHIORI3FW.ChangeSelfInfo` | 人格名、外壳名、外壳路径、对话框名或对话框路径更新时 |
| `OnSHIORI3FW.WindowCreate` | 新建角色窗口时。`reference[0]` 中会存入作用域编号 |
| `OnSHIORI3FW.WindowDestroy` | 销毁角色窗口时。`reference[0]` 中会存入作用域编号 |

```
OnSHIORI3FW.SurfaceRestore
{
	'\0\s[0]\1\s[10]\e'
}
```

## 系统变量

为了便于使用原本不太方便直接调用的函数，提供了以下变量。这些变量可用于获取系统信息。系统会自动更新这些变量，因此请仅将它们用于读取。

### 时间相关变量

| 变量名 | 返回值 |
|--------|--------|
| `year` | 当前日期和时间中的年份数值 |
| `month` | 当前日期和时间中的月份数值 |
| `day` | 当前日期和时间中的日期数值 |
| `weekday` | 当前日期和时间中的星期数值（0=星期日、1=星期一 … 6=星期六） |
| `hour` | 当前日期和时间中的小时数值（24 小时制） |
| `ampm` | 当前日期和时间中的上午／下午数值（0=AM、1=PM） |
| `hour12` | 当前日期和时间中的小时数值（12 小时制） |
| `hour12ex` | 当前日期和时间中的小时数值（12 小时制）。但 12 会显示为 0 时或 12 时 |
| `minute` | 当前日期和时间中的分钟数值 |
| `second` | 当前日期和时间中的秒数值 |
| `systemuptime` | OS 连续运行时间（单位：秒） |
| `systemupsecond` | 将 OS 连续运行时间换算为时分秒时的秒数值 |
| `systemupminute` | 将 OS 连续运行时间换算为时分秒时的分钟数值 |
| `systemuphour` | 将 OS 连续运行时间换算为时分秒时的小时数值 |
| `ghostupmin` | 人格连续运行时间（单位：分钟） |
| `ghostupmin_total` | 人格累计运行时间（单位：分钟） |
| `ghostuptimes` | 人格累计启动次数 |

### 内存相关变量

| 变量名 | 返回值 |
|--------|--------|
| `memoryload` | 物理内存使用率 |
| `memorytotalphys` | 物理内存总量 |
| `memoryavailphys` | 可用物理内存量 |
| `memorytotalvirtual` | 虚拟内存＋物理内存总量 |
| `memoryavailvirtual` | 可用虚拟内存＋物理内存量 |

### 发送方头部相关变量

| 变量名 | 返回值 |
|--------|--------|
| `basewarenameex` | 人格启动时的 baseware 名称（MATERIA 为 `embryo`，CROW 为 `crow`，SSP 为 `SSP`）。此值为首次启动时的值，不会改变 |
| `basewarename` | 当前请求的发送方 baseware 名称（发送方头部名称。也可能包含 baseware 名称以外的内容） |
| `sender` | 与 `basewarename` 相同 |

### 人格与外壳信息

| 变量名 | 内容 |
|--------|------|
| `SHIORI3FW.GhostName` | 当前人格名称 |
| `SHIORI3FW.ShellName` / `SHIORI3FW.ShellPath` | 当前外壳名称 / 外壳路径 |
| `SHIORI3FW.BalloonName` / `SHIORI3FW.BalloonPath` | 当前对话框名称 / 对话框路径 |
| `selfname` / `sakuraname` | 樱（作用域 0）的角色名称 |
| `keroname` | 凯罗（作用域 1）的角色名称 |
| `SHIORI3FW.HWnd` | 角色窗口的 HWND 数组。`[0]` 为樱一侧 |
| `SHIORI3FW.BalloonHWnd` | 对话框窗口的 HWND 数组。`[0]` 为樱一侧 |
| `SHIORI3FW.LastSurface` | 上次显示的 surface 编号数组。`[0]` 为樱一侧 |
| `SHIORI3FW.IsVisible` | surface 的显示状态（1=显示中，0=隐藏）。`[0]` 为樱一侧 |
| `SHIORI3FW.UserName` / `SHIORI3FW.UserNameFull` | 用户名（简称 / 全名） |
| `SHIORI3FW.UserBirthday` | 生日数组 `[年, 月, 日]`（整数类型） |
| `SHIORI3FW.UserSex` | 性别 |
| `SHIORI3FW.LastTalk` | 上次说过的脚本（适用于所有事件） |
| `SHIORI3FW.LastAITalk` | 上次随机对话的脚本 |
| `SHIORI3FW.Eventid` | 当前正在处理的事件 ID |
| `SHIORI3FW.Status` | 初始启动状态（已通过 `Run` 初始化） |
| `SHIORI3FW.UniqueID` | Auth.SSTP 使用的 ID |
| `SHIORI3FW.Capability` | baseware 的头部处理能力（通用数组） |

## 用户设置变量

为自定义人格的运行方式而提供的可读写变量。

| 变量名 | 初始值 | 内容 |
|--------|--------|------|
| `aitalkinterval` | 180（秒） | AI 对话（随机对话）的触发间隔。设为 0 时禁用 |
| `communicateratio` | 0（%） | 触发 AI 对话时，选择开始交流的比例 |

```
aitalkinterval = 300
```

## config.dic 的主要设置

可以通过 `config.dic` 更改系统的运行方式。

| 常量名 | 初始值 | 内容 |
|--------|--------|------|
| `TALK_INTERVAL` | 180 | `aitalkinterval` 的初始值（秒） |
| `COM_RATIO` | 0 | `communicateratio` 的初始值（%） |
| `SHIORI3FW.IGLIST_ACCEL` | 1 | 设为 1 时，使用 SSP / CROW 的 NOTIFY 事件来加快构建人格列表（不会创建樱名和凯罗名列表） |
| `SHIORI3FW.IGLIST_MAX` | 0 | 通过扫描文件构建人格列表时，获取人格的最大数量。设为 -1 时不限制，设为 0 时不获取 |
| `SHIORI3FW.RES_REF_MAX` | 32 | `res_reference*` 变量的最大索引 |
| `SHIORI3FW.AUTO_DATA_CONVERT` | 0 | 设为 1 时，自动转换 SAORI 返回值等的数据类型，并将字节值 1 替换为逗号（兼容 AYA5） |
| `SHIORI3FW.REF_ACCEL` | 0 | 设为 1 时，不创建 `reference0` 等变量，只使用 `reference[0]`（提升速度） |
| `SHIORI3FW.ENABLE_DELAYED_EVAL` | 0 | 启用通过 `:eval=` 执行的延迟 EVAL（出于安全原因，建议禁用） |

## AI 图表的默认值

SSP 的 AI 图表（雷达图）通过 SHIORI 资源 `getaistate` 绘制。当人格中没有 `On_getaistate`，或其返回值为空时，系统词典的 `SHIORI3EV.On_getaistate` 会返回以下 6 个轴的值。若在人格中定义 `On_getaistate`，则优先使用该定义。

| 标签 | 显示值 | 增加值 | 最大值 |
|--------|--------|--------|--------|
| `Boot` | `ghostuptimes`（累计启动次数） | 0 | 阶梯刻度 |
| `Uptime(h)` | `ghostupmin_last / 60`（截至上次的累计启动时间） | `ghostupmin / 60`（本次启动时间） | 阶梯刻度 |
| `Memory` | `GETVARLIST()` 的元素数量 | 0 | 阶梯刻度 |
| `Repertoire` | `GETFUNCLIST('On')` 的元素数量 | 0 | 阶梯刻度 |
| `Talk/h` | `3600 / aitalkinterval`（若 `aitalkinterval` 小于等于 0，则为 0） | 0 | 阶梯刻度 |
| `Social` | `communicateratio` | 0 | 100 |

- 阶梯刻度是能够容纳该值的最小刻度：10、20、50、100、200、500、…（`SHIORI3FW.AIGraphMax`）
- `Memory` 和 `Repertoire` 也包含系统词典自身的变量和函数
- `Uptime(h)` 的显示值和增加值可以是小数（SSP 2.4.26 及之后的版本支持小数）

## 相关内容

- [yaya_optional.dic](./yaya-optional-dic.md)
- [FUNCTIONEX](../functions/FUNCTIONEX.md)
- [系统词典内函数手册（yaya-dic）](https://github.com/YAYA-shiori/yaya-dic/blob/master/docs/manual_yaya_base.md)
