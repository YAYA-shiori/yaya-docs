# GETTYPEEX
**Category:** 型取得/変換

## Signature
```
GETTYPEEX( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | Name of the variable whose type to check (passed as a string) |

## Returns
- 0: Internal error (failure)
- 1: Integer
- 2: Real number
- 3: String
- 4: Generic array
- 5: Hash (Tc600-3 and later)

## Description
Gets the data type of the specified variable. The main difference from `GETTYPE` is that the argument is the **variable name as a string**, not the variable itself.

This function also returns the correct type for generic arrays with one element, so use it in cases where `GETTYPE` cannot determine the type correctly due to its backward-compatible behavior.

## Compatibility
- YAYA: Tc537-3 and later
- Tc600-3: Changed to return 5 for hashes

## See Also
- GETTYPE
- GETVARLIST
