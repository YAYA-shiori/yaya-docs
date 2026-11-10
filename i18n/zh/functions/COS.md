# COS

**Category:** 数学関数

## Signature

```
COS(rad)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| rad | 以弧度为单位的角度 |

## Returns

成功时：表示余弦值的实数
失败时：0.0

## Description

返回余弦值。参数的单位为弧度。

弧度是一种角度单位，180 度等于 π 弧度（π 约为 3.14159265358）。将角度转换为弧度时，计算 `角度 * 3.14159265358 / 180`（90 度约为 1.5708）。

## Example

```
_rad = 60 * 3.14159265358 / 180  // 60° をラジアンに変換
COS(_rad)  // 0.500000 を返す
```

## Compatibility

- YAYA: 从初版起可用
- AYA: 5.8版及之后

## See Also

- SIN
- TAN
- ASIN
- ACOS
- ATAN
- SINH
- COSH
- TANH
