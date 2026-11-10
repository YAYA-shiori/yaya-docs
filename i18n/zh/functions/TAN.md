# TAN
**Category:** 数学関数

## Signature
```
TAN(rad)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | 以弧度为单位的角度值 |

## Returns
- 成功时：正切值（实数）
- 失败时：0.0

## Description
返回正切值。参数的单位是弧度。

弧度是角度的单位之一，180 度等于 π 弧度（π 约为 3.14159265358）。将角度转换为弧度时，计算 `度 * 3.14159265358 / 180`（90 度约为 1.5708）。

## Example
```
_rad = 45 * 3.14159265358 / 180  // 45°をラジアンに変換
TAN(_rad)  // 約 1.000000 を返す
```

## Compatibility
- YAYA：从初始版本起可用
- AYA：5.8 及以后

## See Also
- SIN、COS（三角函数）
- ASIN、ACOS、ATAN（反三角函数）
- SINH、COSH、TANH（双曲函数）
