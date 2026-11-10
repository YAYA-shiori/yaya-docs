# GETSTRBYTES
**Category:** 文字列操作

## Signature
```
GETSTRBYTES( string [ , code ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String whose byte length is to be calculated |
| code | Character encoding ID (defaults to 0), or a character encoding name ([Character encoding names](../grammar/11-character-encoding.md#文字コードの名前)). Calculates the byte length using the specified encoding. If the name is unknown, issues warning W0012 and returns 0 |

## Returns
- On success: Number of bytes required to store the string (integer)
- On failure: 0

## Description
Calculates the number of bytes required to store a string. This can be used to check memory usage for each character encoding.

## Compatibility
- YAYA: Available since the initial version
- AYA: 5.8 and later
- Tc574-8 / Tc603-1: Changed to issue warning W0012 and return 0 when given an unknown character encoding name (previously, no warning was issued and the OS default was used)

## See Also
- GETSETTING
- GETSYSTEMFUNCLIST
