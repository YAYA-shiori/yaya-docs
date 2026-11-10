# ERASE

**Category:** 文字列操作

## Signature

```
ERASE( src, pos, len )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| src | 要删除的字符串 |
| pos | 删除起始位置（0 表示开头）。指定负值时，将其视为从末尾开始的偏移量。 |
| len | 要删除的字符数。超过字符串总字符数时，返回空字符串。 |

## Returns

删除后的字符串。删除长度超过整个字符串时，返回空字符串。

## Description

删除字符串中指定的部分。

## Example

```
_str = 'さくらまゆらねここ'
ERASE( _str, 2, 6 ) // 「さくこ」を返す
```

## Compatibility

- YAYA: 从初版开始支持
- AYA: 5.8 及以后版本
- Tc539-3 及以后版本: 可以为 pos 指定负值

## See Also

- ERASEVAR
