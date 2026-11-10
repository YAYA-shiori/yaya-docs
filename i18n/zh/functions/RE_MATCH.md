# RE_MATCH
**Category:** 正規表現

## Signature
```
RE_MATCH( string , regexp )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要匹配的字符串 |
| regexp | 正则表达式模式 |

## Returns
- **1**：整个字符串与模式完全匹配时
- **0**：不匹配时

## Description
检查目标字符串是否与正则表达式完全匹配。要检查部分匹配，请使用 RE_SEARCH。

可以通过 RE_GETSTR、RE_GETPOS、RE_GETLEN 获取匹配详情。

## Example
```
RE_MATCH("50kg", "(\d+) *kg")
// → 1

RE_MATCH("50cm", "(\d+) *kg")
// → 0
```

## Compatibility
- YAYA：从初始版本起支持
- AYA：5.8 及更高版本
- Tc606-6：正则表达式引擎改为 uka_regexp（语法接近 PCRE2）。可以通过变量或函数解析模式中的子程序调用（[正则表达式](../grammar/14-regular-expressions.md)）

## See Also
- RE_SEARCH
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [正则表达式](../grammar/14-regular-expressions.md)
