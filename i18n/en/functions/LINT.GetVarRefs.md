# LINT.GetVarRefs
**Category:** デバッグ

## Signature
```
LINT.GetVarRefs(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | Name of the function to analyze |

## Returns
- Success: A generic array of strings, each containing 7 comma-separated fields: `kind,category,name,access,line,depth,context`
- Error: -1

## Description
Lists each occurrence of a variable or function in the specified function, as well as each entry into or exit from a block (curly braces), as a separate item, and returns the list as a generic array. Unlike `LINT.GetLocalVarUsedBy` and similar functions, this includes the distinction between reads and writes, line numbers, block types, and the types of syntax in which the occurrences appear.

Each element is comma-separated, so you can retrieve its fields directly as a simple array.

```
_refs = LINT.GetVarRefs('OnTest')
foreach _refs ; _r {
	_kind = _r[0]
	_name = _r[2]
	_line = TOINT(_r[4])
}
```

### Fields

| Number | Field | Value |
|------|------|-----|
| 0 | kind | `var` (variable) / `func` (function) / `{` (block start) / `}` (block end) |
| 1 | category | For `var`: `local` / `global`; for `func`: `user` / `system`; for `{` and `}`: the block type |
| 2 | name | Variable or function name (empty for `{` and `}`) |
| 3 | access | For `var`: `r` (read) / `w` (assignment) / `rw` (read and write); for `func`: `call` (empty for `{` and `}`) |
| 4 | line | Line number in the dictionary file |
| 5 | depth | Block nesting depth (the function body is 1) |
| 6 | context | Type of statement in which the occurrence appears (empty for `{` and `}`) |

### access

| Value | Target |
|----|------|
| `r` | All occurrences other than assignment targets |
| `w` | Assignment targets of `=` and `:=`, assignment targets of `=` to array elements (the `_a` in `_a[0] = 1`), and `foreach` loop variables (both variables in a two-variable foreach; Tc600-3 and later) |
| `rw` | Targets of `+=`, `-=`, `*=`, `/=`, `%=`, `,=` and their `:=` forms, and targets of `++` and `--` (including compound assignments to array elements) |

Because assignments are performed after evaluating the right-hand side, assignment targets (`w` / `rw`) are listed last within the same statement.

```
_z = _z + 1
// var,local,_z,r,10,1,subst
// var,local,_z,w,10,1,subst
```

### Block types (`{` `}` category)

| Value | Target |
|----|------|
| `function` | Function body |
| `if` / `elseif` / `else` | if construct |
| `while` | while construct |
| `for` | for construct |
| `foreach` | foreach construct |
| `switch` | switch construct |
| `case` | case construct |
| `when` / `others` | when / others within a case construct |
| `plain` | Other cases (a standalone `{ }`, each block in a switch, etc.) |

A `}` has the same type and depth as its corresponding `{`.

### context

| Value | Target |
|----|------|
| `output` | Expression to output |
| `subst` | Expression containing an assignment |
| `if` / `elseif` / `while` / `switch` | Condition expression for each construct |
| `for-init` / `for-cond` / `for-step` | a / b / c in `for a ; b ; c` |
| `foreach` / `foreach-var` | a / b in `foreach a ; b` (in `foreach a ; k, v`, both k and v are `foreach-var`; Tc600-3 and later) |
| `case` / `when` | case expression / when condition |
| `parallel` / `void` / `return` | Expression for each construct |

For example, `if _c = 1` appears as an item with `context` set to `if` and `access` set to `w`.

### Items not listed

- Local variables generated internally by the `case` construct (names beginning with `_CaSe_ExPr_PrEfIx_`)
- Statements that contain no variables or functions (`break` / `continue` / `return` (without an expression) / `--`, output consisting only of literals, etc.)
- when labels (literals)

For details about limitations, see [Specifications and Limitations of LINT Functions](../other/lint-functions.md).

## Compatibility
- YAYA: Available from Tc574-1

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarUsedBy
- LINT.GetLocalVarLetted
