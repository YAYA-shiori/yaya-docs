# RE_GETPOS
**Category:** 正規表現

## Signature
```
RE_GETPOS
RE_GETPOS()
```

## Parameters
無

## Returns
列出正規表示式中符合 `( )` 的位置的通用陣列。

| 項目 | 內容 |
|------|------|
| 項目0 | 符合整個正規表示式模式的位置 |
| 項目n | 符合第 n 個括號群組的位置 |

- 位置以從開頭起算的字元數表示（從 0 開始）。
- 尚未執行正規表示式函式，或沒有符合的字串時，會傳回 `IARRAY`。
- 對於 `RE_REPLACE`・`RE_REPLACEEX`・`RE_SPLIT`，傳回的是符合整個正規表示式的位置，而不是個別群組的位置。

## Description
取得正規表示式相關函式的執行結果（符合位置資訊）。

## Compatibility
- YAYA：從初始版本起即可使用
- AYA：5.8 版及之後的版本即可使用

## See Also
- RE_GETSTR
- RE_GETLEN
- [正規表示式](../grammar/14-regular-expressions.md)
