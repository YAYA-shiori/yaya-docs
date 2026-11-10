# ERASE

**Category:** 文字列操作

## Signature

```
ERASE( src, pos, len )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| src | The string to delete from |
| pos | The starting position for deletion (0 is the beginning). Negative values are treated as offsets from the end. |
| len | The number of characters to delete. If it exceeds the total number of characters in the string, an empty string is returned. |

## Returns

The string after deletion. Returns an empty string if the deletion length exceeds the entire string.

## Description

Deletes the specified portion of a string.

## Example

```
_str = 'さくらまゆらねここ'
ERASE( _str, 2, 6 ) // 「さくこ」を返す
```

## Compatibility

- YAYA: Supported from the first release
- AYA: 5.8 and later
- Tc539-3 and later: Negative values can be specified for pos

## See Also

- ERASEVAR
