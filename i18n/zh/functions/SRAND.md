# SRAND
**Category:** 数学関数

## Signature
```
SRAND( [seed] )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| seed | 随机数种子值（接受整数、实数和字符串）。省略时根据当前时间随机初始化 |

## Returns
- 成功时：1
- 失败时：0

## Description
设置整数随机数的种子。省略参数时，根据当前时间初始化种子。

系统词典中可能会使用 RAND 函数，因此使用 SRAND 时请注意影响范围。

## Compatibility
- YAYA：Tc551-1 及之后

## See Also
- RAND（随机数生成）
