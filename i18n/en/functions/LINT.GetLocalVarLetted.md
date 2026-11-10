# LINT.GetLocalVarLetted
**Category:** デバッグ

## Signature
```
LINT.GetLocalVarLetted(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | Name of the function to analyze |

## Returns
- Success: A generic array of local variable names assigned to in the specified function. Entry into and exit from nested scopes are represented by `{` / `}`
- No candidates (including when the result contains only `{` and `}`): An empty generic array
- Error: -1

## Description
Lists the locations in the specified function where local variables are assigned to (let) and returns them in a generic array. Locations that only read variables are not listed. To list both assignments and reads, use `LINT.GetLocalVarUsedBy`.

Variable names are returned in the order in which they are assigned. Entry into and exit from nested scopes (curly-brace blocks) are indicated by `{` and `}`.

The following are also listed as assignments.
- Compound assignments (such as `+=` and `-=`), as well as `++` and `--`
- Assignment to an array element (`_a[0] = 1` is listed as `_a`) (since Tc574-1)
- The loop variable `_v` in `foreach _list ; _v` (since Tc574-1)
- Both loop variables `_k` and `_v` in `foreach _list ; _k, _v` (since Tc600-3)

Local variables generated internally by the `case` syntax (names beginning with `_CaSe_ExPr_PrEfIx_`) are not listed (since Tc574-1).

For details on limitations, see [Specifications and limitations of LINT functions](../other/lint-functions.md).

## Compatibility
- YAYA: Available since Tc568-1
- Tc574-1: Changed to list assignments to array elements and foreach loop variables. Excludes internal case variables
- Tc600-3: Changed to list both loop variables in a two-variable foreach

## See Also
- LINT.GetLocalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetGlobalVarUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetFuncUsedBy
- LINT.GetVarRefs
