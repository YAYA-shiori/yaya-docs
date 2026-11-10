# TOHEXSTR
**Category:** 文字列操作

## Signature
```
TOHEXSTR( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | Integer value to convert |

## Returns
- Success: Hexadecimal number string
- Failure: VOID

## Description
Converts an integer to a hexadecimal number string.

## Example
```
_i = 30
_hex = TOHEXSTR( _i )
_hex // "1E" (10進数30 = 16進数1E)
```

## Compatibility
- YAYA: Since the initial version
- AYA: 5.8 and later
- Tc574-4 / Tc602-5: Fixed an issue where the minimum integer value (-9223372036854775808) was converted to just `-`

## See Also
- TOBINSTR
- HEXSTRTOI
