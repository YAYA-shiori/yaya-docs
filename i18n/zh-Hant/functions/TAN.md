# TAN
**Category:** 数学関数

## Signature
```
TAN(rad)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | 以弧度為單位的角度值 |

## Returns
- 成功時：正切值（實數）
- 失敗時：0.0

## Description
傳回正切值。引數的單位是弧度。

弧度是角度的單位之一，180 度相當於 π 弧度（π 約為 3.14159265358）。若要將度數換算為弧度，請計算 `度數 * 3.14159265358 / 180`（90 度約為 1.5708）。

## Example
```
_rad = 45 * 3.14159265358 / 180  // 45°をラジアンに変換
TAN(_rad)  // 約 1.000000 を返す
```

## Compatibility
- YAYA：從初期版本起即可使用
- AYA：5.8 以後

## See Also
- SIN, COS（三角函式）
- ASIN, ACOS, ATAN（反三角函式）
- SINH, COSH, TANH（雙曲函式）
