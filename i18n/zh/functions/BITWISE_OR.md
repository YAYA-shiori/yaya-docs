# BITWISE_OR

**Category:** ビット演算

## Signature

```
BITWISE_OR( var1 , var2 )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var1 | 数值 |
| var2 | 数值 |

## Returns

成功时：位或运算的数值结果
失败时：VOID

## Description

对 `var1` 和 `var2` 执行位或运算。运算前会分别将它们转换为整数（有符号 64 位；Tc566-1 之前为有符号 32 位）。

## Example

```
_val1 = 28  // 2進数: 11100
_val2 = 9   // 2進数: 01001
BITWISE_OR( _val1, _val2 )  // 29 (2進数: 11101) を出力
```

## Compatibility

- YAYA：Tc513-901 及以上
- Tc566-1：为与整数变为 64 位相适应，运算也改为使用 64 位

## See Also

- BITWISE_AND
- BITWISE_XOR
- BITWISE_NOT
- BITWISE_SHIFT
