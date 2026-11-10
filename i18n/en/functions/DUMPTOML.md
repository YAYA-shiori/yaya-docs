# DUMPTOML
**Category:** 型取得/変換

## Signature
```
DUMPTOML( value [, pretty] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| value | The hash to convert to TOML (including nested hashes). The top level of TOML is a table, so you cannot pass anything other than a hash |
| pretty | If 1, format the output using `[table]` headings; if 0, output one line for each top-level key. Defaults to 1 |

## Returns
- On success: a TOML string
- On failure or when no argument is given: an empty string

## Description
Converts a hash to a TOML string and returns it. This is the reverse conversion of [PARSETOML](PARSETOML.md).

Unlike [DUMPJSON](DUMPJSON.md) / [DUMPXML](DUMPXML.md), the default for pretty is to format the output (1).

### Value mappings

| YAYA | TOML |
|------|------|
| Hash | Table. Keys containing only alphanumeric characters, `_`, and `-` are written as-is; other keys are written as `"..."`. The order follows the hash key order |
| Generic array containing only hashes | Array of tables (when pretty is 1, uses `[[name]]`) |
| Generic array | Array |
| Integer | Integer. 64-bit integers are written without loss of precision |
| Real number | Real number. Always includes a decimal point or exponent (`1.0`, `0.1`, `1e+300`). NaN is `nan`; infinity is `inf` / `-inf` |
| String | String (see below) |
| Empty (VOID) | Not written (TOML has no null, so the key is omitted) |

- Integer values 1 / 0 are written as `1` / `0`. They are not written as `true` / `false`
- Date-time strings (read by [FREADTOML](FREADTOML.md)) are also written as strings using `"..."`.
- If an array contains an empty (VOID) element, it cannot be represented, so error W0027 is raised
- The decimal point is always `.` regardless of the locale

Strings are usually written as `"..."`, with `"` `\` and control characters escaped. Strings that contain `\` but no `'` or newline (such as Windows paths) are written as `'...'` without escaping for readability.

### Formatting (when pretty is 1)

- Write the table's keys and values, then tables at lower levels (`[a.b]`), then arrays of tables (`[[a.c]]`), in that order; insert a blank line between tables
- Omit the heading for a table that has no keys or values and contains only tables at lower levels (the table `a` is also defined by `[a.b]` alone)
- Strings containing newlines are written as multiline `"""..."""` strings
- Arrays longer than 80 characters, and arrays containing arrays or hashes, are written with one element per line (indented by four spaces, with a comma after each element)
- Use LF for newlines, and add a newline after the last line as well

When pretty is 0, output one line for each top-level key. Lower-level hashes are written as inline tables (`{ k = v }`), and arrays of tables are written as arrays of inline tables.

Reading the result back with [PARSETOML](PARSETOML.md) restores the original values, except for omitted empty values.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No argument | W0008 | 8 |
| value is not a hash, or an array contains an empty (VOID) element | W0027 (also outputs the cause) | 27 |

## Example
```
_n = IHASH()
_n["title"] = "設定"
_n["ghost"] = IHASH("name", "さくら", "age", 17)
_n["ghost"]["shell"] = IHASH("name", "master")

DUMPTOML(_n)
// title = "設定"
//
// [ghost]
// age = 17
// name = "さくら"
//
// [ghost.shell]
// name = "master"

DUMPTOML(_n, 0)
// ghost = { age = 17, name = "さくら", shell = { name = "master" } }
// title = "設定"

DUMPTOML(("a", 1))          // 空文字列（警告 W0027）
```

## Compatibility
- YAYA: Tc602-5 and later

## See Also
- [FWRITETOML](FWRITETOML.md)
- [PARSETOML](PARSETOML.md)
- [DUMPJSON](DUMPJSON.md)
- [DUMPYAML](DUMPYAML.md)
