# yaya_shiori3.dic

## 什麼是系統辭典

系統辭典是指一組具備一系列功能的 YAYA 指令碼檔案，目的是讓 YAYA「能輕易作為人格的 SHIORI 使用」。目前系統辭典由下列檔案組成（位於 `yaya_base` 資料夾內）。

| 檔案 | 說明 |
|---------|------|
| `shiori3.dic` | SHIORI 核心辭典。實作作為 SHIORI 運作所需的最低限度功能。本頁將說明此檔案 |
| `compatible.dic` | 舊版相容辭典。實作與 AYA4、5 相容運作的功能（不需要時可以不載入） |
| `optional.dic` | 擴充功能辭典。並非必要，但實作了具備時很方便的功能（[yaya_optional.dic](./yaya-optional-dic.md)） |
| `lint.dic` | 提供 `SHIORI3FW.Lint.Run`，可從已載入的辭典中找出未定義或未使用的變數與函式（YAYA Tc574-1 之後） |
| `config.dic` | 用來設定或變更 `shiori3.dic` 參數的辭典。此辭典由使用者（人格作者）修改。詳細內容記載於檔案本身 |

除了 `config.dic` 以外，基本上使用者不需要修改其他辭典。

最新穩定版由「[哈囉 YAYA 世界（紺野ややめ (Konnoyayame)）](http://ms.shillest.net/yayame.xhtml)」提供。請視需要更新。更新時也建議一併更新 `yaya.dll`。最新開發版可在 [yaya-dic](https://github.com/YAYA-shiori/yaya-dic) 查看。

使用 `yaya-dic` 時，請在基礎設定檔中新增以下一行（[基礎設定](../grammar/01-basic-settings.md)）。

```
dicdir, yaya_base
```

編輯 `_loading_order.txt`，即可停用 `optional.dic` 或啟用 `compatible.dic`。

## 概要

`yaya_shiori3.dic` 是為基於 YAYA 的人格提供 SHIORI/3.0 核心功能的系統辭典。

## SHIORI 事件的輸入與輸出

baseware 傳入的 SHIORI 事件，是如下所示的字串。

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

`yaya_shiori3.dic` 會解讀此字串，並執行下列動作。

| 標頭 | 動作 |
|--------|------|
| `ID: OnSecondChange` | 解讀為事件名稱，並呼叫 `OnSecondChange` 函式。ID 開頭沒有 `On` 時，會呼叫加上 `On_` 的函式（例：`hwnd` → `On_hwnd`） |
| `Sender: SSP` | 將值（`"SSP"`）存入全域變數 `basewarename`、`sender` |
| `Charset: UTF-8` | 字元編碼。會正確解讀，並在輸出時轉換為該字元編碼 |
| `Status: talking` | 將值（`"talking"`）存入全域變數 `status` |
| `Reference0: 107` | 將值（107）存入全域變數 `reference[0]` |

執行上述動作後，`OnSecondChange` 函式會進行處理，接著 `yaya_shiori3.dic` 會將結果以如下所示的字串傳回給 baseware。

```
SHIORI/3.0 200 OK
Sender: AYA
Charset: UTF-8
Value: \0\s[0]あ、エミリさん。\1\s[10]テディも元気そうだな。
Reference0: Emily
```

| 標頭 | 內容 |
|--------|------|
| `SHIORI/3.0 200 OK` | 自動傳回適當的代碼 |
| `Sender: AYA` | 自動附加 |
| `Charset: UTF-8` | 自動傳回適當的代碼 |
| `Value: ～` | 函式的執行結果（也就是對話） |
| `Reference0: Emily` | 若存在名為 `res_reference*`（`*` 為數字）的全域變數，則會將其值放入此處（baseware 會將 SHIORI 傳回的 Reference0 視為通訊對象的人格名稱） |

## 隨機對話

為了方便進行隨機對話，此辭典具備每隔 `aitalkinterval` 秒呼叫一次 `OnAiTalk` 函式的功能。原本 baseware 並沒有 `OnAiTalk` 這項功能，是 `yaya_shiori3.dic` 新增了此功能。

## 內部轉換

此辭典具備在處理完所有事件後呼叫 `OnTranslateInternal` 函式的功能。此時傳入的引數（`_argv[0]`）是準備輸出至 baseware 的對話內容。此函式傳回的內容，會成為實際輸出至 baseware 的對話。因此，可以在 `OnTranslateInternal` 中適當處理 `_argv[0]` 再傳回，以對所有對話一律進行轉換等處理。

## 鏈式對話

鏈式對話是指「以某段對話為契機，依指定順序進行一連串對話」的功能。此功能同樣由 `yaya_shiori3.dic` 實作。

在對話的 `\e` 後方寫上 `:chain=○○`，即可啟動鏈式對話（`○○` 是用來區分鏈式對話的識別碼，除了 `end` 以外可以是任何字串）。啟動鏈式對話時，`OnAiTalk` 不會進行隨機對話，而是呼叫上文所述的 `○○` 函式（鏈式函式）（此功能並非記載於 `yaya_shiori3.dic`，而是記載於人格範本中）。

鏈式函式與一般函式不同，寫法如下（若指定 `:chain=hoge`）。

```
hoge
{{CHAIN
    "\0\s[0]りんご\e"
    "\0\s[1]ごりら\e"
    "\0\s[0]らっぱ\e:chain=end"
}}CHAIN
```

一般函式會從「りんご」、「ごりら」、「らっぱ」中隨機選出一項；鏈式函式則會依序串接對話。若在 `\e` 後方寫上 `:chain=end`，即可停止鏈式對話。

### Chain 分隔符號（`:chain=`）

在對話腳本的結尾加上 `:chain=事件名`，下次有隨機對話機會時，就會呼叫指定的事件。

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

## 延遲 EVAL

在 `\e` 後面寫上 `:eval=運算式`，即可執行該運算式（實際上等同於寫成 `EVAL(運算式)`）。例如，寫成 `"\0\s[0]はじめまして。\e:eval=aisatu=1"`，就能輕鬆實作「以說出某段對話為契機的旗標處理」之類的功能。

基於安全性考量，此功能預設為停用。若要啟用，請充分了解安全風險，再將 `config.dic` 中的 `SHIORI3FW.ENABLE_DELAYED_EVAL` 設為 1。

## 已安裝人格清單

解讀 `ID: installedghostlist`，並建立全域變數 `installedghostlist`（人格名稱的通用陣列）等變數。

收到 `OnNotifyInstalledGhostName` 等事件時，以下變數會自動更新。索引彼此對應，`installedghostlist[i]` 中人格的櫻名會是 `installedsakuralist[i]`。

| 變數名稱 | 內容 |
|--------|------|
| `installedghostlist` | 已安裝人格的人格名稱陣列 |
| `installedsakuralist` | 已安裝人格的櫻名陣列 |
| `installedkerolist` | 已安裝人格的凱洛名陣列 |

## SAORI 呼叫

為了方便呼叫 SAORI，`yaya_shiori3.dic` 提供了以下函式。載入與卸載 SAORI 也會在使用 `FUNCTIONEX` 時自動進行。

### FUNCTIONEX

```
FUNCTIONEX( dllname [, Argument0 , Argument1 , ... ] )
```

| 引數 | 說明 |
|------|------|
| `dllname` | 要呼叫的 SAORI DLL 名稱。以相對於 `yaya.dll` 的路徑指定 |
| `Argument0, 1, ...` | 傳給 SAORI 的引數（可省略） |

`FUNCTIONEX` 的傳回值會是 SAORI 的傳回值（Result 的值）。若 SAORI 傳回更多值（Value0、1、…），則會存入 `valueex` 陣列及全域變數 `valueex0`、`valueex1`、… 中。

```
_result = FUNCTIONEX('kawari8.dll', 'こんにちは')
// 追加の戻り値は valueex[0], valueex[1], ... で参照
```

詳情請參閱 [FUNCTIONEX](../functions/FUNCTIONEX.md)。

#### baseware 內建模組（SAORI over DirectSSTP）

當 `dllname` 以 `internal_` 開頭時（例如 `internal_crypto`、`internal_time.dll` 等；大小寫不拘，結尾的 `.dll` 可有可無），不會載入 DLL，而是透過 `DIRECTSSTP` 呼叫 baseware（SSP 2.9.13 以上版本）的內建模組。寫法、傳回值、`valueex`、`LIB.STATUSCODE` 都與 DLL 的 SAORI 相同。模組與函式請參閱 [SAORI over DirectSSTP](https://ssp.shillest.net/ukadoc/manual/spec_saori_ex.html)。

```
_hash = FUNCTIONEX('internal_crypto', 'Digest', 'sha256', 'abc')
_text = FUNCTIONEX('internal_time', 'Format', 0, '%Y/%m/%d', '--tz=+09:00')
```

- 模組無法使用時（舊版 SSP、SSP 以外的 baseware、不明模組），會傳回 0。每個模組只會在第一次確認能否使用時，透過 `GET Version SAORI/1.0` 查詢並記住結果。若在啟動後不久、尚未得知人格視窗（`SHIORI3FW.HWnd[0]`）時呼叫，則不會記住結果，而是傳回 0
- 發生錯誤時（400、500），Result 為空，`LIB.STATUSCODE` 會包含 `400 Bad Request` 等內容。錯誤原因（`ErrorDescription`）可從 `var.lib.key` / `var.lib.value` 讀取
- 若引數含有換行（CR・LF），可能會被用來追加標頭，因此不會送出並傳回 0。包含換行或前後空白的資料，請使用 `--data-in=base64` 等格式傳遞
- 字元編碼固定為 UTF-8
- 對於耗時的處理（例如 `DeriveKey`、`HashPassword`），請加上 `--async=識別碼`。結果稍後會透過事件（例如 `OnInternalSaoriComplete`）送達，`FUNCTIONEX` 的傳回值會是空（`LIB.STATUSCODE` 為 `204 No Content`）

### SAORI

`FUNCTIONEX` 的同義名稱（別名）。寫法與 `FUNCTIONEX` 相同（`internal_` 內建模組也相同）。由於多了一層包裝，速度比 `FUNCTIONEX` 慢，但差異不至於需要在意。

### FUNCTIONLOAD

載入 SAORI DLL。引數為 SAORI DLL 檔案名稱。成功時傳回 1，失敗時傳回 0。

```
FUNCTIONLOAD('kawari8.dll')
```

### SHIORI3FW.SaoriUnloadAll

卸載目前已載入的所有 SAORI DLL。沒有引數，也沒有傳回值。

## baseware 屬性函式

讀寫 SSP 等支援 DIRECTSSTP 的 baseware 屬性，或執行 EXECUTE SSTP 指令。

| 函式 | 說明 |
|------|------|
| `EXECUTE_SSTP(指令名稱, 引數0, 引數1, ...)` | 向 baseware 傳送 `EXECUTE SSTP/1.1`，並傳回結果（追加資料） |
| `GET_PROPERTY(屬性名稱)` | 取得屬性值。成功時傳回屬性值字串，失敗時傳回空字串 |
| `SET_PROPERTY(屬性名稱, 值)` | 設定屬性值。成功時傳回 1，失敗時傳回 0 |

```
_vol = GET_PROPERTY('volume')
SET_PROPERTY('volume', '80')
```

### EXECUTE_SSTP

```
EXECUTE_SSTP( コマンド名 [, 引数0 , 引数1 , ... ] )
```

透過 DIRECTSSTP 向 baseware 傳送 `EXECUTE SSTP/1.1` 請求，並傳回結果。第二個以後的引數會以 `Reference0`、`Reference1`、… 的形式傳送。可用的指令請參閱 baseware 的 SSTP 規格（例如 `GetVersion`、`GetGhostNameList`、`GetStatus`、`GetCookie`）。

- 傳回值：成功時（狀態為 2xx），傳回空行之後的追加資料（會移除末尾的換行）。失敗時傳回空字串。傳回清單的指令會以 `C_CRLF` 分隔結果字串
- 結果變數：`SSTP.STATUSCODE` 會存入狀態行的結果（例如 `200 OK`、`501 Not Implemented`），`SSTP.STATUS` 會存入該狀態碼的數值。無法傳送時，兩者分別為 `''` 和 0
- 若指令或引數含有換行（CR・LF），可能會被用來追加標頭，因此不會送出並傳回空字串（`SSTP.STATUS` 為 0）

沒有追加資料的指令即使成功，也會傳回空字串，因此請透過 `SSTP.STATUS` 確認是否成功。

```
_ver = EXECUTE_SSTP('GetShortVersion')
_ghosts = SPLIT(EXECUTE_SSTP('GetGhostNameList'), C_CRLF)

_dummy = EXECUTE_SSTP('SetCookie', 'mykey', 'value')
if SSTP.STATUS == 200 || SSTP.STATUS == 204 {
	// 成功
}
```

`GET_PROPERTY` 等同於 `EXECUTE_SSTP('GetProperty', 屬性名稱)`，`SET_PROPERTY` 等同於 `EXECUTE_SSTP('SetProperty', 屬性名稱, 值)`；`SSTP.STATUSCODE` 和 `SSTP.STATUS` 也會以相同方式設定。

## 陣列操作

| 函式 | 說明 |
|------|------|
| `JOIN(値0, 値1, ..., 区切り文字)` | 將最後一個引數作為分隔字元，串接其他值（傳入陣列時會依序串接各元素），並傳回字串 |
| `REVERSE(値0, 値1, ...)` | 傳回引數順序反轉後的陣列 |
| `UNIQUE(値0, 値1, ...)` | 傳回移除引數中重複值後的陣列（[ARRAYDEDUP](../functions/ARRAYDEDUP.md) 的包裝函式） |
| `SPLITEX(文字列, 区切り文字)` | 與 [SPLIT](../functions/SPLIT.md) 相同，但不會將內容為空的元素轉換為陣列元素 |
| `MAX(値0, 値1, ...)` | 傳回引數中的最大值。若包含字串，則傳回字典順序中最後面的字串 |
| `MIN(値0, 値1, ...)` | 傳回引數中的最小值。若包含字串，則傳回字典順序中最前面的字串 |
| `AVERAGE(値0, 値1, ...)` | 傳回引數的平均值。若包含字串，則傳回空字串 |

```
_配列 = ("A","B","C","D","E")
結果 = JOIN(_配列, "★")   // "A★B★C★D★E"
```

## 文字處理・狀態確認

### SHIORI3FW.RemoveAllTags

傳回移除所有 Sakura Script 標籤（例如 `\0`、`\s[0]`）後的字串。

```
_plain = SHIORI3FW.RemoveAllTags('\0\s[0]こんにちは。\e')
// → "こんにちは。"
```

若要顯示標籤的跳脫字元，而非移除標籤，請使用 [SHIORI3FW.EscapeAllTags](./yaya-optional-dic.md#shiori3fwescapealltags)。

### SHIORI3FW.CanTalk

傳回目前人格是否處於可對話的狀態。若 `status` 標頭包含 `talking`、`choosing`、`minimizing`、`timecritical` 其中之一，則判定為不可對話。可對話時傳回 1，不可對話時傳回 0。

```
if SHIORI3FW.CanTalk {
	// ランダムトーク発動
}
```

## 延遲事件（「延後對話」事件）

在指定秒數後，僅觸發一次特定事件。事件會在 `OnSecondChange`（每秒一次）的時機處理。

### SHIORI3FW.SetDelayEvent

```
SHIORI3FW.SetDelayEvent( '発生させるイベント名' , 遅れる秒数 [, Reference0, ...] )
```

註冊延遲事件。若事件名稱為空字串，則取消事件。第 3 個引數起的值是事件觸發時要設定的 Reference 值（可省略）。

```
// 10秒後に OnMyDelayedEvent を発動
SHIORI3FW.SetDelayEvent('OnMyDelayedEvent', 10)

// キャンセル
SHIORI3FW.SetDelayEvent('', 0)
```

### SHIORI3FW.GetDelayEvent

以 `(事件名稱, 剩餘秒數, Reference 陣列)` 的形式，傳回目前已註冊的延遲事件資訊。

## 新增回應標頭

可以在事件處理常式的回應中新增任意標頭。設定會在每個請求後重設。

| 函式 | 說明 |
|------|------|
| `SHIORI3FW.PushAdditionalReturn(ヘッダ名, 値)` | 新增任意回應標頭 |
| `SHIORI3FW.Push_X_SSTP_PassThru(名前, 値)` | 新增 `X-SSTP-PassThru-名前` 標頭（用於 SSTP 直通傳遞） |

在事件處理常式中，為下列變數設定值後，該值會自動附加至回應標頭。

| 變數名稱 | 標頭 | 內容 |
|--------|--------|------|
| `res_reference` 或 `res_reference0` ～ `res_reference31` | `Reference0:` ～ | 事件回應的 Reference 值。可使用陣列或個別變數指定 |
| `marker` 或 `res_marker` | `Marker:` | SSTP 標記值 |
| `res_securitylevel` | `SecurityLevel:` | 安全性等級 |
| `res_valuenotify` | `ValueNotify:` | ValueNotify 值 |

```
OnMyEvent
{
	res_reference0 = 'value0'
	res_reference1 = 'value1'
	'\0\s[0]処理しました。\e'
}
```

`res_reference` 的索引上限由 `config.dic` 的 `SHIORI3FW.RES_REF_MAX` 決定（初始值為 32）。

## 變數管理工具

### SHIORI3FW.RegisterTempVar

```
SHIORI3FW.RegisterTempVar( 変数名, ... )
```

註冊在結束時（unload 時）自動刪除的全域變數。可用於管理不需要保存的暫時性全域變數。

```
myTempVar = '一時データ'
SHIORI3FW.RegisterTempVar('myTempVar')
```

## 擬似事件

在人格的辭典中定義這些函式後，會在特定時機呼叫。

| 函式 | 呼叫時機 |
|------|------------------|
| `OnSHIORI3FW.SurfaceRestore` | AI 對話間隔經過 2/3 時。可用於在對話前將表面恢復為預設狀態等處理 |
| `OnSHIORI3FW.ChangeSelfInfo` | 人格名稱、外殼名稱、外殼路徑、對話方塊名稱或對話方塊路徑更新時 |
| `OnSHIORI3FW.WindowCreate` | 新建立人物視窗時。`reference[0]` 中會存入 scope 編號 |
| `OnSHIORI3FW.WindowDestroy` | 人物視窗被銷毀時。`reference[0]` 中會存入 scope 編號 |

```
OnSHIORI3FW.SurfaceRestore
{
	'\0\s[0]\1\s[10]\e'
}
```

## 系統變數

為了方便使用原本不易直接使用的函式，提供了下列變數。這些變數可用於取得系統資訊。由於系統會自動更新這些變數，請僅用於讀取。

### 時間相關變數

| 變數名稱 | 傳回值 |
|--------|--------|
| `year` | 目前日期時間的年份數值 |
| `month` | 目前日期時間的月份數值 |
| `day` | 目前日期時間的日期數值 |
| `weekday` | 目前日期時間的星期數值（0=星期日、1=星期一 … 6=星期六） |
| `hour` | 目前日期時間的小時數值（24 小時制） |
| `ampm` | 目前日期時間的上午或下午數值（0=AM、1=PM） |
| `hour12` | 目前日期時間的小時數值（12 小時制） |
| `hour12ex` | 目前日期時間的小時數值（12 小時制）。但 12 會顯示為 0 時或 12 時 |
| `minute` | 目前日期時間的分鐘數值 |
| `second` | 目前日期時間的秒數值 |
| `systemuptime` | 作業系統連續運作時間（單位：秒） |
| `systemupsecond` | 將作業系統連續運作時間換算為時分秒時的秒數 |
| `systemupminute` | 將作業系統連續運作時間換算為時分秒時的分鐘數 |
| `systemuphour` | 將作業系統連續運作時間換算為時分秒時的小時數 |
| `ghostupmin` | 人格連續運作時間（單位：分鐘） |
| `ghostupmin_total` | 人格累計運作時間（單位：分鐘） |
| `ghostuptimes` | 人格累計啟動次數 |

### 記憶體相關變數

| 變數名稱 | 傳回值 |
|--------|--------|
| `memoryload` | 實體記憶體使用率 |
| `memorytotalphys` | 實體記憶體容量 |
| `memoryavailphys` | 可用實體記憶體容量 |
| `memorytotalvirtual` | 虛擬＋實體記憶體容量 |
| `memoryavailvirtual` | 可用虛擬＋實體記憶體容量 |

### Sender 標頭相關變數

| 變數名稱 | 傳回值 |
|--------|--------|
| `basewarenameex` | 人格啟動時所用的 baseware 名稱（MATERIA 為 `embryo`、CROW 為 `crow`、SSP 為 `SSP`）。此值為首次啟動時的值，不會變更 |
| `basewarename` | 目前請求的來源 baseware 名稱（Sender 標頭名稱；有時也會是 baseware 名稱以外的值） |
| `sender` | 與 `basewarename` 相同 |

### 人格與外殼資訊

| 變數名稱 | 內容 |
|--------|------|
| `SHIORI3FW.GhostName` | 目前的人格名稱 |
| `SHIORI3FW.ShellName` / `SHIORI3FW.ShellPath` | 目前的外殼名稱 / 外殼路徑 |
| `SHIORI3FW.BalloonName` / `SHIORI3FW.BalloonPath` | 目前的對話方塊名稱 / 對話方塊路徑 |
| `selfname` / `sakuraname` | Sakura（範圍 0）的角色名稱 |
| `keroname` | Kero（範圍 1）的角色名稱 |
| `SHIORI3FW.HWnd` | 角色視窗的 HWND 陣列。`[0]` 為 Sakura 端 |
| `SHIORI3FW.BalloonHWnd` | 對話方塊視窗的 HWND 陣列。`[0]` 為 Sakura 端 |
| `SHIORI3FW.LastSurface` | 上一個顯示的 Surface 編號陣列。`[0]` 為 Sakura 端 |
| `SHIORI3FW.IsVisible` | Surface 的顯示狀態（1=顯示中、0=隱藏）。`[0]` 為 Sakura 端 |
| `SHIORI3FW.UserName` / `SHIORI3FW.UserNameFull` | 使用者名稱（簡稱 / 全名） |
| `SHIORI3FW.UserBirthday` | 生日陣列 `[年, 月, 日]`（整數型別） |
| `SHIORI3FW.UserSex` | 性別 |
| `SHIORI3FW.LastTalk` | 上一次說出的指令碼（適用於所有事件） |
| `SHIORI3FW.LastAITalk` | 上一次隨機對話的指令碼 |
| `SHIORI3FW.Eventid` | 目前處理中的事件 ID |
| `SHIORI3FW.Status` | 初始啟動狀態（已由 `Run` 初始化） |
| `SHIORI3FW.UniqueID` | Auth.SSTP 使用的 ID |
| `SHIORI3FW.Capability` | baseware 的標頭處理能力（通用陣列） |

## 使用者設定變數

可讀寫的變數，用於自訂人格的行為。

| 變數名稱 | 初始值 | 內容 |
|--------|--------|------|
| `aitalkinterval` | 180（秒） | AI 對話（隨機對話）的觸發間隔。設為 0 可停用 |
| `communicateratio` | 0（%） | AI 對話觸發時，選擇開始溝通的比例 |

```
aitalkinterval = 300
```

## config.dic 的主要設定

可透過 `config.dic` 變更系統行為。

| 常數名稱 | 初始值 | 內容 |
|--------|--------|------|
| `TALK_INTERVAL` | 180 | `aitalkinterval` 的初始值（秒） |
| `COM_RATIO` | 0 | `communicateratio` 的初始值（%） |
| `SHIORI3FW.IGLIST_ACCEL` | 1 | 設為 1 時，使用 SSP / CROW 的 NOTIFY 事件快速建立人格清單（不會建立 Sakura 名稱與 Kero 名稱的清單） |
| `SHIORI3FW.IGLIST_MAX` | 0 | 透過掃描檔案建立人格清單時，取得人格的最大數量。設為 -1 表示不限數量，設為 0 則不取得 |
| `SHIORI3FW.RES_REF_MAX` | 32 | `res_reference*` 變數的索引上限 |
| `SHIORI3FW.AUTO_DATA_CONVERT` | 0 | 設為 1 時，自動轉換 SAORI 傳回值等資料的型別，並將位元組值 1 替換為逗號（相容於 AYA5） |
| `SHIORI3FW.REF_ACCEL` | 0 | 設為 1 時，不建立 `reference0` 等變數，只使用 `reference[0]`（提升速度） |
| `SHIORI3FW.ENABLE_DELAYED_EVAL` | 0 | 啟用透過 `:eval=` 執行的延遲 EVAL（基於安全考量，建議停用） |

## AI 圖表的預設值

SSP 的 AI 圖表（雷達圖）會使用 SHIORI 資源 `getaistate` 繪製。若人格端沒有 `On_getaistate`，或其傳回空值，系統辭典的 `SHIORI3EV.On_getaistate` 就會傳回以下 6 個軸的資料。若在人格端定義 `On_getaistate`，則會優先使用該定義。

| 標籤 | 顯示值 | 增加值 | 最大值 |
|--------|--------|--------|--------|
| `Boot` | `ghostuptimes`（累計啟動次數） | 0 | 階梯式尺度 |
| `Uptime(h)` | `ghostupmin_last / 60`（截至上一次的累計啟動時間） | `ghostupmin / 60`（本次啟動時間） | 階梯式尺度 |
| `Memory` | `GETVARLIST()` 的元素數量 | 0 | 階梯式尺度 |
| `Repertoire` | `GETFUNCLIST('On')` 的元素數量 | 0 | 階梯式尺度 |
| `Talk/h` | `3600 / aitalkinterval`（若 `aitalkinterval` 小於或等於 0，則為 0） | 0 | 階梯式尺度 |
| `Social` | `communicateratio` | 0 | 100 |

- 階梯式尺度會取可容納該值的最小值：10、20、50、100、200、500、…（`SHIORI3FW.AIGraphMax`）
- `Memory` 與 `Repertoire` 也會計入系統辭典本身的變數與函式
- `Uptime(h)` 的顯示值與增加值為小數（SSP 2.4.26 以後的版本可處理小數）

## 相關項目

- [yaya_optional.dic](./yaya-optional-dic.md)
- [FUNCTIONEX](../functions/FUNCTIONEX.md)
- [系統辭典函式手冊（yaya-dic）](https://github.com/YAYA-shiori/yaya-dic/blob/master/docs/manual_yaya_base.md)
