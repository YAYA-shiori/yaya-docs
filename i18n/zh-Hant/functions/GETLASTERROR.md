# GETLASTERROR
**Category:** デバッグ

## Signature
```
GETLASTERROR
GETLASTERROR()
```

## Parameters
無

## Returns
最近一次系統函式呼叫的錯誤碼（整數）。沒有錯誤時為 0。

## Description
傳回最近一次執行的系統函式呼叫所產生錯誤碼的函式。

此函式傳回的值也可以透過 [SETLASTERROR](SETLASTERROR.md) 設定。若要確實檢查可能發生錯誤的位置，請先使用 `SETLASTERROR(0)` 將值重設為 0，再呼叫系統函式，之後檢查 `GETLASTERROR`。

## Error Codes
| 代碼 | 意義 |
|--------|------|
| 0 | 沒有錯誤 |
| 8 | 引數不足 |
| 9 | 引數值不正確 |
| 10 | 無法處理空字串 |
| 11 | 沒有可儲存結果的變數 |
| 12 | 超出範圍或值不正確 |
| 13 | 處理失敗 |
| 14 | 尚未載入外部函式庫 |
| 15 | 檔案尚未開啟 |
| 16 | 正規表示式語法錯誤或過於複雜 |
| 17 | 正規表示式處理時發生未定義錯誤 |
| 18 | 預期為變數的位置收到非變數引數 |

## Example
```
SETLASTERROR(0)
// システム関数を呼び出す
if !GETLASTERROR {
    "エラーが発生しました。"
}
```

## Compatibility
- YAYA：自初期版本起可使用
- AYA：5.8 版以後

## See Also
- SETLASTERROR
