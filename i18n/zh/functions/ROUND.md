# ROUND
**Category:** 数学関数

## Signature
```
ROUND( val )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| val | 要四舍五入的实数 |

## Returns
- 成功: 四舍五入后的实数
- 失败: 0.0

## Description
对实数的小数部分进行四舍五入。

请注意负数边界值时的行为:
- `ROUND(-1.5)` → `-1.0`（不是 -2.0）
- `ROUND(-1.55)` → `-2.0`

## Example
| 输入 | 输出 | 备注 |
|------|------|------|
| 1.55 | 2.0 | 不小于 1.5 |
| 1.45 | 1.0 | 小于 1.5 |
| 1.5  | 2.0 | 正好为 0.5 |
| -1.5 | -1.0 | 负数边界值 |
| -1.55 | -2.0 | 负值 |

## Compatibility
- YAYA: 初始版本起支持
- AYA: 5.8 及以上版本

## See Also
- CEIL
- FLOOR
