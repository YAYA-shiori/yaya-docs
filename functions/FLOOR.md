# FLOOR

**Category:** 数学関数
**Source:** マニュアル/関数/FLOOR

## Signature

```
FLOOR(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | 切り捨てる実数 |

## Returns

- 成功時: 引数以下の最大の整数（実数型）。C言語の `floor()` と同様の動作
- 失敗時: 0.0

負の数の場合、ゼロ方向ではなく負の方向に丸められることに注意（例: -1.75 → -2.000000）。

## Example

```
_val = 1.75
FLOOR(_val)  // Returns 1.000000

_val = -1.75
FLOOR(_val)  // Returns -2.000000 (not -1.000000)
```

## Compatibility

- YAYA: 初回リリースから利用可能
- AYA: バージョン 5.8 以降

## See Also

- CEIL
- ROUND
