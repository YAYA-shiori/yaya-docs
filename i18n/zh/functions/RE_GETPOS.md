# RE_GETPOS
**Category:** 正規表現

## Signature
```
RE_GETPOS
RE_GETPOS()
```

## Parameters
无

## Returns
列出正则表达式中与 `( )` 匹配位置的通用数组。

| 元素 | 内容 |
|------|------|
| 元素0 | 整个正则表达式模式匹配的位置 |
| 元素n | 第 n 个括号组匹配的位置 |

- 位置表示从开头起的字符数（从 0 开始）。
- 未执行正则表达式函数，或没有匹配字符串时，返回 `IARRAY`。
- 对于 `RE_REPLACE`、`RE_REPLACEEX`、`RE_SPLIT`，返回的是整个正则表达式的匹配位置，而非各个组的位置。

## Description
获取正则表达式相关函数的执行结果（匹配位置信息）。

## Compatibility
- YAYA：从初始版本起即可使用
- AYA：从 5.8 版起可使用

## See Also
- RE_GETSTR
- RE_GETLEN
- [正则表达式](../grammar/14-regular-expressions.md)
