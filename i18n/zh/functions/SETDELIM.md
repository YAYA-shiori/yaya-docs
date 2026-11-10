# SETDELIM
**Category:** 配列操作

## Signature
```
SETDELIM( array , delim )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| array | 要设置分隔符的简易数组变量 |
| delim | 要设置的分隔符字符串 |

## Returns
无

## Description
设置变量的默认分隔符（简易数组的分隔符）。默认分隔符为逗号（,）。

**注意：**两个参数都必须直接指定给函数。以下用法无法正常工作：

```
// 不正な使い方（動作しない）
_i = (var, "/")
SETDELIM(_i)
```

```
// 正しい使い方
SETDELIM(var, "/")
```

## Compatibility
- YAYA：从初始版本起支持
- AYA：5.8 及之后

## See Also
- GETDELIM
