# HASH_SIZE
**Category:** ハッシュ操作

## Signature
```
HASH_SIZE( hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| hash | 雜湊 |

## Returns
元素數量（整數）

## Description
傳回雜湊的元素數量。

引數不是雜湊時，會發出警告 W0009。

## Example
```
_h = IHASH("a", 1, "b", 2)
HASH_SIZE(_h)   // 2
```

## Compatibility
- YAYA: Tc600-3 以後

## See Also
- ARRAYSIZE
- IHASH
