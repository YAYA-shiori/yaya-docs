# RE_GETLEN
**Category:** 正規表現

## Signature
```
RE_GETLEN
RE_GETLEN()
```

## Parameters
无

## Returns
列出正则表达式中与 `( )` 匹配部分长度的通用数组。

| 元素 | 内容 |
|------|------|
| 元素0 | 与整个正则表达式匹配部分的长度 |
| 元素n | 与第 n 个括号组匹配部分的长度 |

- 长度以字符数计量。
- 未执行正则表达式函数，或没有匹配字符串时，返回 `IARRAY`。
- 对于 `RE_REPLACE`、`RE_REPLACEEX`、`RE_SPLIT`，返回的是与整个正则表达式匹配部分的长度，而非各个组的长度。

## Description
获取正则表达式相关函数的执行结果。与 `RE_GETPOS`、`RE_GETSTR` 配合使用。

## Compatibility
- YAYA：从初始版本起即可使用
- AYA：从 5.8 版起可使用

## See Also
- RE_GETPOS
- RE_GETSTR
- [正则表达式](../grammar/14-regular-expressions.md)
