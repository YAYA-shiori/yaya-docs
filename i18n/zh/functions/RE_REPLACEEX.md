# RE_REPLACEEX
**Category:** 正規表現

## Signature
```
RE_REPLACEEX( string , regexp , replace_ex [, count] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要处理的字符串（建议使用 TOSTR 将数值型变量转换为字符串类型） |
| regexp | 正则表达式模式 |
| replace_ex | 替换后的字符串（可以使用 `$0`、`$1` 等 Perl 风格的元字符） |
| count | 替换次数（省略或为负值时替换全部） |

## Returns
- 成功: 替换后的字符串
- 失败: 原 string（不变）

## Description
替换要处理的字符串中与正则表达式匹配的部分。与 RE_REPLACE 的区别在于，替换字符串中可以使用 `$0`、`$1` 等 Perl 风格的元字符。

使用 RE_REPLACEEX 时，RE_GETSTR、RE_GETPOS、RE_GETLEN 返回的是正则表达式模式整体第 n 个匹配的相关信息，而不是第 n 个分组的捕获信息。

## Compatibility
- YAYA: 初始版本起支持（count 参数从 Tc548-1 起支持）
- Tc606-6: 正则表达式引擎已更改为 uka_regexp（语法接近 PCRE2）。可以使用变量和函数解析模式中的子程序调用（[正则表达式](../grammar/14-regular-expressions.md)）

## See Also
- REPLACE
- RE_REPLACE
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [正则表达式](../grammar/14-regular-expressions.md)
