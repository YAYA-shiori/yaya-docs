# ACOS

**Category:** 数学関数

## Signature

```
ACOS( val )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | 用來計算反餘弦的實數值。範圍為 -1.0 ≦ val ≦ 1.0 |

## Returns

成功時：以弧度傳回反餘弦值（實數）
失敗時：0.0

## Description

以弧度傳回反餘弦值。

傳回值的單位是弧度。若要轉換為度，請計算 `ラジアン * 180 / 3.14159265358`。弧度是角度的單位之一，180 度相當於 π 弧度（π 約為 3.14159265358）。

## Example

```
_d = ACOS( 0.5 )    // 約 1.047198 (ラジアン) を返す
_d * 180 / 3.14159265358  // 約 60 度に変換
```

## Compatibility

- YAYA: 從初始版本起即可使用
- AYA: 5.8 版以後

## See Also

- ASIN
- ATAN
- SIN
- COS
- TAN
- SINH
- COSH
- TANH
