# STRSTR
**Category:** 文字列操作

## Signature
```
STRSTR(src, search, pos)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 搜尋目標字串 |
| search | 要搜尋的子字串 |
| pos | 搜尋起始位置（從 0 開始） |

## Returns
- 找到時：子字串起始位置的字元索引（從 0 開始）
- 找不到時：-1

## Description
在字串中搜尋子字串，並傳回找到位置的字元索引。

## Compatibility
- YAYA：從初始版本起即可使用
- AYA：5.8 以後

## See Also
- STRLEN（取得字串長度）
- SUBSTR（取得部分字串）
