# RE_GREP
**Category:** 正規表現

## Signature
```
RE_GREP( string , regexp )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要处理的字符串 |
| regexp | 用于匹配的正则表达式模式 |

## Returns
- 1 以上：匹配部分的数量（有匹配项时）
- 0：没有匹配部分时

## Description
在目标字符串中搜索所有与正则表达式匹配的部分。可以使用 `RE_GETSTR`、`RE_GETPOS`、`RE_GETLEN` 获取详细结果。

## Compatibility
- YAYA：从初始版本起即可使用
- AYA：从 5.8 版起可使用
- Tc606-6：正则表达式引擎改为 uka_regexp（语法接近 PCRE2）。可以通过变量或函数解析模式中的子程序调用（[正则表达式](../grammar/14-regular-expressions.md)）

## See Also
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [正则表达式](../grammar/14-regular-expressions.md)
