# CVAUTO

**Category:** 型取得/変換

## Signature

```
CVAUTO(var [, strict_convert])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | The variable to convert |
| strict_convert | (Optional, default: 0) If a nonzero value is specified, conversion is performed only if converting the result back to a string produces the original string (same behavior as [CVAUTOEX](CVAUTOEX.md); Tc571-2 and later) |

## Returns

No return value (converts the variable in place)

When you specify a variable containing a string in string form, the value is converted and stored again as an integer if it can be interpreted as one, or as a real number if it can be interpreted as one. If it cannot be interpreted as either, it remains a string. Behavior is undefined if a generic array variable is passed.

## Example

```
_val = '3.14159'
CVAUTO(_val)
GETTYPE(_val) // 2 を返す（実数型であることを示す）
```

## Compatibility

- YAYA: Tc516-901 and later
- Tc571-2: Added `strict_convert`

## See Also

- CVREAL
- CVINT
- CVSTR
- CVAUTOEX
- TOAUTO
