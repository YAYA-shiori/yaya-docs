# 基礎設定

## 概要

YAYA 的預設 DLL 檔案名稱是 `yaya.dll`，主檔名 `yaya` 可以自由變更為其他名稱。

要讓 YAYA 運作，需要一個稱為「基礎設定檔案」的檔案。基礎設定檔案的檔案名稱是「主檔名.txt」，預設為 `yaya.txt`。如果將 DLL 檔案名稱變更為 `hoge.dll`，基礎設定檔案就會是 `hoge.txt`。

基礎設定檔案是文字檔，會以執行作業系統的預設字元編碼解讀。若需要考慮國際化，為避免多位元組字元編碼相關的問題，基礎設定檔案應只使用 ASCII 編碼撰寫。

如果沒有設定檔，或沒有任何要載入的辭典，便會以[外殼模式](#シェルモード)運作（Tc574-7 / Tc602-12 以後的版本如此；在此之前，若沒有設定檔，會發生錯誤 E0005 並停止運作）。

## 設定範例

```
// dics
dic, basis.dic
dic, control./*doc*/ayc

// option parameters
charset, UTF-8
charset.dic, Shift_JIS
charset.setting, Shift_JIS
charset.output, UTF-8
charset.file, Shift_JIS
charset.save, UTF-8
charset.extension, Shift_JIS

msglang, english
log, executelog.txt
iolog, off
fncdepth, 16
```

設定時以逗號分隔指令與參數。空白行（只有換行符號的行）、`//` 之後的內容，以及以 `/*` 和 `*/` 包圍的區域都會視為註解。

## 載入時發生辭典錯誤時的行為

Tc555-1 以後的版本中，載入時若發生辭典錯誤，會先使用緊急用的基礎設定檔案再次嘗試載入。

緊急用基礎設定檔案的檔案名稱是「主檔名_emerg.txt」，預設為 `yaya_emerg.txt`。變更 DLL 名稱時的行為也與一般基礎設定檔案相同。

如果仍然發生錯誤，request 函式便不會傳回任何內容（NULL）。

發生問題時，可透過 [GETERRORLOG](../functions/GETERRORLOG.md) 取得錯誤記錄。

使用 `yaya_emerg.txt` 的緊急模式不會變成[外殼模式](#シェルモード)。如果沒有 `yaya_emerg.txt`，便會如同以往停止運作。

## 設定項目

### charset, name

設定標準字元編碼。請從下列保留值中指定一項。若未指定，則會視為 Shift_JIS。

- `Shift_JIS` / `ShiftJIS` / `SJIS`: Shift JIS 編碼
- `UTF-8`: UTF-8
- `default`: 執行作業系統的預設字元編碼

以下以 `charset.` 開頭的項目是個別設定。請務必寫在 `charset` 的整體指定之後。

### charset.dic

辭典的字元編碼。

### charset.setting

基礎設定檔案本身的字元編碼。

### charset.output

request 函式輸入與輸出的字元編碼。

### charset.log

記錄檔與對話方塊輸出的字元編碼（Tc569-15 以後的版本）。

### charset.file

檔案輸入與輸出的字元編碼。

### charset.save

全域變數存檔檔案輸入與輸出的字元編碼。

### charset.save.old

讀取未指定字元編碼的舊格式存檔檔案時使用的字元編碼。

### charset.extension

外部 DLL（SAORI 等）的輸入與輸出字元編碼。

### dic, filename ( , charset )

載入辭典檔案 `filename`。辭典檔案是撰寫 YAYA 指令碼的程式原始檔，YAYA 會根據其中編寫的內容運作。可以指定並載入任意數量的辭典檔案。

`filename` 請指定相對於 load 所指定路徑位置的相對路徑。

標準辭典檔案是以 `charset` 指定的字元編碼撰寫的純文字檔。此外，也可以載入依照特定規則進行混淆處理的加密檔案。

在檔案名稱後以逗號分隔加入字元編碼後，指定的檔案便會以該字元編碼載入。

### dicif, filename ( , charset )

與 `dic` 相同，但指定的檔案不存在時會忽略（Tc571-2 以後的版本）。

### dicdir, dirname ( , charset )

將指定目錄以下的所有檔案作為辭典載入（Tc556-1 以後的版本）。除了指定的是目錄之外，其餘與 `dic` 相同。

!!! warning "載入順序"
    檔案的讀取順序並不固定。因此，定義 `globaldefine` 等內容時，可能會因載入順序而發生問題。定義 `globaldefine` 時，務必將定義它的辭典檔案排在前面載入。

如果 `dicdir` 指定的目錄中有名為 `_loading_order_override.txt` 或 `_loading_order.txt` 的檔案，其行為就會與寫入 `includeEX,(目錄)/_loading_order.txt` 相同。會依照 `_loading_order_override.txt` → `_loading_order.txt` 的順序檢查檔案是否存在，並只對先找到的檔案執行 `includeEX`（Tc571-2 以後的版本）。

如果沒有指定 `dic`，或 `dicif` 的所有目標檔案都不存在，或 `dicdir` 指定的目錄是空的等，導致沒有任何要載入的辭典時，便會以[外殼模式](#シェルモード)運作（Tc574-7 / Tc602-12 以後的版本）。

### msglang, language

!!! note "通常不必指定"
    通常不必特別指定，錯誤訊息的語言會自動切換（Tc573-5 以後的版本）。

選擇記錄在記錄檔中的錯誤訊息等內容所使用的語言。請從下列保留值中指定一項。若未指定，則會視為 `japanese`。

- `japanese`
- `english`
- `chinese-simplified`
- `chinese-traditional`
- `german`
- `korean`

此設定是為了相容舊版本而保留。請改用 `messagetxt`。

### messagetxt, filename ( , charset )

!!! note "通常不需指定"
    通常不需特別指定，錯誤訊息的語言會自動切換（Tc573-5 以後）。

讀取記錄檔中錯誤訊息等內容所使用的語言檔案。例如可如下撰寫。省略 `charset` 時，會使用 UTF-8（含 BOM）（Tc557 以後）。

```
messagetxt,messagetxt/japanese.txt
messagetxt,messagetxt/english.txt
messagetxt,messagetxt/chinese-simplified.txt
messagetxt,messagetxt/chinese-traditional.txt
messagetxt,messagetxt/german.txt
messagetxt,messagetxt/korean.txt
```

語言檔案名稱可在 [yaya-shiori 的 messagetxt](https://github.com/ponapalt/yaya-shiori/tree/500/messagetxt) 確認。

Tc570-1 以後，Windows 上的語言檔案會嵌入 DLL，因此不需要另外發布語言檔案本身。`messagetxt` 中指定檔案名稱的規格仍予以保留，供 Windows 以外的環境使用。

### basepath, directory

將載入辭典等內容時作為基準的目錄重新設定為任意位置。未設定時，通常會使用與 `yaya.dll` 相同的目錄（Tc557 以後）。

### include, filename

從其他檔案載入基礎設定檔的內容。指定檔案的內容也會視為有效的基礎設定。

### includeEX, filename

基本上與 `include` 執行相同的處理，但如果 `filename` 指定的檔名包含目錄名稱，就會先暫時將目前目錄切換到該目錄，再執行 `include` 處理（Tc559 以後）。

### log, logfilename

將執行記錄寫入檔案 `logfilename`。寫入時會使用 `charset.log` 指定的字元編碼。`logfilename` 請指定相對於 load 所指定路徑位置的路徑。

### iolog, [on|off]

設定是否將執行 load、unload、request 時的輸入輸出字串及處理時間記錄到記錄檔。設為 `on` 時會記錄。預設為 `on`，不需要記錄時請設為 `off`。即使指定 `off`，若以拖放到玉上啟動的方式使用，也會強制設為 `on`。

### iolog.filter.keyword, [忽略判定字串]

如果 request 的字串中包含指定的忽略判定字串，就不會將該 request 的 I/O 記錄到記錄檔（也不會輸出至玉）。可以指定多個。舊定義名稱為 `ignoreiolog`。

例：不記錄 `OnSecondChange` 和 `OnMouse` 系列事件

```
ignoreiolog, ID: OnSecondChange //OnSecondChange無視
iolog.filter.keyword, OnMouse        //OnMouse系無視
```

由於基礎設定檔的格式，忽略判定字串前後的空白，以及註解 `//` 之後的內容都會被忽略。

### iolog.filter.keyword.delete, [字串]

刪除上述項目。這是提供給 [SETSETTING](../functions/SETSETTING.md) 使用的寫法，直接寫在定義檔中幾乎沒有意義。

### iolog.filter.keyword.regex, [忽略判定字串：正規表示式]

`iolog.filter.keyword` 的正規表示式版本。

### iolog.filter.keyword.regex.delete, [字串]

刪除上述項目。這是提供給 [SETSETTING](../functions/SETSETTING.md) 使用的寫法，直接寫在定義檔中幾乎沒有意義。

### iolog.filter.mode, [模式]

切換上述 `iolog.filter.keyword` 等判定條件的處理方式，決定要「不輸出符合條件的項目」，或是「只輸出符合條件的項目」。未定義時，會採用「不輸出符合條件的項目」模式。

```
iolog.filter.mode,allowlist
iolog.filter.mode,whitelist
```

切換為只輸出符合條件項目的模式。

```
iolog.filter.mode,denylist
iolog.filter.mode,blacklist
```

切換為不輸出符合條件項目的模式。

### fncdepth, [depth]

以數值指定函式呼叫的最大深度。預設值為 32。最小值為 2，指定更小的值或無效值時，也會以 2 處理。設為 0 時，不會檢查深度上限（Tc556-1 以後）。

達到上限時會呼叫 [shiori.OnCallLimit](../system/shiori-OnCallLimit.md)。

除了深度上限之外，Tc607-4 以後，當 YAYA 所在執行緒的堆疊剩餘空間不足（大約低於 128KB）時，也會像達到上限時一樣停止呼叫，並呼叫 `shiori.OnCallLimit`。被停止的呼叫傳回值會是空值。即使將 `fncdepth` 設為 0 或較大的值，也不會再因堆疊用盡而連同 baseware 一起當掉。停止時的呼叫深度會依 baseware 執行緒的堆疊大小而變（1MB 的堆疊可達數百層）。Tc607-3 以前，若設為 0 且呼叫深度過深，會連同 baseware 一起當掉。

### looplimit, [count]

以數值指定迴圈次數上限。預設值為 1000000（Tc574-10 / Tc606-4 以後；此前為 10000）。設為 0 時不會檢查上限，但會持續執行而造成凍結。對 `foreach` 無效（Tc564-1 以後）。

達到上限時會呼叫 [shiori.OnLoopLimit](../system/shiori-OnLoopLimit.md)。

### save.encode, [on|off]

加密存檔檔案。這種「加密」並不算什麼高明的加密，頂多只能稍微增加閱讀難度。一旦設為 `on`，存檔檔案就會一直保持加密狀態，直到刪除為止。變更設定時請務必小心。

### save.auto, [on|off]

切換自動儲存存檔檔案功能的開啟／關閉。開啟時，會定期備份，並在結束時自動儲存變數。關閉時，除非明確呼叫儲存函式，否則不會儲存。預設為開啟。

### embed.lazy, [on|off]

在執行時尋找字串中未加括號的 `%` 嵌入名稱（預設：`on`）。設為 `off` 時，會在讀取辭典時確定名稱（Tc604-1 以後。[詳細資訊](06-string-embedding.md#名前を読み込み時に確定する)）。

### maxlognum, [count]

設定可透過 [GETERRORLOG](../functions/GETERRORLOG.md) 取得的記錄最大值。預設值為 256 個元素。

## 外殼模式

Tc574-7 / Tc602-12 以後。若沒有設定檔，或沒有任何要讀取的辭典，YAYA 會以只讀取下列辭典的方式運作。

```c
load { }
unload { }
request { EVAL(_argv[0]) }
```

直接對傳入 request 的字串執行 [EVAL](../functions/EVAL.md)，並傳回其結果。除了單一運算式，也可以撰寫以 `;` 或換行分隔的陳述式序列，以及控制陳述式。即使不準備完整的人格或辭典，也能快速確認 YAYA 運算式及函式的運作方式。

| request 的輸入 | 傳回值 |
|---------------|------|
| `1+2` | `3` |
| `_a = 3; _a * 5` | `15` |
| `'hello' + ' world'` | `hello world` |
| `X = 10` | 空字串（全域變數 `X` 會被設為 10） |
| `X` | `10` |

- 全域變數會在同一個工作階段期間保留
- 沒有設定檔時，不會自動儲存或還原變數（`yaya_variable.cfg`）。若有設定檔，但未指定辭典，則會依照 `save.auto` 等設定處理
- 進入外殼模式時，記錄中會出現註記 N0002
- 若發生 `dic` 指定的辭典檔案不存在、辭典有語法錯誤、`include` 的目標不存在等錯誤，就不會進入外殼模式
- SHIORI 的 request 也會直接執行 EVAL，因此此模式並非用來作為人格使用。預期的用法是使用 YAYA 執行檔版本（`yaya.exe`），先對空目錄執行 `load`，再透過 `request` 傳送運算式
