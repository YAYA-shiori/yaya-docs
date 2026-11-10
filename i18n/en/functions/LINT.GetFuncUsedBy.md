# LINT.GetFuncUsedBy
**Category:** デバッグ

## Signature
```
LINT.GetFuncUsedBy(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | Name of the function to analyze |

## Returns
- Success: A generic array of function names used in the specified function (both user-defined functions and system functions)
- No candidates: An empty generic array
- Error: -1

## Description
Lists all function names used in the specified function (including user-defined functions and system functions) and returns them in a generic array. This is a Lint utility function for analyzing code dependencies and performing checks during development.

Duplicate function names are removed, and the names are returned in alphabetical order. If a string contains an embedded expression `%(式)`, `TOSTR`, which is used internally to expand it, is also included. For details on limitations, see [Specifications and limitations of LINT functions](../other/lint-functions.md).

## Compatibility
- YAYA: Available since Tc568-1

## See Also
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
- LINT.GetVarRefs
