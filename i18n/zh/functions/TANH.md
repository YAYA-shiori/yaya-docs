# TANH
**Category:** 数学関数

## Signature
```
TANH(rad)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | 以弧度为单位的角度值 |

## Returns
- 成功时：双曲正切（实数）
- 失败时：0.0

## Description
返回双曲正切（双曲函数）。参数的单位是弧度。

弧度是角度单位之一，180 度等于 π 弧度（π 约为 3.14159265358）。要将度转换为弧度，计算 `度 * 3.14159265358 / 180`（90 度约为 1.5708）。

## Example
```
_rad = 45 * 3.14159265358 / 180  // 45°をラジアンに変換
TANH(_rad)  // 約 0.655794 を返す
```

## Compatibility
- YAYA: Tc522-1以降

## See Also
- SIN, COS, TAN（三角函数）
- ASIN, ACOS, ATAN（反三角函数）
- SINH, COSH（双曲函数）
