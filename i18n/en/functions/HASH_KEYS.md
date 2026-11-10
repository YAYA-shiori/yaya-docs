# HASH_KEYS
**Category:** ハッシュ操作

## Signature
```
HASH_KEYS( hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| hash | Hash |

## Returns
Generic array of keys, sorted by key.

## Description
Returns the keys of a hash as a generic array. The keys are sorted by key, not by insertion order (numbers < strings).

A warning W0009 is issued if the argument is not a hash.

## Example
```
_h = IHASH("b", 1, "a", 2, 10, 3, 9, 4)
HASH_KEYS(_h)   // 9,10,a,b
```

## Compatibility
- YAYA: Tc600-3 and later

## See Also
- HASH_VALUES
- IHASH
