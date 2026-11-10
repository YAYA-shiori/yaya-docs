# ASIN

**Category:** 数学関数

## Signature

```
ASIN(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | 用于计算反正弦的实数值。范围为 -1.0 ≤ val ≤ 1.0 |

## Returns

成功时：以弧度返回反正弦值（实数）
失败时：0.0

## Description

以弧度返回反正弦值。

返回值的单位是弧度。要换算为度，可计算 `ラジアン * 180 / 3.14159265358`。弧度是一种角度单位，180 度相当于 π 弧度（π 约为 3.14159265358）。

## Example

```
_d = ASIN(0.5)           // 0.523599 (ラジアン) を返す
_d * 180 / 3.14159265358 // 度に変換：30.000000
```

## Compatibility

- YAYA：从初始版本起可用
- AYA：版本 5.8 及以上

## See Also

- ACOS
- ATAN
- SIN
- COS
- TAN
- SINH
- COSH
- TANH
