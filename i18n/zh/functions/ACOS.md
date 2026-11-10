# ACOS

**Category:** 数学関数

## Signature

```
ACOS( val )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | 用于计算反余弦的实数值。范围为 -1.0 ≦ val ≦ 1.0 |

## Returns

成功时：以弧度返回反余弦值（实数）
失败时：0.0

## Description

以弧度返回反余弦值。

返回值的单位为弧度。要转换为角度，请计算 `弧度 * 180 / 3.14159265358`。弧度是角度单位之一，180 度相当于 π 弧度（π 约为 3.14159265358）。

## Example

```
_d = ACOS( 0.5 )    // 約 1.047198 (ラジアン) を返す
_d * 180 / 3.14159265358  // 約 60 度に変換
```

## Compatibility

- YAYA：从初始版本起可用
- AYA：5.8 及更高版本

## See Also

- ASIN
- ATAN
- SIN
- COS
- TAN
- SINH
- COSH
- TANH
