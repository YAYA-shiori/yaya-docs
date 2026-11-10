# LINT.GetGlobalVarLetted
**Category:** デバッグ

## Signature
```
LINT.GetGlobalVarLetted(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | Name of the function to analyze |

## Returns
- Success: A generic array of global variable names assigned to in the specified function
- No candidates: An empty generic array
- Error: -1

## Description
Lists the locations in the specified function where global variables are assigned to (let) and returns them in a generic array. Locations that only read variables are not listed. To list reads as well, use `LINT.GetGlobalVarUsedBy`.

Duplicate variable names are removed, and the names are returned in alphabetical order.

The following are also listed as assignments.
- Compound assignments (such as `+=` and `-=`), as well as `++` and `--`
- Assignment to an array element (`G_a[0] = 1` is listed as `G_a`) (since Tc574-1)
- The loop variable `G_v` in `foreach _list ; G_v` (since Tc574-1)
- Both loop variables `G_k` and `G_v` in `foreach _list ; G_k, G_v` (since Tc600-3)

For details on limitations, see [Specifications and limitations of LINT functions](../other/lint-functions.md).

## Compatibility
- YAYA: Available since Tc568-1
- Tc574-1: Changed to list assignments to array elements and foreach loop variables
- Tc600-3: Changed to list both loop variables in a two-variable foreach

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetLocalVarUsedBy
- LINT.GetLocalVarLetted
- LINT.GetVarRefs
