# ISINTSTR
**Category:** 文字列操作

## Signature
```
ISINTSTR( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要验证能否作为整数解释的字符串 |

## Returns
- 1：字符串可以作为整数解释
- 0：字符串不能作为整数解释

## Description
验证指定字符串能否作为整数解释。此函数与 ISREALSTR 相对应，有助于区分整数和浮点数的字符串表示形式。

## Compatibility
- YAYA: 从初始版本起可用
- AYA: 5.8及之后

## See Also
- ISREALSTR
