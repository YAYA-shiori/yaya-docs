# RE_SPLIT
**Category:** 正規表現

## Signature
```
RE_SPLIT( string , regexp [, max] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要拆分的字符串 |
| regexp | 用于拆分的正则表达式模式 |
| max | 最大拆分次数（省略或为 0 时全部拆分） |

## Returns
- 成功: 存放拆分后字符串的通用数组
- 失败: 空的通用数组

## Description
使用正则表达式模式拆分要处理的字符串，并以通用数组形式返回结果。

指定 `max` 时，会在达到该次数后停止拆分，并将剩余部分合并到最后一个元素中（`RE_SPLIT('a,b,c,d', ',', 2)` 会得到 `a` 和 `b,c,d`）。

可以通过 RE_GETSTR、RE_GETPOS、RE_GETLEN 获取拆分结果的详情。

## Compatibility
- YAYA: 初始版本起支持（max 参数从 Tc536-1 起支持）
- Tc606-6: 正则表达式引擎已更改为 uka_regexp（语法接近 PCRE2）。可以使用变量和函数解析模式中的子程序调用（[正则表达式](../grammar/14-regular-expressions.md)）

## See Also
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [正则表达式](../grammar/14-regular-expressions.md)
