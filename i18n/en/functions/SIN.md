# SIN
**Category:** 数学関数

## Signature
```
SIN( rad )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | Angle in radians (number) |

## Returns
- On success: Sine value (real number)
- On failure: 0.0

## Description
Returns the sine value. The argument is in radians.

A radian is a unit of angle; 180 degrees equals π radians (π is approximately 3.14159265358). To convert degrees to radians, calculate `degrees * 3.14159265358 / 180` (90 degrees is approximately 1.5708).

## Example
```
_rad = 30 * 3.14159265358 / 180  // 30度をラジアンに変換
SIN( _rad )  // → 0.500000
```

## Compatibility
- YAYA: Supported since the initial version
- AYA: 5.8 and later

## See Also
- COS
- TAN
- ASIN
- ACOS
- ATAN
- SINH
- COSH
- TANH
