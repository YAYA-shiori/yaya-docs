# RE_REPLACE
**Category:** 正規表現

## Signature
```
RE_REPLACE( string , regexp , replace [, count] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要处理的字符串（建议使用 TOSTR 将数值型变量转换为字符串类型） |
| regexp | 正则表达式模式 |
| replace | 替换后的字符串（不能使用元字符） |
| count | 替换次数（省略或为负值时替换全部） |

## Returns
- 成功: 替换后的字符串
- 未匹配: 原字符串（不变）

## Description
替换要处理的字符串中与正则表达式匹配的部分。替换字符串中不能使用元字符。若要使用元字符，请使用 RE_REPLACEEX。

可以通过 RE_GETSTR、RE_GETPOS、RE_GETLEN 获取匹配详情。

## Compatibility
- YAYA: 初始版本起支持（count 参数从 Tc548-1 起支持）
- AYA: 5.8 及以上版本
- Tc606-6: 正则表达式引擎已更改为 uka_regexp（语法接近 PCRE2）。可以使用变量和函数解析模式中的子程序调用（[正则表达式](../grammar/14-regular-expressions.md)）

## See Also
- REPLACE
- RE_REPLACEEX
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [正则表达式](../grammar/14-regular-expressions.md)
