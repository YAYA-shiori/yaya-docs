# FLOOR

**Category:** 数学関数

## Signature

```
FLOOR(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | 要無條件捨去的小數 |

## Returns

- 成功時：傳回小於或等於引數的最大整數（實數型別）。動作與 C 語言的 `floor()` 相同
- 失敗時：0.0

請注意，負數會朝負無限大的方向，而不是朝零的方向取整（例如：-1.75 → -2.000000）。

## Description

捨去實數小數點以下的部分。與 C 語言的 `floor()` 相同，傳回「小於或等於引數的整數中最大的一個」，因此處理負值時請特別注意。

## Example

```
_val = 1.75
FLOOR(_val)  // 1.000000 を返す

_val = -1.75
FLOOR(_val)  // -2.000000 を返す（-1.000000 ではない）
```

## Compatibility

- YAYA：自首次發布起即可使用
- AYA：5.8 版以上

## See Also

- CEIL
- ROUND
