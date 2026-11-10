# STRLEN
**Category:** 文字列操作

## Signature
```
STRLEN(string)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要取得字元數的字串 |

## Returns
- 成功時：字元數（整數）
- 失敗時：0

## Description
傳回字串的字元數。傳回的是字元數而非位元組數，因此漢字等多位元組字元也會計為 1 個字元。

## Compatibility
- YAYA：自初期版本起即可使用
- AYA：5.8 之後

## See Also
- STRSTR（搜尋子字串）
- SUBSTR（取得子字串）
- GETSTRBYTES（取得位元組數）
