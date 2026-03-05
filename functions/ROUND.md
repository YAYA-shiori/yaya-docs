# ROUND
**Category:** 数学関数
**Source:** マニュアル/関数/ROUND

## Signature
```
ROUND( val )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| val | 四捨五入する実数 |

## Returns
- 成功: 四捨五入された実数
- 失敗: 0.0

## Description
実数の小数点以下を四捨五入します。

負数の境界値では以下の挙動に注意してください:
- `ROUND(-1.5)` → `-1.0`（-2.0ではない）
- `ROUND(-1.55)` → `-2.0`

## Example
| 入力 | 出力 | 備考 |
|------|------|------|
| 1.55 | 2.0 | 1.5以上 |
| 1.45 | 1.0 | 1.5未満 |
| 1.5  | 2.0 | ちょうど0.5 |
| -1.5 | -1.0 | 負の境界値 |
| -1.55 | -2.0 | 負の値 |

## Compatibility
- YAYA: 初期バージョンより対応
- AYA: 5.8以降

## See Also
- CEIL
- FLOOR
