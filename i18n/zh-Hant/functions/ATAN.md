# ATAN

**Category:** 数学関数

## Signature

```
ATAN(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | 要計算反正切的實數值 |

## Returns

成功時：以弧度傳回反正切值（實數）
失敗時：0.0

## Description

以弧度傳回反正切值。

傳回值的單位是弧度。若要換算成度，請計算 `弧度 * 180 / 3.14159265358`。弧度是角度的單位之一，180 度相當於 π 弧度（π 約為 3.14159265358）。

## Example

```
_d = ATAN(1.0)               // 約 0.785398 ラジアンを返す
_d * 180 / 3.14159265358     // 約 45 度に変換
```

## Compatibility

- YAYA：從初始版本起即可使用
- AYA：版本 5.8 以後

## See Also

- ASIN
- ACOS
- SIN
- COS
- TAN
- SINH
- COSH
- TANH
