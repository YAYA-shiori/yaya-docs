# ASIN

**Category:** 数学関数

## Signature

```
ASIN(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | The real number for which to calculate the arcsine. Must be in the range -1.0 ≤ val ≤ 1.0 |

## Returns

On success: The arcsine in radians (real number)
On failure: 0.0

## Description

Returns the arcsine in radians.

The return value is in radians. To convert it to degrees, calculate `radians * 180 / 3.14159265358`. The radian is a unit of angle; 180 degrees is π radians (π is approximately 3.14159265358).

## Example

```
_d = ASIN(0.5)           // 0.523599 (ラジアン) を返す
_d * 180 / 3.14159265358 // 度に変換：30.000000
```

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later

## See Also

- ACOS
- ATAN
- SIN
- COS
- TAN
- SINH
- COSH
- TANH
