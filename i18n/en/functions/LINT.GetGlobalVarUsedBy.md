# LINT.GetGlobalVarUsedBy
**Category:** デバッグ

## Signature
```
LINT.GetGlobalVarUsedBy(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | Name of the function to analyze |

## Returns
- Success: A generic array of global variable names used in the specified function
- No candidates: An empty generic array
- Error: -1

## Description
Lists the global variable names used in the specified function and returns them in a generic array. Both assignments and reads are included.

Duplicate variable names are removed, and the names are returned in alphabetical order. Therefore, even when used together with `LINT.GetGlobalVarLetted`, you cannot determine which variables are assigned but not read. For details on limitations, see [Specifications and limitations of LINT functions](../other/lint-functions.md).

## Compatibility
- YAYA: Available since Tc568-1

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
- LINT.GetVarRefs
