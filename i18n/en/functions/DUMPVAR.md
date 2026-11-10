# DUMPVAR

**Category:** デバッグ

## Signature

```
DUMPVAR()
```

## Parameters

None

## Returns

Returns no value (VOID).

## Description

Outputs a variable dump to the log. When executed, it writes the state of all variables at that point to the default log file (usually ayame.log). This is a debugging utility for checking the state of variables at a specific point during script execution.

## Output format

Writes one variable per line in the form `[number] variable name = value`. Values are typed.

| Type | Format |
|---|---|
| Integer, real number, string | `(int)5`, `(double)2.500000`, `(string)abc` |
| VOID | `(nop/void)` |
| Generic array | Followed by `(array) : `, with elements separated by spaces |
| Hash (Tc600-4 and later) | Followed by `(hash) : `, with `key=value` pairs separated by spaces |
| Nested elements (Tc600-4 and later) | Arrays are enclosed in `(array)[ ... ]`; hashes are enclosed in `(hash){ ... }` |

```
[0] count = (int)3
[1] list = (array) : (int)1 (string)p
[2] h = (hash) : (string)a=(int)1 (string)l=(array)[ (int)1 (int)2 ] (string)n=(hash){ (string)x=(double)2.500000 }
```

## Compatibility

- YAYA: Tc529-2 and later
- Tc600-4: Hashes and nested values are now output (previously, hashes appeared as `(unknown type)` and nested elements as `(?UNKNOWN)`)
