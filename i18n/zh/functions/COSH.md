# COSH

**Category:** 数学関数

## Signature

```
COSH(rad)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| rad | 以弧度为单位的角度值 |

## Returns

成功时：表示双曲余弦（双曲函数）值的实数
失败时：0.0

返回双曲余弦（双曲函数）值。参数的单位为弧度。

## Description

返回双曲余弦（双曲函数）值。参数的单位为弧度。

弧度是一种角度单位，180 度等于 π 弧度（π 约为 3.14159265358）。将角度转换为弧度时，计算 `角度 * 3.14159265358 / 180`（90 度约为 1.5708）。

## Example

```
_rad = 60 * 3.14159265358 / 180  // 60° をラジアンに変換
COSH(_rad)  // 約 1.600287 を返す
```

## Compatibility

- YAYA: TC522-1及之后

## See Also

- SIN
- COS
- TAN
- ASIN
- ACOS
- ATAN
- SINH
- TANH
