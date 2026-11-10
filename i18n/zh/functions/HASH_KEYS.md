# HASH_KEYS
**Category:** ハッシュ操作

## Signature
```
HASH_KEYS( hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| hash | 哈希 |

## Returns
返回由键组成的通用数组。按键的顺序排列。

## Description
以通用数组形式返回哈希的键。排列顺序不是插入顺序，而是键的顺序（数值 < 字符串）。

参数不是哈希时，会发出警告 W0009。

## Example
```
_h = IHASH("b", 1, "a", 2, 10, 3, 9, 4)
HASH_KEYS(_h)   // 9,10,a,b
```

## Compatibility
- YAYA：Tc600-3 及之后

## See Also
- HASH_VALUES
- IHASH
