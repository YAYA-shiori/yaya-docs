# RE_GETLEN
**Category:** 正規表現

## Signature
```
RE_GETLEN
RE_GETLEN()
```

## Parameters
無

## Returns
列出正規表示式中符合 `( )` 的部分長度的通用陣列。

| 項目 | 內容 |
|------|------|
| 項目0 | 符合整個正規表示式的部分長度 |
| 項目n | 符合第 n 個括號群組的部分長度 |

- 長度以字元數計算。
- 尚未執行正規表示式函式，或沒有符合的字串時，會傳回 `IARRAY`。
- 對於 `RE_REPLACE`・`RE_REPLACEEX`・`RE_SPLIT`，傳回的是符合整個正規表示式的部分長度，而不是個別群組的長度。

## Description
取得正規表示式相關函式的執行結果。請與 `RE_GETPOS`・`RE_GETSTR` 搭配使用。

## Compatibility
- YAYA：從初始版本起即可使用
- AYA：5.8 版及之後的版本即可使用

## See Also
- RE_GETPOS
- RE_GETSTR
- [正規表示式](../grammar/14-regular-expressions.md)
