# SINH
**Category:** 数学関数

## Signature
```
SINH(rad)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | 以弧度為單位的角度值 |

## Returns
- 成功時：雙曲正弦（實數）
- 失敗時：0.0

## Description
計算並傳回雙曲正弦（雙曲函數）。引數的單位為弧度。

弧度是角度的一種單位，180 度等於 π 弧度（π 約為 3.14159265358）。將角度轉換為弧度時，請計算 `度 * 3.14159265358 / 180`（90 度約為 1.5708）。

## Example
```
_rad = 30 * 3.14159265358 / 180  // 30°をラジアンに変換
SINH(_rad)                        // 約 0.547853 を返す
```

## Compatibility
- YAYA：Tc522-1 以後

## See Also
- SIN, COS, TAN（三角函數）
- ASIN, ACOS, ATAN（反三角函數）
- COSH, TANH（雙曲函數）
