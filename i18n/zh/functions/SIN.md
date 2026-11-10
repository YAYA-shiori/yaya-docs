# SIN
**Category:** 数学関数

## Signature
```
SIN( rad )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | 以弧度为单位的角度（数值） |

## Returns
- 成功：正弦值（实数）
- 失败：0.0

## Description
返回正弦值。参数的单位为弧度。

弧度是角度单位之一，180 度对应 π 弧度（π 约为 3.14159265358）。将角度转换为弧度时，计算 `角度 * 3.14159265358 / 180`（90 度约为 1.5708）。

## Example
```
_rad = 30 * 3.14159265358 / 180  // 30度をラジアンに変換
SIN( _rad )  // → 0.500000
```

## Compatibility
- YAYA：从初始版本起支持
- AYA：5.8 及之后

## See Also
- COS
- TAN
- ASIN
- ACOS
- ATAN
- SINH
- COSH
- TANH
