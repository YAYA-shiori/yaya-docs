# FLOOR

**Category:** 数学関数

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

## Description

実数の小数点以下を切り捨てる。C 言語の `floor()` と同じく「引数以下の整数の中で最大のもの」を返すので、負の値では注意すること。

## Example

```
_val = 1.75
FLOOR(_val)  // 1.000000 を返す

_val = -1.75
FLOOR(_val)  // -2.000000 を返す（-1.000000 ではない）
```

## Compatibility

- YAYA: 初回リリースから利用可能
- AYA: バージョン 5.8 以降

## See Also

- CEIL
- ROUND
