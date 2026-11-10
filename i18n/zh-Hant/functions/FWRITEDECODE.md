# FWRITEDECODE
**Category:** ファイル操作

## Signature
```
FWRITEDECODE( path, string [, type] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 以 FOPEN 指定的檔名 |
| string | 要寫入的已編碼字串 |
| type | 解碼方式：`"base64"`、`"url"`、`"form"` 其中之一（省略時為 base64。詳情請參閱 [STRDECODE](STRDECODE.md)）。Tc554-1 因實作錯誤而無法省略 |

## Returns
無

## Description
將資料解碼後寫入的函式，可解碼 base64 或 URL 編碼。此函式執行與 FREADENCODE 相反的操作。

必須事先以 FOPEN 開啟檔案。若 FOPEN 未以二進位存取模式開啟，則會進行換行碼轉換。即使解碼結果包含位元組值 0（0x00），也能正常寫入。

## Compatibility
- YAYA：Tc554-1 以後
- Tc554-1 因實作錯誤而無法省略 `type`

## See Also
- FWRITE
- FREADENCODE
- STRDECODE
