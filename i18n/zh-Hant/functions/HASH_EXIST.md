# HASH_EXIST
**Category:** ハッシュ操作

## Signature
```
HASH_EXIST( key, hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key | 要檢查的鍵 |
| hash | 雜湊 |

## Returns
- 1：有此鍵
- 0：沒有此鍵

## Description
傳回雜湊中是否有指定的鍵。請注意，引數順序是**鍵、雜湊**（與 ASEARCH 相同）。

`h[鍵]` 在鍵不存在時會傳回 VOID（Tc602-13 以前會傳回空字串），但值本身也可能是 VOID 或空字串，因此要確認「鍵不存在」時，請使用此函式。

鍵的比對依照[雜湊鍵的規則](../grammar/12-hash.md#キーの一致)。當 `key` 是陣列或雜湊時，會發出警告 W0009。

## Example
```
_h = IHASH("a", "", 1, "x")
HASH_EXIST("a", _h)   // 1
HASH_EXIST("b", _h)   // 0
HASH_EXIST("1", _h)   // 1 （1 と "1" は同じキー）
```

## Compatibility
- YAYA：Tc600-3 以後

## See Also
- HASH_KEYS
- HASH_SIZE
- IHASH
