# BITWISE_SHIFT

**Category:** ビット演算

## Signature

```
BITWISE_SHIFT(var, shift)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | The number to shift |
| shift | The number of bits to shift. Positive values shift left; negative values shift right |

## Returns

On success: The numeric result of the bit shift operation
On failure: VOID

## Description

Performs a bit shift operation on `var`. Before the operation, it is converted to a signed 64-bit integer (signed 32-bit before Tc566-1).

Specify the number of bits to shift with `shift`. A positive `shift` shifts left, and a negative value shifts right. Whether a right shift is arithmetic or logical is implementation-dependent. The `yaya.dll` currently distributed for Windows performs an arithmetic shift (`BITWISE_SHIFT(-8, -1)` is `-4`).

## Example

```
_var = 0x7fffffff
_result = BITWISE_SHIFT(_var, -2)
// _result は 0x1fffffff になる
```

## Compatibility

- YAYA: Tc513-901 and later
- Tc566-1: The operation also uses 64 bits to match the change to 64-bit integers

## See Also

- BITWISE_AND
- BITWISE_OR
- BITWISE_XOR
- BITWISE_NOT
