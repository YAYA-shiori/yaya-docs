# COSH

**Category:** 数学関数

## Signature

```
COSH(rad)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| rad | 以弧度為單位的角度值 |

## Returns

成功時：表示雙曲餘弦（雙曲線函式）值的實數
失敗時：0.0

傳回雙曲餘弦（雙曲線函式）值。引數的單位為弧度。

## Description

傳回雙曲餘弦（雙曲線函式）值。引數的單位為弧度。

弧度是角度的單位之一，180 度等於 π 弧度（π 約為 3.14159265358）。將角度從度轉換為弧度時，請計算 `度 * 3.14159265358 / 180`（90 度約為 1.5708）。

## Example

```
_rad = 60 * 3.14159265358 / 180  // 60° をラジアンに変換
COSH(_rad)  // 約 1.600287 を返す
```

## Compatibility

- YAYA: TC522-1 以後

## See Also

- SIN
- COS
- TAN
- ASIN
- ACOS
- ATAN
- SINH
- TANH
