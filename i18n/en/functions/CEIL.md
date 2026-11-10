# CEIL

**Category:** 数学関数

## Signature

```
CEIL(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | A real number to round up |

## Returns

On success: the rounded-up real number
On failure: 0.0

Like the C language ceil() function, this returns “the smallest integer greater than or equal to the argument.” Take care when handling negative numbers.

## Description

Rounds up the fractional part of a real number. Like the C language `ceil()` function, it returns “the smallest integer among those greater than or equal to the argument,” so take care with negative values.

## Example

```
CEIL(1.75)   // 2.000000 を返す
CEIL(-1.75)  // -1.000000 を返す（-2ではなく切り上げのため）
CEIL(7/3)    // 2.000000 を返す（整数除算のため7/3=2）
CEIL(7.0/3)  // 3.000000 を返す（実数除算）
```

## Compatibility

- YAYA: Available since the first release
- AYA: Version 5.8 and later

## See Also

- FLOOR
- ROUND
