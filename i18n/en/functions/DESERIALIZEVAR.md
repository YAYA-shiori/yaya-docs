# DESERIALIZEVAR
**Category:** メタ操作・特殊関数

## Signature
```
DESERIALIZEVAR( name, text )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | A string containing the name of the variable to restore. If it starts with `_`, it is a local variable; otherwise, it is a global variable. The variable is created if it does not exist. |
| text | A string in the format returned by [SERIALIZEVAR](SERIALIZEVAR.md) |

## Returns
Returns 1 if restoration succeeds. Returns 0 if `text` cannot be parsed as the specified format or an argument is invalid (the variable is left unchanged).

## Description
Reads `text` as a value in the format that [SAVEVAR](SAVEVAR.md#保存形式) writes to a save file, then stores it in the variable named `name`. Any value the variable previously held is replaced, and its type is determined by the contents of `text` (integer / real / string / array / hash).

As with [LETTONAME](LETTONAME.md), any setter / watcher configured for the variable is not called. Delimiter and setter / watcher / destorier settings are not changed.

In the following cases, a warning is issued and 0 is returned; the variable is not created or modified.

| Case | Warning |
|------|------|
| Too few arguments | W0008 |
| `name` or `text` is not a string | W0009 |
| `name` is an empty string | W0010 |
| `name` cannot be used as a variable name (contains `,`, has the same name as a system function or reserved word, etc.) | W0012 |
| `text` cannot be parsed as the specified format (an empty string, a string without double quotes, an array without `:`, a value consisting only of `IVOID`, etc.) | W0026 |

## Example
```
a = (1, "x", 2.5)
_s = SERIALIZEVAR("a")
_r = DESERIALIZEVAR("b", _s)   // b が (1, "x", 2.5) になる。_r は 1

DESERIALIZEVAR("n", "0.5")     // n が実数 0.5 になる
DESERIALIZEVAR("m", "abc")     // 0。警告 W0026
```

Restoring to a local variable:

```
_x = IARRAY
_x[0] = IHASH("k", 1)
_x[1] = "s"
_r = DESERIALIZEVAR("_y", SERIALIZEVAR("_x"))
// _y は _x と同じ入れ子の配列になる
```

## Compatibility
- Tc607-3 and later

## See Also
- SERIALIZEVAR
- SAVEVAR
- RESTOREVAR
- LETTONAME
- PARSEJSON
