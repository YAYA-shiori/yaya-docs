# TOSTR
**Category:** 型取得/変換

## Signature
```
TOSTR( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | Integer, real number, or generic array to convert |

## Returns
- Success: Converted string
- Failure: VOID

## Description
Converts an integer, real number, or generic array to a string. If a generic array is passed, returns a string with its elements joined by commas.

## Example
```
_i = 100
_result = TOSTR( _i )
// "100"

_array = ('さくら','ねここ','まゆら')
_result = TOSTR( _array )
// "さくら,ねここ,まゆら"
```

## Compatibility
- YAYA: Since the initial version
- AYA: 5.8 and later
- Tc574-4 / Tc602-5: Fixed an issue where the minimum integer value (-9223372036854775808) was converted to just `-`
- Tc574-4 / Tc601-1: Fixed an issue where converting real numbers of 1e57 or greater to strings could leave trailing garbage

## See Also
- TOINT
- TOREAL
