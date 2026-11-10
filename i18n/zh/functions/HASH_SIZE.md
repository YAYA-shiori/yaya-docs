# HASH_SIZE
**Category:** ハッシュ操作

## Signature
```
HASH_SIZE( hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| hash | 哈希 |

## Returns
元素数（整数）

## Description
返回哈希的元素数。

参数不是哈希时，会发出警告 W0009。

## Example
```
_h = IHASH("a", 1, "b", 2)
HASH_SIZE(_h)   // 2
```

## Compatibility
- YAYA: Tc600-3及之后

## See Also
- ARRAYSIZE
- IHASH
