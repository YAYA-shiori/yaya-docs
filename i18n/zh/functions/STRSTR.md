# STRSTR
**Category:** 文字列操作

## Signature
```
STRSTR(src, search, pos)
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| src | 搜索目标字符串 |
| search | 要搜索的子字符串 |
| pos | 搜索起始位置（从 0 开始） |

## Returns
- 找到时：子字符串起始字符的位置（从 0 开始）
- 未找到时：-1

## Description
搜索字符串中的子字符串，并返回找到的字符位置。

## Compatibility
- YAYA: 从初始版本起可用
- AYA: 5.8 及以上

## See Also
- STRLEN（获取字符串长度）
- SUBSTR（获取子字符串）
