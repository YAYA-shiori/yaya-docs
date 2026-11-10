# BITWISE_OR

**Category:** ビット演算

## Signature

```
BITWISE_OR( var1 , var2 )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var1 | Number |
| var2 | Number |

## Returns

On success: The numeric result of the bitwise OR operation
On failure: VOID

## Description

Performs a bitwise OR operation on `var1` and `var2`. Before the operation, each value is converted to a signed 64-bit integer (signed 32-bit before Tc566-1).

## Example

```
_val1 = 28  // 2進数: 11100
_val2 = 9   // 2進数: 01001
BITWISE_OR( _val1, _val2 )  // 29 (2進数: 11101) を出力
```

## Compatibility

- YAYA: Tc513-901 and later
- Tc566-1: The operation also uses 64 bits to match the change to 64-bit integers

## See Also

- BITWISE_AND
- BITWISE_XOR
- BITWISE_NOT
- BITWISE_SHIFT
