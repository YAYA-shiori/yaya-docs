# SINH
**Category:** 数学関数

## Signature
```
SINH(rad)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | Angle value in radians |

## Returns
- On success: Hyperbolic sine (real number)
- On failure: 0.0

## Description
Calculates and returns the hyperbolic sine. The argument is in radians.

A radian is a unit of angle; 180 degrees equals π radians (π is approximately 3.14159265358). To convert degrees to radians, calculate `degrees * 3.14159265358 / 180` (90 degrees is approximately 1.5708).

## Example
```
_rad = 30 * 3.14159265358 / 180  // 30°をラジアンに変換
SINH(_rad)                        // 約 0.547853 を返す
```

## Compatibility
- YAYA: Tc522-1 and later

## See Also
- SIN, COS, TAN (trigonometric functions)
- ASIN, ACOS, ATAN (inverse trigonometric functions)
- COSH, TANH (hyperbolic functions)
