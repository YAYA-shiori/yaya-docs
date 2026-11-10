# BITWISE_AND

**Category:** ビット演算

## Signature

```
BITWISE_AND( var1 , var2 )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var1 | Number |
| var2 | Number |

## Returns

On success: The numeric result of the bitwise AND operation
On failure: VOID

## Description

Performs a bitwise AND operation on `var1` and `var2`. Before the operation, each value is converted to a signed 64-bit integer (signed 32-bit before Tc566-1).

## Example

```
_val1 = 30  // 2進数: 11110
_val2 = 13  // 2進数: 01101
BITWISE_AND(_val1, _val2)  // 12 (2進数: 01100) を出力
```

## Compatibility

- YAYA: Tc513-901 and later
- Tc566-1: The operation also uses 64 bits to match the change to 64-bit integers

## See Also

- BITWISE_OR
- BITWISE_XOR
- BITWISE_NOT
- BITWISE_SHIFT
