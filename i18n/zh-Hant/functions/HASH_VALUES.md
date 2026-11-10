# HASH_VALUES
**Category:** ハッシュ操作

## Signature
```
HASH_VALUES( hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| hash | 雜湊 |

## Returns
通用陣列，包含各個值，並依鍵的順序排列。

## Description
以通用陣列傳回雜湊中的值。排列順序與 [HASH_KEYS](HASH_KEYS.md) 相同，皆依鍵的順序排列。

值為陣列時，會將該陣列作為一個元素包含在內（因此會形成巢狀陣列）。因此，傳回值的元素數量會與雜湊的元素數量相同。

引數不是雜湊時，會發出警告 W0009。

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
- YAYA: Tc600-3 以後

## See Also
- HASH_KEYS
- IHASH
- [巢狀值與多維指派](../grammar/13-nesting.md)
