# COS

**Category:** 数学関数

## Signature

```
COS(rad)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| rad | 以弧度為單位的角度 |

## Returns

成功時：表示餘弦值的實數
失敗時：0.0

## Description

傳回餘弦值。引數的單位為弧度。

弧度是角度的單位之一，180 度等於 π 弧度（π 約為 3.14159265358）。將角度從度轉換為弧度時，請計算 `度 * 3.14159265358 / 180`（90 度約為 1.5708）。

## Example

```
_rad = 60 * 3.14159265358 / 180  // 60° をラジアンに変換
COS(_rad)  // 0.500000 を返す
```

## Compatibility

- YAYA: 初版起即可使用
- AYA: 5.8 版以後

## See Also

- SIN
- TAN
- ASIN
- ACOS
- ATAN
- SINH
- COSH
- TANH
