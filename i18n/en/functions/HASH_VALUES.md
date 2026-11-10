# HASH_VALUES
**Category:** ハッシュ操作

## Signature
```
HASH_VALUES( hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| hash | hash |

## Returns
Generic array of values, ordered by key.

## Description
Returns the hash values as a generic array. The order is the same as the key order in [HASH_KEYS](HASH_KEYS.md).

If a value is an array, it is included as a single element (as a nested array). Therefore, the number of elements in the return value is the same as the number of elements in the hash.

If the argument is not a hash, warning W0009 is issued.

## Example
```
_h = IHASH("a", 1)
_h["b"] = (1, 2)
_v = HASH_VALUES(_h)
ARRAYSIZE(_v)   // 2
_v[1]           // 配列 (1,2)
TOSTR(_v)       // "1,1,2"
```

## Compatibility
- YAYA: Tc600-3 and later

## See Also
- HASH_KEYS
- IHASH
- [Nested Values and Multidimensional Assignment](../grammar/13-nesting.md)
