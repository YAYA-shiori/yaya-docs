# COS

**Category:** 数学関数

## Signature

```
COS(rad)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| rad | Angle in radians |

## Returns

On success: A real number representing the cosine
On failure: 0.0

## Description

Returns the cosine. The argument is in radians.

A radian is a unit of angle, and 180 degrees is π radians (π is approximately 3.14159265358). To convert degrees to radians, calculate `degrees * 3.14159265358 / 180` (90 degrees is approximately 1.5708).

## Example

```
_rad = 60 * 3.14159265358 / 180  // 60° をラジアンに変換
COS(_rad)  // 0.500000 を返す
```

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later

## See Also

- SIN
- TAN
- ASIN
- ACOS
- ATAN
- SINH
- COSH
- TANH
