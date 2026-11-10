# RE_GREP
**Category:** 正規表現

## Signature
```
RE_GREP( string , regexp )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 處理目標字串 |
| regexp | 要比對的正規表示式模式 |

## Returns
- 1 以上：符合部分的數量（有符合項目時）
- 0：沒有符合項目時

## Description
在目標字串中搜尋所有符合正規表示式的部分。可以使用 `RE_GETSTR`・`RE_GETPOS`・`RE_GETLEN` 取得詳細結果。

## Compatibility
- YAYA：從初始版本起即可使用
- AYA：5.8 版及之後的版本即可使用
- Tc606-6：正規表示式引擎改為 uka_regexp（語法近似 PCRE2）。可以透過變數或函式解析模式中的子程序呼叫（[正規表示式](../grammar/14-regular-expressions.md)）

## See Also
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [正規表示式](../grammar/14-regular-expressions.md)
