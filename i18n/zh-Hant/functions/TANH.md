# TANH
**Category:** 数学関数

## Signature
```
TANH(rad)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | 以弧度為單位的角度值 |

## Returns
- 成功時：雙曲正切（實數）
- 失敗時：0.0

## Description
傳回雙曲正切（雙曲函式）。引數的單位是弧度。

弧度是角度單位之一，180 度相當於 π 弧度（π 約為 3.14159265358）。要將角度換算成弧度，請計算 `度 * 3.14159265358 / 180`（90 度約為 1.5708）。

## Example
```
_rad = 45 * 3.14159265358 / 180  // 45°をラジアンに変換
TANH(_rad)  // 約 0.655794 を返す
```

## Compatibility
- YAYA：Tc522-1 之後

## See Also
- SIN、COS、TAN（三角函式）
- ASIN、ACOS、ATAN（反三角函式）
- SINH、COSH（雙曲函式）
