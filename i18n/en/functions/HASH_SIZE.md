# HASH_SIZE
**Category:** ハッシュ操作

## Signature
```
HASH_SIZE( hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| hash | hash |

## Returns
Number of elements (integer)

## Description
Returns the number of elements in the hash.

If the argument is not a hash, warning W0009 is issued.

## Example
```
_h = IHASH("a", 1, "b", 2)
HASH_SIZE(_h)   // 2
```

## Compatibility
- YAYA: Tc600-3 and later

## See Also
- ARRAYSIZE
- IHASH
