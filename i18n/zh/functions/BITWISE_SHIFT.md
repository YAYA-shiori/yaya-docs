# BITWISE_SHIFT

**Category:** ビット演算

## Signature

```
BITWISE_SHIFT(var, shift)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 要进行移位运算的数值 |
| shift | 移位的位数。正值表示左移，负值表示右移 |

## Returns

成功时：位移运算的数值结果
失败时：VOID

## Description

对 `var` 执行位移运算。运算前会将其转换为整数（有符号64位；Tc566-1之前为有符号32位）。

通过 `shift` 指定位移的位数。`shift` 为正时左移，为负时右移。右移是算术移位还是逻辑移位取决于具体实现。目前发布的 Windows 版 `yaya.dll` 使用算术移位（`BITWISE_SHIFT(-8, -1)` 的结果为 `-4`）。

## Example

```
_var = 0x7fffffff
_result = BITWISE_SHIFT(_var, -2)
// _result は 0x1fffffff になる
```

## Compatibility

- YAYA: TC513-901 及之后
- Tc566-1: 随着整数变为64位，运算也改为使用64位进行

## See Also

- BITWISE_AND
- BITWISE_OR
- BITWISE_XOR
- BITWISE_NOT
