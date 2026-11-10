# Specifications and Constraints of LINT Functions

The `LINT.*` functions are a group of debugging functions that extract where functions and variables are used from the analysis results of loaded dictionaries (statements and expression terms inside functions). They provide the building blocks for implementing static checks such as yayalint in YAYA dictionaries, but they have the following specifications and constraints.

## Function List

| Function | Target | Duplicates | Scope `{` `}` | Read/write distinction | Line |
|------|------|------|------|------|------|
| [LINT.GetVarRefs](../functions/LINT.GetVarRefs.md) | Variables, functions, and blocks | Each occurrence | Yes (with type) | Yes | Yes |
| [LINT.GetFuncUsedBy](../functions/LINT.GetFuncUsedBy.md) | Functions (user-defined and system) | Removed, sorted by name | No | - | No |
| [LINT.GetUserDefFuncUsedBy](../functions/LINT.GetUserDefFuncUsedBy.md) | User-defined functions | Removed, sorted by name | No | - | No |
| [LINT.GetGlobalVarUsedBy](../functions/LINT.GetGlobalVarUsedBy.md) | Global variables (both reads and writes) | Removed, sorted by name | No | No | No |
| [LINT.GetGlobalVarLetted](../functions/LINT.GetGlobalVarLetted.md) | Global variables (assignments only) | Removed, sorted by name | No | - | No |
| [LINT.GetLocalVarUsedBy](../functions/LINT.GetLocalVarUsedBy.md) | Local variables (both reads and writes) | Each occurrence | Yes | No | No |
| [LINT.GetLocalVarLetted](../functions/LINT.GetLocalVarLetted.md) | Local variables (assignments only) | Each occurrence | Yes | - | No |

When writing a new check, use `LINT.GetVarRefs` to retrieve information that includes everything provided by the other functions.

## Changes in Tc574-1

- Added `LINT.GetVarRefs`.
- `GetGlobalVarLetted` / `GetLocalVarLetted`
  - Assignments to array elements (`_a[0] = 1`, `G_a[0] = 1`) are now listed as assignments to those variables.
  - The loop variable `_v` in a `foreach _list ; _v` loop is now listed as an assignment.
- `GetLocalVarUsedBy`
  - Within the same statement, the variable being assigned is now listed last. Since assignment occurs after the right-hand side is evaluated, `_z = _z + 1` is listed in the order `_z` (read) → `_z` (assignment).
- `GetLocalVarUsedBy` / `GetLocalVarLetted`
  - Local variables generated internally by the `case` syntax (names beginning with `_CaSe_ExPr_PrEfIx_`) are no longer listed.

## Limitations

### Requires dictionaries to be loaded

The dictionaries being analyzed must have loaded successfully. If a dictionary cannot be loaded due to a syntax error or other issue, YAYA enters emergency mode, and the dictionary using the LINT functions will not run. Duplicate definitions, syntax errors, and calls to undefined functions with parentheses (E0071) are reported as errors by YAYA itself during loading.

### Source Locations

- Lines are available from `LINT.GetVarRefs`. The line number is for the statement.
- For statements spanning multiple lines due to `/` line continuation or a here document, the number is that of the **last line**.
- Column numbers are unavailable. They are not stored internally by YAYA either. This is because lines are joined, `#define` substitutions are performed, comments are removed, and statements are split at `{`, `}`, and `;` during loading.

### How Names Appear

- `#define` / `#globaldefine` are substituted as strings during loading, so the names shown are the names after substitution.
- Names specified as strings, such as `EVAL('name')` or `LETTONAME('name', …)`, cannot be tracked.
- The functions and variables in the dictionary being linted are also included in the list. Exclude them by using a prefix or similar method.
- `TOSTR`, which is used internally to expand embedded expressions `%(expression)`, is included as a function call (`LINT.GetFuncUsedBy` / `LINT.GetVarRefs`). It cannot be distinguished from `TOSTR` written by the user.

### Distinguishing Reads and Writes

- In `LINT.GetVarRefs`, a variable assigned to with `=` is marked `w`; a variable assigned to with a compound assignment (such as `+=`, including `++` and `--`) is marked `rw`.
- Assignment to an array element with `=` (`_a[0] = 1`) is treated as `w`. Other elements of the array remain, but assignment to an element of an undefined variable is also allowed.
- Reordering (placing the assignment target last) is done per statement. When an expression contains multiple assignments, the order may not match the execution order.
- Functions other than `LINT.GetVarRefs` do not indicate whether a variable was read or written.
  - `GetGlobalVarUsedBy` / `GetGlobalVarLetted` remove duplicates, so they cannot identify global variables that are assigned to but never read.
  - You cannot determine whether each item in `GetLocalVarUsedBy` is a read or an assignment by matching it one by one against `GetLocalVarLetted`.

### Syntax information

- The block type and the types of syntax constructs that occur (such as conditional expressions, parts of a for loop, and case expressions) can be obtained with `LINT.GetVarRefs`.
- Statements that do not contain variables or functions (such as `break` / `continue` / `return` with no expression / `--`, and output consisting only of literals) are not listed.
- Since `others` is internally converted to `else`, “else directly under a case block” is classified as `others`.
- Since `when` is internally converted to `if` / `elseif`, this is determined by whether it contains case-internal variables.

### Analysis scope

- The flow of branches and loops must be reconstructed on the dictionary side from the block types and depths.
- For analysis across functions (such as how the `_argv` argument is used and where global variables are assigned), the results for each function must be cross-referenced on the dictionary side.

## Example inspection setup

| Inspection | Possible | Method |
|------|------|------|
| Unused functions | Yes | Collect `func,user` from `LINT.GetVarRefs` for all functions in `GETFUNCLIST`, then list functions that do not appear anywhere (excluding those called externally, such as event functions) |
| Unused local variables | Yes | For each scope (`{` `}`), find variables that have only `w` and no `r` / `rw` |
| Reads of undefined local variables | Yes (branches must be considered on the dictionary side) | Trace from the beginning in order, and look for `r` / `rw` before `w` / `rw` appears in that scope or an outer scope |
| Unused global variables | Yes | Collect `var,global` from all functions and find variables that have only `w` (reads through `EVAL`, etc. cannot be tracked) |
| Assignments in conditional expressions | Yes | Look for cases where `context` is `if` / `elseif` / `while` / `switch` / `for-cond` and `access` is `w` / `rw` |
| Invalid case clauses | Partially | Check whether, directly under a `case` block (depth +1), there are any blocks other than `when` / `others` or any entries whose `context` is not `when`. Statements that contain no variables or functions cannot be detected |
| Candidates for misspelled names | Yes | Calculate edit distance against `GETFUNCLIST` / `GETVARLIST` on the dictionary side |
| Display of line and column | Lines only | Columns cannot be obtained |
