# ATAN

**Category:** 数学関数

## Signature

```
ATAN(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | The real number for which to calculate the arctangent |

## Returns

On success: Returns the arctangent value in radians (real number)
On failure: 0.0

## Description

Returns the arctangent in radians.

The return value is in radians. To convert it to degrees, calculate `radians * 180 / 3.14159265358`. A radian is a unit of angle; 180 degrees equals π radians (π is approximately 3.14159265358).

## Example

```
_d = ATAN(1.0)               // 約 0.785398 ラジアンを返す
_d * 180 / 3.14159265358     // 約 45 度に変換
```

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later

## See Also

- ASIN
- ACOS
- SIN
- COS
- TAN
- SINH
- COSH
- TANH
