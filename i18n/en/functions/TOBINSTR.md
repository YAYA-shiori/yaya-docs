# TOBINSTR
**Category:** 文字列操作

## Signature
```
TOBINSTR( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | Integer value to convert |

## Returns
- Success: Binary number string
- Failure: VOID

## Description
Converts an integer to a binary number string.

## Example
```
_i = 30
_bin = TOBINSTR( _i )
_bin // "11110" (10進数30 = 2進数11110)
```

## Compatibility
- YAYA: Since the initial version
- AYA: 5.8 and later
- Tc574-4 / Tc602-5: Fixed an issue where the minimum integer value (-9223372036854775808) was converted to just `-`

## See Also
- TOHEXSTR
- BINSTRTOI
