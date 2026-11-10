# FLOOR

**Category:** 数学関数

## Signature

```
FLOOR(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | Real number to round down |

## Returns

- On success: The greatest integer less than or equal to the argument (real-number type). Works like C's `floor()`
- On failure: 0.0

Note that for negative numbers, rounding is toward negative infinity, not toward zero (for example, -1.75 → -2.000000).

## Description

Rounds down the fractional part of a real number. As with C's `floor()`, it returns the greatest integer less than or equal to the argument, so take care with negative values.

## Example

```
_val = 1.75
FLOOR(_val)  // 1.000000 を返す

_val = -1.75
FLOOR(_val)  // -2.000000 を返す（-1.000000 ではない）
```

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later

## See Also

- CEIL
- ROUND
