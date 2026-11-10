# SAVEVAR
**Category:** メタ操作・特殊関数

## Signature
```
SAVEVAR( [path] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Destination file name (if omitted, DLL name + "_variable.cfg"; e.g., yaya_variable.cfg) |

## Returns
None (VOID)

## Description
Saves variables. This is equivalent to the processing performed when unloading.

You can also specify an arbitrary path for the destination file.

## Save Format

Writes one variable per line in the following format.

```
変数名,値,"デリミタ",watcher|setter|destorier
```

Values are formatted as follows.

| Type | Format | Example |
|---|---|---|
| Integer | As is | `5` |
| Real number | A decimal with enough digits to restore the original value (exponents are not used). Infinity and NaN are written as `inf` `-inf` `nan` (Tc574-8 / Tc603-1 and later) | `2.5`、`0.0000001` |
| String | `"..."` (`"` and control characters are escaped) | `"abc"` |
| Generic array | Separate elements with `:`. If there is one element, append `:IARRAY`; if empty, write `IARRAY:IARRAY` | `1:"b":2.5` |
| Hash (Tc600-3 and later) | Separate `key=value` pairs with `:`. If there is one element, append `:IHASH=IHASH`; if empty, write `IHASH=IHASH:IHASH=IHASH` | `"a"=1:"b"="x"` |
| VOID element, key, or value | `IVOID` | `"v"=IVOID` |
| Nested elements (Tc600-3 and later) | Enclose the array or hash format in `IARRAY{...}` / `IHASH{...}` | `"l"=IARRAY{1:2}` |

Examples of hashes and nested values in Tc600-3 and later:

```
h,"a"=1:"l"=IARRAY{1:2}:"n"=IHASH{"x"=1:"y"="s"},",",
v,IHASH{"k"=1:IHASH=IHASH}:IARRAY,",",
e,"e"=IHASH{IHASH=IHASH:IHASH=IHASH}:"ea"=IARRAY{IARRAY:IARRAY},",",
```

Nested values are written using the same rules, so they can be restored to their original values no matter how deeply nested they are.

The format for variables that do not contain hashes or nested values is the same as before Tc600-3. If you read a file saved with Tc600-3 or later using an older version, only variables that contain hashes or nested values will be corrupted ([Changes in 600](../other/changes-600.md#セーブファイルの互換性)).

## Compatibility
- YAYA: Supported since the initial version
- AYA: 5.8 and later
- Tc600-3: Supports saving hash and nested values
- Tc574-8 / Tc603-1: Real numbers are now saved with enough digits to restore their original values (previously, they were rounded to 6 decimal places, and infinity and NaN could not be read back)

## See Also
- RESTOREVAR
- SERIALIZEVAR
- DESERIALIZEVAR
