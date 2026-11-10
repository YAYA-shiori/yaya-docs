# TOAUTO
**Category:** 型取得/変換

## Signature
```
TOAUTO( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String to convert |

## Returns
- If it can be interpreted as an integer: the integer value
- If it can be interpreted as a real number (if integer conversion fails): the real value
- If it can be interpreted as neither: returns the original string unchanged

## Description
Attempts automatic type conversion of a string. It first tries to convert the string to an integer, then tries to convert it to a real number if that fails. If both conversions fail, it returns the original string unchanged.

Behavior is undefined if a generic array is passed as an argument.

## Compatibility
- YAYA: TC516-901 and later

## See Also
- TOINT
- TOREAL
- TOSTR
- TOAUTOEX
- CVAUTO
