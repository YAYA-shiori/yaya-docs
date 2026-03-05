# ATAN

**Category:** 数学関数
**Source:** マニュアル/関数/ATAN

## Signature

```
ATAN(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | アークタンジェントを求める実数値 |

## Returns

成功時：アークタンジェントの値をラジアンで返す（実数）
失敗時：0.0

## Example

```
_d = ATAN(1.0)               // 約 0.785398 ラジアンを返す
_d * 180 / 3.14159265358     // 約 45 度に変換
```

## Compatibility

- YAYA: 初期リリースから利用可能
- AYA: バージョン 5.8 以降

## See Also

- ASIN
- ACOS
- SIN
- COS
- TAN
- SINH
- COSH
- TANH
