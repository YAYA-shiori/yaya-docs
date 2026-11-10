# RE_GETSTR
**Category:** 正規表現

## Signature
```
RE_GETSTR
RE_GETSTR()
```

## Parameters
無

## Returns
存放符合部分字串的通用陣列。

| 項目 | 內容 |
|------|------|
| 項目0 | 符合整個正規表示式的字串 |
| 項目n | 符合第 n 個括號群組的部分字串 |

- 尚未執行正規表示式函式，或沒有符合的字串時，會傳回 `IARRAY`。
- 對於 `RE_REPLACE`・`RE_REPLACEEX`・`RE_SPLIT`，會傳回存放符合整個正規表示式的字串的陣列，而不是個別群組的字串。

## Description
取得正規表示式相關函式的執行結果。

## Example
```
RE_MATCH("x > 15.7", "x *> *([\d\.]+)")
_array = RE_GETSTR
// _array は ("x > 15.7", "15.7") になる
```

## Compatibility
- YAYA：從初始版本起即可使用
- AYA：5.8 版起即可使用

## See Also
- RE_GETPOS
- RE_GETLEN
- [正規表示式](../grammar/14-regular-expressions.md)
