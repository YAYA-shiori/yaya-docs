# BITWISE_XOR

**Category:** ビット演算

## Signature

```
BITWISE_XOR( var1 , var2 )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var1 | 要进行位运算的值 |
| var2 | 要进行位运算的值 |

## Returns

成功时：位 XOR 运算的结果（数值）
失败时：VOID

## Description

对 `var1` 和 `var2` 执行位 XOR 运算。运算前会分别将它们转换为整数（有符号64位；Tc566-1之前为有符号32位）。

## Example

```
_val1 = 28 // binary: 11100
_val2 = 9  // binary: 01001
BITWISE_XOR( _val1, _val2 ) // 21 を返す（2進数: 10101）
```

## Compatibility

- YAYA: TC513-901及之后
- Tc566-1: 随着整数变为64位，运算也改为使用64位进行

## See Also

- BITWISE_AND
- BITWISE_OR
- BITWISE_NOT
- BITWISE_SHIFT
