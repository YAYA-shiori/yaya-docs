# RE_MATCH
**Category:** 正規表現

## Signature
```
RE_MATCH( string , regexp )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要比對的字串 |
| regexp | 正規表示式模式 |

## Returns
- **1**：整個字串完全符合模式時
- **0**：沒有符合項目時

## Description
檢查處理目標字串是否完全符合正規表示式。若要檢查部分符合，請使用 RE_SEARCH。

可以透過 RE_GETSTR、RE_GETPOS、RE_GETLEN 取得符合項目的詳細資訊。

## Example
```
RE_MATCH("50kg", "(\d+) *kg")
// → 1

RE_MATCH("50cm", "(\d+) *kg")
// → 0
```

## Compatibility
- YAYA：從初始版本起支援
- AYA：5.8 版及之後的版本
- Tc606-6：正規表示式引擎改為 uka_regexp（語法近似 PCRE2）。可以透過變數或函式解析模式中的子程序呼叫（[正規表示式](../grammar/14-regular-expressions.md)）

## See Also
- RE_SEARCH
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [正規表示式](../grammar/14-regular-expressions.md)
