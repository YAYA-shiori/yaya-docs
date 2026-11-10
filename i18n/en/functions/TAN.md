# TAN
**Category:** 数学関数

## Signature
```
TAN(rad)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | Angle value in radians |

## Returns
- On success: the tangent value (real number)
- On failure: 0.0

## Description
Returns the tangent. The argument is in radians.

A radian is a unit of angle, and 180 degrees is π radians (π is approximately 3.14159265358). To convert degrees to radians, calculate `degrees * 3.14159265358 / 180` (90 degrees is approximately 1.5708).

## Example
```
_rad = 45 * 3.14159265358 / 180  // 45°をラジアンに変換
TAN(_rad)  // 約 1.000000 を返す
```

## Compatibility
- YAYA: Available since the initial version
- AYA: 5.8 and later

## See Also
- SIN, COS (trigonometric functions)
- ASIN, ACOS, ATAN (inverse trigonometric functions)
- SINH, COSH, TANH (hyperbolic functions)
