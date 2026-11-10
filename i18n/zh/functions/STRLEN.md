# STRLEN
**Category:** 文字列操作

## Signature
```
STRLEN(string)
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| string | 要获取字符数的字符串 |

## Returns
- 成功时：字符数（整数）
- 失败时：0

## Description
返回字符串的字符数。返回的是字符数而非字节数，因此汉字等多字节字符也按 1 个字符计数。

## Compatibility
- YAYA：从初始版本起可用
- AYA：5.8 及之后

## See Also
- STRSTR（子字符串搜索）
- SUBSTR（获取子字符串）
- GETSTRBYTES（获取字节数）
