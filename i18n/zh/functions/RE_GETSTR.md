# RE_GETSTR
**Category:** 正規表現

## Signature
```
RE_GETSTR
RE_GETSTR()
```

## Parameters
无

## Returns
存放匹配子字符串的通用数组。

| 元素 | 内容 |
|------|------|
| 元素0 | 与整个正则表达式匹配的字符串 |
| 元素n | 与第 n 个括号组匹配的子字符串 |

- 未执行正则表达式函数或没有匹配字符串时，返回 `IARRAY`。
- 对于 `RE_REPLACE`、`RE_REPLACEEX`、`RE_SPLIT`，返回存放与整个正则表达式匹配字符串的数组，而非各个组的字符串。

## Description
获取正则表达式相关函数的执行结果。

## Example
```
RE_MATCH("x > 15.7", "x *> *([\d\.]+)")
_array = RE_GETSTR
// _array は ("x > 15.7", "15.7") になる
```

## Compatibility
- YAYA：从初始版本起即可使用
- AYA：从 5.8 版起可使用

## See Also
- RE_GETPOS
- RE_GETLEN
- [正则表达式](../grammar/14-regular-expressions.md)
