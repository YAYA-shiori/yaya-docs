# yaya_optional.dic

## 概要

`yaya_optional.dic` 是一个系统词典，包含一些非必需但实用的辅助工具函数。它会与 `shiori3.dic`（[yaya_shiori3.dic](./yaya-shiori3-dic.md)）一同自动加载。它提供操作 Sakura Script 标签、格式化字符串、初始化对话框、检测人格（FMO）等功能。

## SHIORI3FW.EscapeDangerousTags

```
SHIORI3FW.EscapeDangerousTags( script )
```

禁用（转义）字符串中包含的“危险” Sakura Script 标签。只将执行危险操作的标签（例如启动浏览器、启动邮件客户端、切换被动模式等）的反斜杠转义为 `\\`，安全标签则保持原样。

目前，以下标签被视为“危险”：

- `\![]` 中包含以下字符串的标签：`updatebymyself` / `vanishbymyself` / `enter,passivemode` / `leave,passivemode` / `lock,repaint` / `unlock,repaint` / `biff` / `open,browser` / `open,mailer` / `raise`
- `\j[]` 标签

| 参数 | 说明 |
|------|------|
| `script` | 要禁用的字符串 |

返回值为已禁用的字符串。

```
_safe = SHIORI3FW.EscapeDangerousTags(外部から受け取ったテキスト)
```

## SHIORI3FW.EscapeAllTags

```
SHIORI3FW.EscapeAllTags( script )
```

转义字符串中包含的“所有” Sakura Script 标签。凡是以 `\` 开头的内容都会被转义。适用于希望将用户输入原样显示在对话框中等场景。

| 参数 | 说明 |
|------|------|
| `script` | 要转义的字符串 |

返回值为已转义的字符串。

```
_display = SHIORI3FW.EscapeAllTags('\0\s[0]これはタグではなくテキストです。\e')
// → "\\0\\s[0]これはタグではなくテキストです。\\e" として表示される
```

[SHIORI3FW.RemoveAllTags](./yaya-shiori3-dic.md#shiori3fwremovealltags) 会**删除**标签，而此函数会**转义并显示**标签。

## SHIORI3FW.TranslateSystemChar

```
SHIORI3FW.TranslateSystemChar( text [ , 置換文字 ] )
```

将 YAYA 的运算符、分隔符等系统保留字符替换为指定字符。适用于生成可用作变量名或标识符的安全字符串。

| 参数 | 说明 |
|------|------|
| `text` | 要处理的文本 |
| `置換文字` | 替换后的字符（省略时为 `_`） |

```
_varname = SHIORI3FW.TranslateSystemChar('hello world!')
// → "hello_world_"

