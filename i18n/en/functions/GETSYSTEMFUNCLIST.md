# GETSYSTEMFUNCLIST
**Category:** メタ操作・特殊関数

## Signature
```
GETSYSTEMFUNCLIST( [ prefix ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| prefix | (Optional) Returns only system function names that start with the specified string. If omitted, returns all system functions |

## Returns
- On success: Generic array of system function names
- On failure: IARRAY

## Description
Returns a list of system functions. If `prefix` is specified, only system function names that start with that string are returned. If omitted, a list of all system functions is returned.

## Compatibility
- YAYA: Tc557-1 and later

## See Also
- GETVARLIST
- GETFUNCLIST
