# ASIN

**Category:** 数学関数

## Signature

```
ASIN(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | 要計算反正弦的實數值。範圍為 -1.0 ≤ val ≤ 1.0 |

## Returns

成功時：以弧度傳回反正弦值（實數）
失敗時：0.0

## Description

以弧度傳回反正弦值。

傳回值的單位是弧度。若要換算成度，請計算 `弧度 * 180 / 3.14159265358`。弧度是角度的單位之一，180 度相當於 π 弧度（π 約為 3.14159265358）。

## Example

```
_d = ASIN(0.5)           // 0.523599 (ラジアン) を返す
_d * 180 / 3.14159265358 // 度に変換：30.000000
```

## Compatibility

- YAYA：從初始版本起即可使用
- AYA：版本 5.8 以後

## See Also

- ACOS
- ATAN
- SIN
- COS
- TAN
- SINH
- COSH
- TANH
