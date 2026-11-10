# SERIALIZEVAR
**Category:** メタ操作・特殊関数

## Signature
```
SERIALIZEVAR( name )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | String containing the variable name. If it starts with `_`, it is a local variable; otherwise, it is a global variable |

## Returns
A string containing the variable's value in the same format as a save file value.

If the variable does not exist, its value is VOID, or it is a variable erased with [ERASEVAR](ERASEVAR.md), the function issues warning W0012 and returns VOID.

## Description
Converts the value of the specified variable into a string in the same format that [SAVEVAR](SAVEVAR.md#保存形式) writes to a save file. Pass it to [DESERIALIZEVAR](DESERIALIZEVAR.md) to restore the same value to another variable.

A save file line has the format `変数名,値,"デリミタ",watcher|setter|destorier`, but this function returns **only the value part**. It does not include the variable name, delimiter, watcher / setter / destorier, or character encoding specification.

Unlike JSON, it preserves distinctions such as integers versus real numbers, integer keys versus string keys, and VOID versus an empty string. Nested arrays and hashes are also written as-is in the form `IARRAY{...}` / `IHASH{...}`.

The returned string is on one line, with control characters such as line breaks escaped.

## Example
```
a = 5
b = "x,y"
c = (1, "x", 2.5)
d = IHASH("k", 1)

SERIALIZEVAR("a")   // 5
SERIALIZEVAR("b")   // "x,y"（ダブルクォートを含む）
SERIALIZEVAR("c")   // 1:"x":2.5
SERIALIZEVAR("d")   // "k"=1:IHASH=IHASH
```

You can also specify a local variable.

```
_x = IARRAY
_x[0] = IHASH("k", 1)
_x[1] = "s"
_s = SERIALIZEVAR("_x")   // IHASH{"k"=1:IHASH=IHASH}:"s"
```

## Compatibility
- Tc607-3 and later

## See Also
- DESERIALIZEVAR
- SAVEVAR
- RESTOREVAR
- DUMPJSON
