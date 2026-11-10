# ATAN

**Category:** 数学関数

## Signature

```
ATAN(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | 用于求反正切的实数值 |

## Returns

成功时：以弧度返回反正切值（实数）
失败时：0.0

## Description

以弧度返回反正切值。

返回值的单位是弧度。要换算为度，可计算 `ラジアン * 180 / 3.14159265358`。弧度是一种角度单位，180 度相当于 π 弧度（π 约为 3.14159265358）。

## Example

```
_d = ATAN(1.0)               // 約 0.785398 ラジアンを返す
_d * 180 / 3.14159265358     // 約 45 度に変換
```

## Compatibility

- YAYA：从初始版本起可用
- AYA：版本 5.8 及以上

## See Also

- ASIN
- ACOS
- SIN
- COS
- TAN
- SINH
- COSH
- TANH
