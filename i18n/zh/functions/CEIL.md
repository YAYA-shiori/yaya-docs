# CEIL

**Category:** 数学関数

## Signature

```
CEIL(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | 要向上取整的实数 |

## Returns

成功时：向上取整后的实数
失败时：0.0

与 C 语言的 ceil() 函数相同，返回「大于或等于参数的最小整数」。需要注意负数的处理方式。

## Description

将实数的小数部分向上取整。与 C 语言的 `ceil()` 一样，返回「大于或等于参数的整数中最小的一个」，因此处理负值时要特别注意。

## Example

```
CEIL(1.75)   // 2.000000 を返す
CEIL(-1.75)  // -1.000000 を返す（-2ではなく切り上げのため）
CEIL(7/3)    // 2.000000 を返す（整数除算のため7/3=2）
CEIL(7.0/3)  // 3.000000 を返す（実数除算）
```

## Compatibility

- YAYA: 从初版起可用
- AYA: 5.8版及之后

## See Also

- FLOOR
- ROUND
