# IHASH
**Category:** ハッシュ操作

## Signature
```
IHASH( [key1, value1, key2, value2, ...] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key*n* | Key |
| value*n* | The value corresponding to key*n* |

## Returns
A hash. If no arguments are specified, returns an empty hash.

## Description
Creates a hash by alternating keys and values.

- Generic arrays passed as arguments are expanded, just as they are for other functions. `IHASH("x", (1,2,3))` is equivalent to `IHASH("x",1,2,3)`, resulting in two elements: `x=1` and `2=3`. To put an array in a hash value, assign it to an element after creating the hash (`_h["x"] = (1,2,3)`)
- If a hash is passed as an argument, it is not expanded and is used as-is as a key or value (nested)
- If the number of arguments is odd, warning W0020 is issued, and the last key's value becomes VOID
- If two or more items are considered to have the same key, the first key and value are retained

See [Hash](../grammar/12-hash.md) for the rules for key matching and ordering.

## Example
```
_h = IHASH("name", "さくら", "age", 16)
_h["name"]              // "さくら"

_e = IHASH()            // 空のハッシュ
_e["k"] = (1, 2, 3)     // 値に配列を入れる

IHASH(9, "i9", "9", "s9")   // 9 と "9" は同じキーなので 9=i9 だけ
```

## Compatibility
- YAYA: Tc600-3以降

## See Also
- HASH_SPLIT
- HASH_KEYS
- HASH_VALUES
- HASH_EXIST
- HASH_SIZE
- IARRAY
