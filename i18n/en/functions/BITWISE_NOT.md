# BITWISE_NOT

**Category:** ビット演算

## Signature

```
BITWISE_NOT( var )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | The number to operate on |

## Returns

On success: The numeric result of the bitwise NOT operation
On failure: VOID

## Description

Performs a bitwise NOT operation on `var`. Before the operation, it is converted to a signed 64-bit integer (signed 32-bit before Tc566-1).

## Example

```
_val = 28          // 2進数: 00011100
BITWISE_NOT(_val)  // -29 (2進数: 11100011) を返す
```

## Compatibility

- YAYA: Tc513-901 and later
- Tc566-1: The operation also uses 64 bits to match the change to 64-bit integers

## See Also

- BITWISE_AND
- BITWISE_OR
- BITWISE_XOR
- BITWISE_SHIFT
