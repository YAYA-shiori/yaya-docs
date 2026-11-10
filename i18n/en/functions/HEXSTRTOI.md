# HEXSTRTOI
**Category:** 文字列操作

## Signature
```
HEXSTRTOI( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String containing the hexadecimal value to convert |

## Returns
- On success: converted number (integer)
- On failure: 0

## Description
Converts a string containing a hexadecimal value to an integer. If the string has a `0x` prefix, it is ignored.

## Example
```
_hex = '1E'
_i = HEXSTRTOI( _hex )
// _i は 30（16進数 1E = 10進数 30）
```

## Compatibility
- YAYA: Available from the initial release
  - Tc547-1 and later: Processes a leading `0x` prefix
- AYA: 5.8 and later

## See Also
- BINSTRTOI
- TOHEXSTR
