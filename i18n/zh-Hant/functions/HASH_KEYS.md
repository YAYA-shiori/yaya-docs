# HASH_KEYS
**Category:** ハッシュ操作

## Signature
```
HASH_KEYS( hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| hash | 雜湊 |

## Returns
傳回鍵組成的通用陣列。依鍵的順序排列。

## Description
以通用陣列傳回雜湊的鍵。排列順序不是插入順序，而是鍵的排序順序（數值 < 字串）。

引數不是雜湊時，會發出警告 W0009。

## Example
```
_h = IHASH("b", 1, "a", 2, 10, 3, 9, 4)
HASH_KEYS(_h)   // 9,10,a,b
```

## Compatibility
- YAYA：Tc600-3 以後

## See Also
- HASH_VALUES
- IHASH
