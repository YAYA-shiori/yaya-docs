# TANH
**Category:** 数学関数

## Signature
```
TANH(rad)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | Angle value in radians |

## Returns
- On success: the hyperbolic tangent (real number)
- On failure: 0.0

## Description
Returns the hyperbolic tangent (a hyperbolic function). The argument is in radians.

A radian is a unit of angle, and 180 degrees is π radians (π is approximately 3.14159265358). To convert degrees to radians, calculate `degrees * 3.14159265358 / 180` (90 degrees is approximately 1.5708).

## Example
```
_rad = 45 * 3.14159265358 / 180  // 45°をラジアンに変換
TANH(_rad)  // 約 0.655794 を返す
```

## Compatibility
- YAYA: Available from Tc522-1 onward

## See Also
- SIN, COS, TAN (trigonometric functions)
- ASIN, ACOS, ATAN (inverse trigonometric functions)
- SINH, COSH (hyperbolic functions)
