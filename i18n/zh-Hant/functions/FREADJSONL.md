# FREADJSONL
**Category:** ファイル操作

## Signature
```
FREADJSONL( path [, start [, maxlines [, key ...]]] )
```

## Parameters
| 參數 | 說明 |
|-----------|-------------|
| path | 要讀取的 JSON Lines 檔案路徑（相對於 yaya.dll 的路徑，或絕對路徑） |
| start | 開始讀取的位元組位置（可省略，預設為 0）。若指向行的中間，會跳過該行並從下一行開始讀取（[從行的中間讀取](#行の途中から読む)）。範圍為 0 以上、2147483647 以下 |
| maxlines | 讀取行數的上限（可省略，預設為 0，讀取至檔案結尾）。空行及無法解析的行也會計入 |
| key | 要擷取的鍵（可省略，可指定任意數量）。各行的最上層為物件時，只傳回該鍵的值（[指定鍵讀取](#キーを指定して読む)）。僅限字串 |

## Returns
- 成功時：包含以下鍵的雜湊
  - `rows`：成功解析為 JSON 的各行值所組成的陣列（轉換方式與 [FREADJSON](FREADJSON.md#値の対応) 相同）
  - `pos`：對應 `rows` 各元素之行首位元組位置的陣列（順序與 `rows` 相同）
  - `end`：讀取結束的位置。繼續讀取時，將此值傳入 `start`
  - `skipped`：無法解析為 JSON 而跳過的行數
- 失敗時：空（VOID）

## Description
讀取 JSON Lines（每行寫入一個 JSON 的文字格式，副檔名為 `.jsonl`）檔案，並以各行值的陣列傳回。不需要事先用 [FOPEN](FOPEN.md) 開啟。

結果與用 [FREAD](FREAD.md) 逐行讀取，再用 [PARSEJSON](PARSEJSON.md) 解析相同；但此函式以 UTF-8 一次讀取檔案並逐行解析，不需按行數重複呼叫函式及轉換字串，因此速度較快。適合讀取對話紀錄或歷程等持續追加、行數增至數萬的檔案。

- 字元編碼僅支援 UTF-8。忽略開頭的 BOM
- 以 LF 分隔行。忽略行尾的 CR。只含空白的行會被跳過
- 無法解析為 JSON 的行會被跳過，不輸出警告，並計入 `skipped`。最上層不是物件或陣列的行（如 `42`），只要能解析也會放入 `rows`
- 不能寫入 `/* */` 或 `//` 註解（JSON Lines 沒有註解，這點與 [FREADJSON](FREADJSON.md) 不同）
- `pos` 的位置是從檔案開頭起算的位元組數，與 [FSEEK](FSEEK.md) 及 [FTELL](FTELL.md) 使用的位置相同

### 最後一行尚未寫入完成時
最後一行未以換行結尾時，若能解析為 JSON，則讀取該行；若無法解析（可能是其他程式正在寫入），則不讀取並保留。此時 `end` 會是該行的開頭。將 `end` 傳入下次的 `start`，便能在寫入完成後從該行開始讀取。

### 從行的中間讀取
若 `start` 前一個位元組不是換行，則視 `start` 為行的中間，捨棄第一個不完整的行。只想讀取檔案末尾時，可以傳入從 `FSIZE` 減去想讀取的位元組數所得的位置。若 `start` 是行首（0、上次的 `end` 或 `pos` 的值），則從該行開始讀取。

當 `start` 大於或等於檔案大小時，不讀取任何內容，`rows` 和 `pos` 為空陣列，`end` 為 `start`。

### 指定鍵讀取
指定 `key` 時，若各行的最上層為物件，只會將該鍵的值組成雜湊並放入 `rows`。雖然會解析整行 JSON，但只需轉換指定鍵的結果（字串轉換與雜湊建立），因此從包含請求本文等大型值的行中只擷取時間等資料時速度較快，結果也較小。

- 僅支援最上層的鍵。無法用 `.` 指向下層（`"a.b"` 指的是名稱中含有 `.` 的鍵）
- 行中不存在的鍵也不會建立於結果雜湊中。值為 `null` 的鍵則與轉換整體時相同，以 VOID 值保留
- 最上層不是物件的行，則不使用 `key`，而是轉換整體
- 鍵也可以用陣列傳入（函式引數中，外層陣列會被展開）。可以寫成 `FREADJSONL("a.jsonl", 0, 0, _keys)`

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| path 不是字串。start、maxlines 不是整數。key 不是字串 | W0009 | 9 |
| start 為負數或超過 2147483647。maxlines 為負數 | W0012 | 12 |
| 無法開啟檔案 | W0025 | 25 |

## Example
history.jsonl:
```
{"display":"こんにちは","timestamp":1790311762291,"project":"C:\\work\\a"}
{"display":"つづき","timestamp":1790311800000,"project":"C:\\work\\b"}
```

```
_r = FREADJSONL("history.jsonl", 0, 0, "timestamp", "project")
_r["rows"][0]["project"]    // C:\work\a
_r["rows"][1]["timestamp"]  // 1790311800000
_r["pos"][1]                // 2 行目の頭のバイト位置
_r["skipped"]               // 0
```

只讀取新增的部分（記住 `end`，並在下次呼叫時傳入 `start`）：
```
if GETTYPE(lastpos) == 0 {
    lastpos = 0
}
_r = FREADJSONL("history.jsonl", lastpos, 0, "timestamp", "project")
lastpos = _r["end"]
foreach _r["rows"]; _row {
    // 新しく書き足された行だけが順に入る
}
```

## Compatibility
- Tc608-6: 新增

## See Also
- [FREADJSON](FREADJSON.md)
- [PARSEJSON](PARSEJSON.md)
- [FREAD](FREAD.md)
- [FSEEK](FSEEK.md)
