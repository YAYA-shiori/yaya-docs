# RE_REPLACE
**Category:** 正規表現

## Signature
```
RE_REPLACE( string , regexp , replace [, count] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要處理的字串（建議將數值型變數用 TOSTR 轉換成字串型別） |
| regexp | 正規表示式模式 |
| replace | 取代後的字串（不可使用中繼字元） |
| count | 取代次數（省略或指定負值時會全部取代） |

## Returns
- 成功: 取代後的字串
- 沒有符合項目: 原字串（未變更）

## Description
取代要處理的字串中符合正規表示式的部分。取代字串不可使用中繼字元。若要使用中繼字元，請使用 RE_REPLACEEX。

可使用 RE_GETSTR、RE_GETPOS、RE_GETLEN 取得符合項目的詳細資訊。

## Compatibility
- YAYA: 自初始版本起支援（count 參數自 Tc548-1 起支援）
- AYA: 5.8 以後
- Tc606-6: 將正規表示式引擎變更為 uka_regexp（語法接近 PCRE2）。可透過變數或函式解析模式中的子程式呼叫（[正規表示式](../grammar/14-regular-expressions.md)）

## See Also
- REPLACE
- RE_REPLACEEX
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [正規表示式](../grammar/14-regular-expressions.md)
