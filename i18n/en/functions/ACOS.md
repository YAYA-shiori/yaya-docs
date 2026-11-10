# ACOS

**Category:** 数学関数

## Signature

```
ACOS( val )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | The real number for which to calculate the arccosine. Must be in the range -1.0 ≦ val ≦ 1.0 |

## Returns

On success: The arccosine in radians (real number)
On failure: 0.0

## Description

Returns the arccosine in radians.

The return value is in radians. To convert it to degrees, calculate `radians * 180 / 3.14159265358`. The radian is a unit of angle; 180 degrees is π radians (π is approximately 3.14159265358).

## Example

```
_d = ACOS( 0.5 )    // 約 1.047198 (ラジアン) を返す
_d * 180 / 3.14159265358  // 約 60 度に変換
```

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later

## See Also

- ASIN
- ATAN
- SIN
- COS
- TAN
- SINH
- COSH
- TANH
