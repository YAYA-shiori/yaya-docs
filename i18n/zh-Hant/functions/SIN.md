# SIN
**Category:** 数学関数

## Signature
```
SIN( rad )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | 以弧度為單位的角度（數值） |

## Returns
- 成功：正弦值（實數）
- 失敗：0.0

## Description
傳回正弦值。引數的單位為弧度。

弧度是角度的一種單位，180 度等於 π 弧度（π 約為 3.14159265358）。將角度轉換為弧度時，請計算 `度 * 3.14159265358 / 180`（90 度約為 1.5708）。

## Example
```
_rad = 30 * 3.14159265358 / 180  // 30度をラジアンに変換
SIN( _rad )  // → 0.500000
```

## Compatibility
- YAYA：從初始版本起支援
- AYA：5.8 以後

## See Also
- COS
- TAN
- ASIN
- ACOS
- ATAN
- SINH
- COSH
- TANH
