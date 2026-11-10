# COSH

**Category:** 数学関数

## Signature

```
COSH(rad)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| rad | Angle value in radians |

## Returns

On success: A real number representing the hyperbolic cosine
On failure: 0.0

Returns the hyperbolic cosine. The argument is in radians.

## Description

Returns the hyperbolic cosine. The argument is in radians.

A radian is a unit of angle; 180 degrees equals π radians (π is approximately 3.14159265358). To convert degrees to radians, calculate `度 * 3.14159265358 / 180` (90 degrees is approximately 1.5708).

## Example

```
_rad = 60 * 3.14159265358 / 180  // 60° をラジアンに変換
COSH(_rad)  // 約 1.600287 を返す
```

## Compatibility

- YAYA: Tc522-1 and later

## See Also

- SIN
- COS
- TAN
- ASIN
- ACOS
- ATAN
- SINH
- TANH
