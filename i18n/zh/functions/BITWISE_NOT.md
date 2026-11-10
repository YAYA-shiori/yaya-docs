# BITWISE_NOT

**Category:** ビット演算

## Signature

```
BITWISE_NOT( var )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 要进行运算的数值 |

## Returns

成功时：位非运算后的数值结果
失败时：VOID

## Description

对 `var` 执行位非运算。运算前会将其转换为整数（有符号 64 位；Tc566-1 之前为有符号 32 位）。

## Example

```
_val = 28          // 2進数: 00011100
BITWISE_NOT(_val)  // -29 (2進数: 11100011) を返す
```

## Compatibility

- YAYA：Tc513-901 及以上
- Tc566-1：为与整数变为 64 位相适应，运算也改为使用 64 位

## See Also

- BITWISE_AND
- BITWISE_OR
- BITWISE_XOR
- BITWISE_SHIFT
