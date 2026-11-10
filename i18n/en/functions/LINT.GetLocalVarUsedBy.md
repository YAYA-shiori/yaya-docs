# LINT.GetLocalVarUsedBy
**Category:** デバッグ

## Signature
```
LINT.GetLocalVarUsedBy(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | Name of the function to analyze |

## Returns
- Success: A generic array of local variable names used within the specified function. Entry to and exit from nested scopes are represented by `{` / `}`
- No candidates (including when the result contains only `{` and `}`): An empty generic array
- Error: -1

## Description
Lists the local variable names used within the specified function and returns them in a generic array. Both assignments and reads are included.

Variable names are returned in the order in which they are used. Entry to and exit from nested scopes (brace blocks) are indicated by `{` and `}`.

In Tc574-1 and later, variables assigned to within the same statement (including `foreach` loop variables) are listed at the end of that statement. This is because assignment occurs after evaluation of the right-hand side.

```
_z = _z + 1      // → _z（読み）, _z（代入）
_a[0] = _b       // → _b, _a
```

Local variables generated internally by the `case` syntax (names beginning with `_CaSe_ExPr_PrEfIx_`) are not listed (Tc574-1 and later).

The return value does not distinguish between reads and assignments. For details about the restrictions, see [Specifications and restrictions of LINT functions](../other/lint-functions.md).

## Compatibility
- YAYA: Available from Tc568-1
- Tc574-1: Changed to list variables assigned to within the same statement at the end. Excludes internal variables of case

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarLetted
- LINT.GetVarRefs
