# HASH_EXIST
**Category:** ハッシュ操作

## Signature
```
HASH_EXIST( key, hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key | 要检查的键 |
| hash | 哈希 |

## Returns
- 1：存在该键
- 0：不存在该键

## Description
返回哈希中是否存在指定键。请注意，参数顺序为**键、哈希**（与 ASEARCH 相同）。

`h[键]` 在键不存在时会返回 VOID（Tc602-13 之前返回空字符串），但值本身也可能是 VOID 或空字符串，因此要确认“键不存在”时应使用本函数。

键的匹配遵循[哈希键的规则](../grammar/12-hash.md#キーの一致)。`key` 为数组或哈希时，会发出警告 W0009。

## Example
```
_h = IHASH("a", "", 1, "x")
HASH_EXIST("a", _h)   // 1
HASH_EXIST("b", _h)   // 0
HASH_EXIST("1", _h)   // 1 （1 と "1" は同じキー）
```

## Compatibility
- YAYA：Tc600-3 及之后

## See Also
- HASH_KEYS
- HASH_SIZE
- IHASH
