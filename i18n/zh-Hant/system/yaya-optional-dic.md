# yaya_optional.dic

## 概要

`yaya_optional.dic` 是包含輔助工具函式的系統辭典，並非必要，但有的話會很方便。它會與 `shiori3.dic`（[yaya_shiori3.dic](./yaya-shiori3-dic.md)）一同自動載入。提供操作 Sakura Script 標籤、整理字串、初始化對話方塊、偵測人格（FMO）等功能。

## SHIORI3FW.EscapeDangerousTags

```
SHIORI3FW.EscapeDangerousTags( script )
```

將字串中包含的「危險」Sakura Script 標籤停用（跳脫）。只會將執行危險操作的標籤（例如啟動瀏覽器、啟動郵件軟體、切換被動模式等）中的反斜線跳脫為 `\\`，安全的標籤則會保持原樣。

目前視為「危險」的標籤如下。

- `\![]` 中包含下列字串的標籤：`updatebymyself` / `vanishbymyself` / `enter,passivemode` / `leave,passivemode` / `lock,repaint` / `unlock,repaint` / `biff` / `open,browser` / `open,mailer` / `raise`
- `\j[]` 標籤

| 引數 | 說明 |
|------|------|
| `script` | 要停用的字串 |

傳回值為停用後的字串。

```
_safe = SHIORI3FW.EscapeDangerousTags(外部から受け取ったテキスト)
```

## SHIORI3FW.EscapeAllTags

```
SHIORI3FW.EscapeAllTags( script )
```

將字串中包含的「所有」Sakura Script 標籤跳脫。無論內容為何，只要以 `\` 開頭就會跳脫。可用於將使用者輸入直接顯示在對話方塊中等情況。

| 引數 | 說明 |
|------|------|
| `script` | 要跳脫的字串 |

傳回值為跳脫後的字串。

```
_display = SHIORI3FW.EscapeAllTags('\0\s[0]これはタグではなくテキストです。\e')
// → "\\0\\s[0]これはタグではなくテキストです。\\e" として表示される
```

[SHIORI3FW.RemoveAllTags](./yaya-shiori3-dic.md#shiori3fwremovealltags) 會**刪除**標籤，而此函式則會**跳脫並顯示**標籤。

## SHIORI3FW.TranslateSystemChar

```
SHIORI3FW.TranslateSystemChar( text [ , 置換文字 ] )
```

將 YAYA 的運算子、分隔符號等系統保留字元替換為指定字元。適合用來產生可安全用作變數名稱或識別字的字串。

| 引數 | 說明 |
|------|------|
| `text` | 要處理的文字 |
| `置換文字` | 替換後的字元（省略時為 `_`） |

```
_varname = SHIORI3FW.TranslateSystemChar('hello world!')
// → "hello_world_"

