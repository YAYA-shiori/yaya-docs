# HASH_EXIST
**Category:** ハッシュ操作

## Signature
```
HASH_EXIST( key, hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key | Key to check |
| hash | Hash |

## Returns
- 1: Key exists
- 0: Key does not exist

## Description
Returns whether a key exists in a hash. Note that the arguments are ordered **key, hash**, as with ASEARCH.

`h[key]` returns VOID if the key does not exist (an empty string through Tc602-13), but the value itself may also be VOID or an empty string. Use this function to check whether a key does not exist.

Key matching follows the [hash key rules](../grammar/12-hash.md#キーの一致). If `key` is an array or hash, warning W0009 is issued.

## Example
```
_h = IHASH("a", "", 1, "x")
HASH_EXIST("a", _h)   // 1
HASH_EXIST("b", _h)   // 0
HASH_EXIST("1", _h)   // 1 （1 と "1" は同じキー）
```

## Compatibility
- YAYA: Tc600-3 and later

## See Also
- HASH_KEYS
- HASH_SIZE
- IHASH
