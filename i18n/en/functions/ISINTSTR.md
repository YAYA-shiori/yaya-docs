# ISINTSTR
**Category:** 文字列操作

## Signature
```
ISINTSTR( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String to check for interpretation as an integer |

## Returns
- 1: The string can be interpreted as an integer
- 0: The string cannot be interpreted as an integer

## Description
Checks whether the specified string can be interpreted as an integer. This function complements ISREALSTR and is useful for distinguishing string representations of integers from those of floating-point numbers.

## Compatibility
- YAYA: Available from the initial release
- AYA: 5.8 and later

## See Also
- ISREALSTR
