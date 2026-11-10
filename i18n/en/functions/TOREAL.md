# TOREAL
**Category:** 型取得/変換

## Signature
```
TOREAL( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String or integer to convert |

## Returns
- Success: Converted real number
- Failure: 0.0

## Description
Converts a string or integer to a real number (floating-point number).

## Example
```
_s = '1.00005'
_d = TOREAL( _s )
_d // 1.000050 (実数)

_i = 1
_d = TOREAL( _i )
_d // 1.000000 (実数)
```

## Compatibility
- YAYA: Since the initial version
- AYA: 5.8 and later

## See Also
- TOINT
- TOSTR
