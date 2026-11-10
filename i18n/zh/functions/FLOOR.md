# FLOOR

**Category:** 数学関数

## Signature

```
FLOOR(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | 要向下取整的实数 |

## Returns

- 成功时：小于或等于参数的最大整数（实数类型）。行为与 C 语言的 `floor()` 相同
- 失败时：0.0

请注意，对于负数，取整方向是负方向，而不是朝向零的方向（例如：-1.75 → -2.000000）。

## Description

舍去实数的小数部分。与 C 语言的 `floor()` 一样，本函数返回“小于或等于参数的整数中最大的一个”，因此处理负值时请注意。

## Example

```
_val = 1.75
FLOOR(_val)  // 1.000000 を返す

_val = -1.75
FLOOR(_val)  // -2.000000 を返す（-1.000000 ではない）
```

## Compatibility

- YAYA: 从首次发布起即可使用
- AYA: 5.8 及以上版本

## See Also

- CEIL
- ROUND
