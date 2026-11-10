# SINH
**Category:** 数学関数

## Signature
```
SINH(rad)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | 以弧度为单位的角度值 |

## Returns
- 成功时：双曲正弦值（实数）
- 失败时：0.0

## Description
计算并返回双曲正弦（双曲函数）。参数的单位为弧度。

弧度是角度单位之一，180 度对应 π 弧度（π 约为 3.14159265358）。将角度转换为弧度时，计算 `角度 * 3.14159265358 / 180`（90 度约为 1.5708）。

## Example
```
_rad = 30 * 3.14159265358 / 180  // 30°をラジアンに変換
SINH(_rad)                        // 約 0.547853 を返す
```

## Compatibility
- YAYA：Tc522-1 及之后

## See Also
- SIN、COS、TAN（三角函数）
- ASIN、ACOS、ATAN（反三角函数）
- COSH、TANH（双曲函数）
