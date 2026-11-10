# BITWISE_XOR

**Category:** ビット演算

## Signature

```
BITWISE_XOR( var1 , var2 )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var1 | Value to use in the bitwise operation |
| var2 | Value to use in the bitwise operation |

## Returns

On success: The result of the bitwise XOR operation (number)
On failure: VOID

## Description

Performs a bitwise XOR operation on `var1` and `var2`. Before the operation, each value is converted to a signed 64-bit integer (signed 32-bit before Tc566-1).

## Example

```
_val1 = 28 // binary: 11100
_val2 = 9  // binary: 01001
BITWISE_XOR( _val1, _val2 ) // 21 を返す（2進数: 10101）
```

## Compatibility

- YAYA: TC513-901 and later
- Tc566-1: The operation also uses 64 bits to match the change to 64-bit integers

## See Also

- BITWISE_AND
- BITWISE_OR
- BITWISE_NOT
- BITWISE_SHIFT
