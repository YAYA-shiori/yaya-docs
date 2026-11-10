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
最近一次系統函式呼叫的錯誤代碼（整數）。若沒有錯誤則為 0。

## Description
傳回最近一次執行的系統函式呼叫之錯誤代碼。

## Error Codes
| 代碼 | 意義 |
|--------|------|
| 0 | 沒有錯誤 |
| 8 | 引數不足 |
| 9 | 引數值無效 |
| 10 | 無法處理空字串 |
| 11 | 沒有可儲存結果的變數 |
| 12 | 超出範圍或值無效 |
| 13 | 處理失敗 |
| 14 | 尚未載入外部函式庫 |
| 15 | 檔案尚未開啟 |
| 16 | 正規表示式語法錯誤或過於複雜 |
| 17 | 正規表示式處理期間發生未定義錯誤 |
| 18 | 需要變數的位置傳入了非變數的引數 |

## Example
```
SETLASTERROR(0)
// システム関数を呼び出す
if !GETLASTERROR {
    "エラーが発生しました。"
}
```

## Compatibility
- YAYA：從初期版本起即可使用
- AYA：5.8 版以後

## See Also
- SETLASTERROR