_varname = SHIORI3FW.TranslateSystemChar('foo/bar', '-')
// → "foo-bar"
```

## 字符串格式化

用于对齐对话框内菜单等内容的显示宽度。字符数均按**半角换算**指定（1 个全角字符＝2 个半角字符）。

| 函数 | 说明 |
|------|------|
| `SHIORI3FW.MakeLongText(テキスト, 文字数)` | 如果文本未达到指定的半角换算字符数，则在末尾补上空格以对齐长度。如果文本已达到或超过指定长度，则原样返回 |
| `SHIORI3FW.MakeShortText(テキスト, 文字数)` | 如果文本超过指定的半角换算字符数，则截去末尾并添加 `...` 或 `..`。如果文本不超过指定长度，则原样返回 |
| `SHIORI3FW.MakeJustText(テキスト, 文字数)` | 组合上述两个函数，将文本调整为恰好指定的半角换算字符数 |

```
_item  = SHIORI3FW.MakeJustText('設定', 20)
_short = SHIORI3FW.MakeShortText('これはとても長いテキストです', 10)   // "これは..." のように切り詰められる
```

## SHIORI3FW.InitBalloons

```
SHIORI3FW.InitBalloons()
```

生成一段 Sakura Script，用于清空当前所有有效作用域的对话框。适用于在多作用域环境中一次性重置对话框。此函数不接受参数，返回值是由所有作用域的 `\p[n]\c\b[-1]` 拼接而成的 Sakura Script 字符串。

```
OnMyEvent
{
	SHIORI3FW.InitBalloons + '\0\s[0]初期化しました。\e'
}
```

## FMO 相关

FMO（File Mapping Object，文件映射对象）是 SSP 管理的“当前正在运行的人格信息”共享内存。使用以下函数可以检查其他人格是否存在，或获取相关信息。

### SHIORI3FW.IsGhostExist

```
SHIORI3FW.IsGhostExist( name [ , fmoname ] )
```

使用 FMO 检查指定名称（\0 名）的人格当前是否正在运行。由于使用 FMO，此函数可以获取调用瞬间的信息。函数内部会调用 `SHIORI3FW.RefreshFMOTable`。

| 参数 | 说明 |
|------|------|
| `name` | 人格名 |
| `fmoname` | 要检查的 FMO 名称（可省略。省略时为 `Sakura`。通常可以省略） |

如果该人格正在运行，则返回 1；否则返回 0。

```
if SHIORI3FW.IsGhostExist('ゆっくり霊夢') {
	'\0\s[0]霊夢がいるよ！\e'
}
```

### SHIORI3FW.RefreshFMOTable

```
SHIORI3FW.RefreshFMOTable( [ fmoname [ , hwnd ] ] )
```

使用 [READFMO](../functions/READFMO.md) 函数，将 FMO 构建为便于处理的字符串数组。FMO 包含“当前正在运行的”人格信息，因此使用此函数可以实时获取正在运行的人格信息。如果 FMO 内容与上次相比没有变化，则会跳过重新解析（缓存）。

| 参数 | 说明 |
|------|------|
| `fmoname` | 要读取的 FMO 名称（可省略。省略时为 `Sakura`。Unicode 版为 `SakuraUnicode`。通常可以省略） |
| `hwnd` | 要忽略的人格窗口句柄（可省略。省略时使用 `SHIORI3FW.HWnd[0]`。通常可以省略） |

此函数没有返回值，但会构建以下全局变量。这些变量会在 SHIORI 结束时自动清除。

“临时启动”（例如 SSTPVIEWER 或虚拟条目）的人格会自动从 FMO 表中排除。

#### SHIORI3FW.FMOTable

格式为简易数组，以逗号和 `|` 分隔。在 SSP 中，所有项目都会填充；但有些 baseware 可能没有某些项目（项目为空）。此外，在 Windows 以外的操作系统上无法使用。

```
id|name|keroname|hwnd|kerohwnd|path|ghostpath,
id|name|keroname|hwnd|kerohwnd|path|ghostpath,
...
```

| 项目 | 含义 |
|------|------|
| `id` | 表示人格的 ID。通常是即使知道了也没有意义的字符串 |
| `name` | \0 名 |
| `keroname` | \1 名 |
| `hwnd` | \0 的窗口句柄 |
| `kerohwnd` | \1 的窗口句柄 |
| `path` | 人格的安装目录（通常是 `ssp.exe` 所在位置，但 SSP 可以有多个人格安装目录） |
| `ghostpath` | 人格的基础目录，即存放 `install.txt` 或 `thumbnail.png` 的位置 |

#### SHIORI3FW.SakuraNameList

格式为通用数组。它是从上述信息中提取出的仅包含 \0 名的数组。例如，使用 `ANY(SHIORI3FW.SakuraNameList)`，即可轻松地从正在运行的人格中随机选择一个并获取其名称。

```
// 起動中の全ゴースト名を列挙する例
SHIORI3FW.RefreshFMOTable
_list = SHIORI3FW.SakuraNameList
_n = ARRAYSIZE(_list)
for _i = 0; _i < _n; _i++ {
	// _list[_i] にさくら名が入っている
}
```

#### SHIORI3FW.FMOCache

上次读取的 FMO 原始数据（用于缓存）。通常很少直接引用。

#### 备注

通常，上述变量不包含自身的信息（因为 `hwnd` 会指定为 `SHIORI3FW.HWnd[0]`）。如果想包含自身的信息，可以将 `hwnd` 设为 -1 等值。

## SHIORI3FW.HTTPCodeToMessage

```
SHIORI3FW.HTTPCodeToMessage( コード )
```

将网络更新等操作返回的 HTTP 状态码转换为日语错误消息。如果没有对应的代码，则返回空字符串。

| 代码 | 返回值 |
|--------|--------|
| `'403'` | `'アクセス拒否'` |
| `'404'`、`'410'` | `'ファイル無し'` |
| `'500'`、`'502'`、`'503'` | `'サーバ側の不調'` |
| `'timeout'` | `'タイムアウト'` |
| `'fileio'` | `'ファイル書き込みエラー'` |
| `'artificial'` | `'手動中断'` |

```
OnNetworkUpdateComplete
{
	if reference[1] != '200' {
		_msg = SHIORI3FW.HTTPCodeToMessage(reference[1])
		'\0\s[0]更新に失敗しました：%(_msg)\e'
	}
}
```

## 相关内容

- [yaya_shiori3.dic](./yaya-shiori3-dic.md)
- [系统词典函数手册（yaya-dic）](https://github.com/YAYA-shiori/yaya-dic/blob/master/docs/manual_yaya_base.md)
