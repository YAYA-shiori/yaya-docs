# LINT.GetUserDefFuncUsedBy
**Category:** デバッグ

## Signature
```
LINT.GetUserDefFuncUsedBy(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | Name of the function to analyze |

## Returns
- Success: A generic array of user-defined function names used in the specified function
- No candidates: An empty generic array
- Error: -1

## Description
Lists the user-defined function names used in the specified function and returns them in a generic array. System functions are not included (to list system functions as well, use `LINT.GetFuncUsedBy`).

Duplicate function names are removed, and the names are returned in alphabetical order. Functions called from strings using `EVAL` and similar methods are not included. For details on limitations, see [Specifications and limitations of LINT functions](../other/lint-functions.md).

## Compatibility
- YAYA: Available since Tc568-1

## See Also
- LINT.GetFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
- LINT.GetVarRefs
