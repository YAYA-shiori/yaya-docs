# HASH_SPLIT
**Category:** ハッシュ操作

## Signature
```
HASH_SPLIT( str, sep1, sep2 )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | 要分割的字符串 |
| sep1 | 元素分隔符 |
| sep2 | 键和值的分隔符 |

## Returns
哈希

## Description
使用 `sep1` 将字符串拆分为多个元素，再使用 `sep2` 将各元素拆分为键和值，从而创建哈希。

- 跳过空元素
- 不含 `sep2` 的元素会成为只有键的元素（值为 VOID）
- 丢弃键为空的元素（例如 `=x`）
- 在第一个 `sep2` 处分割。`d=4=5` 会得到键 `d`、值 `4=5`
- 当 `sep1` 或 `sep2` 是空字符串时，会发出警告 W0010 并返回空哈希

## Example
```
_h = HASH_SPLIT("a=1,b=2,,c,=x,d=4=5", ",", "=")
// a=1,b=2,c=,d=4=5 （要素数 4）
```

## Compatibility
- YAYA: Tc600-3及之后

## See Also
- IHASH
- SPLIT
