# LOGGING
**Category:** デバッグ

## Signature
```
LOGGING(var)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | Value to write to the log. Any data type can be specified |

## Returns
VOID (no return value)

## Description
Writes the specified value to the log file and also displays it in the debugging tool "Tama." Any data type is accepted.

Simple arrays are output with their values joined by commas.

## Output Format

When multiple arguments are specified or an array is passed, each value is written on one line, separated by commas. Strings are enclosed in `"`.

```
LOGGING('a', 1, 2.5)   // "a",1,2.500000
```

When a value contains an array or hash (Tc602-8 and later), arrays are enclosed in `( )`, hashes in `{ }`, and hash elements are written in the form `key=value`. The same rules apply to nested contents, making it clear which parts are nested.

```
_h = PARSEJSON('{"l":[1,2],"m":{"x":"a"}}')
LOGGING(_h)                           // {"l"=(1,2),"m"={"x"="a"}}
LOGGING(PARSEJSON('[[1,[2,"s"]],3]'))  // (1,(2,"s")),3
```

The outermost array is expanded as arguments, so it is not enclosed in parentheses.

## Compatibility
- YAYA: Available since the initial version
- AYA: Available from version 5.8 onward
- Tc602-8: Changed output to enclose nested arrays in `( )` and hashes in `{ }` (previously, nested contents were also joined by `,` or `=`, and strings used as hash keys or values were not enclosed in `"`)

## See Also
- GETERRORLOG
- CLEARERRORLOG
- GETLASTERROR
- SETLASTERROR
