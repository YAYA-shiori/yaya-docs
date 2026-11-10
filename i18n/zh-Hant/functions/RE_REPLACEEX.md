# RE_REPLACEEX
**Category:** 正規表現

## Signature
```
RE_REPLACEEX( string , regexp , replace_ex [, count] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要處理的字串（建議將數值型變數用 TOSTR 轉換成字串型別） |
| regexp | 正規表示式模式 |
| replace_ex | 取代後的字串（可使用 `$0`、`$1` 等 Perl 風格中繼字元） |
| count | 取代次數（省略或指定負值時會全部取代） |

## Returns
- 成功: 取代後的字串
- 失敗: 原 string（未變更）

## Description
取代要處理的字串中符合正規表示式的部分。與 RE_REPLACE 的差異在於，取代字串可以使用 `$0`、`$1` 等 Perl 風格中繼字元。

使用 RE_REPLACEEX 時，RE_GETSTR、RE_GETPOS、RE_GETLEN 傳回的是正規表示式模式整體第 n 個符合項目的資訊，而不是第 n 個群組的擷取資訊。

## Compatibility
- YAYA: 自初始版本起支援（count 參數自 Tc548-1 起支援）
- Tc606-6: 將正規表示式引擎變更為 uka_regexp（語法接近 PCRE2）。可透過變數或函式解析模式中的子程式呼叫（[正規表示式](../grammar/14-regular-expressions.md)）

## See Also
- REPLACE
- RE_REPLACE
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [正規表示式](../grammar/14-regular-expressions.md)