_varname = SHIORI3FW.TranslateSystemChar('foo/bar', '-')
// → "foo-bar"
```

## 字串整理

適用於整理對話方塊中的選單等需要對齊顯示寬度的情況。指定的字元數一律以**半形換算**（1 個全形字元＝2 個半形字元）計算。

| 函式 | 說明 |
|------|------|
| `SHIORI3FW.MakeLongText(テキスト, 文字数)` | 若文字未達指定的半形換算字元數，會在末尾補上空格以對齊長度。若已達或超過指定長度，則原樣傳回文字 |
| `SHIORI3FW.MakeShortText(テキスト, 文字数)` | 若文字超過指定的半形換算字元數，會截去末尾並加上 `...` 或 `..`。若在指定長度以內，則原樣傳回文字 |
| `SHIORI3FW.MakeJustText(テキスト, 文字数)` | 結合上述兩個函式，將文字整理成指定的半形換算字元數 |

```
_item  = SHIORI3FW.MakeJustText('設定', 20)
_short = SHIORI3FW.MakeShortText('これはとても長いテキストです', 10)   // "これは..." のように切り詰められる
```

## SHIORI3FW.InitBalloons

```
SHIORI3FW.InitBalloons()
```

產生一段 Sakura Script，用來清除目前所有有效作用域的對話方塊。適用於在多作用域環境中一次重設所有對話方塊。無引數，傳回值是串接所有作用域的 `\p[n]\c\b[-1]` 後所形成的 Sakura Script 字串。

```
OnMyEvent
{
	SHIORI3FW.InitBalloons + '\0\s[0]初期化しました。\e'
}
```

## FMO 相關

FMO（File Mapping Object）是 SSP 管理的「目前正在執行的人格資訊」共用記憶體。使用下列函式可以確認其他人格是否存在，或取得相關資訊。

### SHIORI3FW.IsGhostExist

```
SHIORI3FW.IsGhostExist( name [ , fmoname ] )
```

透過 FMO 檢查指定名稱（\0 名）的人格目前是否正在執行。由於使用 FMO，因此可以取得呼叫此函式當下的資訊。函式內部會呼叫 `SHIORI3FW.RefreshFMOTable`。

| 引數 | 說明 |
|------|------|
| `name` | 人格名稱 |
| `fmoname` | 要檢查的 FMO 名稱（可省略。省略時為 `Sakura`，通常可省略） |

若該人格正在執行，傳回 1；若未執行，則傳回 0。

```
if SHIORI3FW.IsGhostExist('ゆっくり霊夢') {
	'\0\s[0]霊夢がいるよ！\e'
}
```

### SHIORI3FW.RefreshFMOTable

```
SHIORI3FW.RefreshFMOTable( [ fmoname [ , hwnd ] ] )
```

使用 [READFMO](../functions/READFMO.md) 函式，將 FMO 建構為易於處理的字串陣列。FMO 包含「目前正在執行的」人格資訊，因此使用此函式可以即時取得執行中人格的資訊。若 FMO 內容與上次相同，則會略過重新解析（快取）。

| 引數 | 說明 |
|------|------|
| `fmoname` | 要讀取的 FMO 名稱（可省略。省略時為 `Sakura`；Unicode 版為 `SakuraUnicode`。通常可省略） |
| `hwnd` | 要忽略的人格視窗控制代碼（可省略。省略時會使用 `SHIORI3FW.HWnd[0]`。通常可省略） |

此函式沒有傳回值，但會建構下列全域變數。這些變數會在 SHIORI 結束時自動清除。

「暫時啟動」（例如 SSTPVIEWER 或虛擬項目）的人格會自動從 FMO 表格中排除。

#### SHIORI3FW.FMOTable

格式為以逗號和 `|` 分隔的簡易陣列。在 SSP 中所有項目都會填入，但在某些 baseware 中可能會有不存在（空白）的項目。此外，無法在 Windows 以外的作業系統上使用。

```
id|name|keroname|hwnd|kerohwnd|path|ghostpath,
id|name|keroname|hwnd|kerohwnd|path|ghostpath,
...
```

| 項目 | 意義 |
|------|------|
| `id` | 表示人格的 ID。通常是無須知道其意義的字串 |
| `name` | \0 名 |
| `keroname` | \1 名 |
| `hwnd` | \0 的視窗控制代碼 |
| `kerohwnd` | \1 的視窗控制代碼 |
| `path` | 人格的安裝目錄（通常是 `ssp.exe` 所在位置，但 SSP 可以有多個人格安裝位置） |
| `ghostpath` | 人格的根目錄。也就是存放 `install.txt` 和 `thumbnail.png` 的位置 |

#### SHIORI3FW.SakuraNameList

格式為通用陣列。從上述資料中擷取 \0 名所組成的陣列。例如，使用 `ANY(SHIORI3FW.SakuraNameList)`，即可輕鬆從執行中的人格中隨機選出一個並取得其名稱。

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

上次讀取的 FMO 原始資料（用於快取）。較少直接參照。

#### 備註

一般情況下，由於會將 `SHIORI3FW.HWnd[0]` 指定為 `hwnd`，上述變數不會包含自身的資訊。若要包含自身，請將 `hwnd` 設為 -1 等值。

## SHIORI3FW.HTTPCodeToMessage

```
SHIORI3FW.HTTPCodeToMessage( コード )
```

將網路更新等作業傳回的 HTTP 狀態碼轉換為日文錯誤訊息。若沒有對應的代碼，則傳回空字串。

| 代碼 | 傳回值 |
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

## 相關

- [yaya_shiori3.dic](./yaya-shiori3-dic.md)
- [系統辭典內函式手冊（yaya-dic）](https://github.com/YAYA-shiori/yaya-dic/blob/master/docs/manual_yaya_base.md)
