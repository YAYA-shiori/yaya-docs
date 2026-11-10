# ROUND
**Category:** 数学関数

## Signature
```
ROUND( val )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| val | 要四捨五入的實數 |

## Returns
- 成功: 四捨五入後的實數
- 失敗: 0.0

## Description
將實數的小數部分四捨五入。

請注意負數邊界值的下列行為:
- `ROUND(-1.5)` → `-1.0`（不是 -2.0）
- `ROUND(-1.55)` → `-2.0`

## Example
| 輸入 | 輸出 | 備註 |
|------|------|------|
| 1.55 | 2.0 | 1.5 以上 |
| 1.45 | 1.0 | 小於 1.5 |
| 1.5  | 2.0 | 正好是 0.5 |
| -1.5 | -1.0 | 負數邊界值 |
| -1.55 | -2.0 | 負數 |

## Compatibility
- YAYA: 自初始版本起支援
- AYA: 5.8 以後

## See Also
- CEIL
- FLOOR
