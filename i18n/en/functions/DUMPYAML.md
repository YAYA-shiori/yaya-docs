# DUMPYAML
**Category:** 型取得/変換

## Signature
```
DUMPYAML( value [, pretty] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| value | The value to convert to YAML. A hash or array (including nested ones) can be passed as a single argument |
| pretty | If 1, use block style (a human-readable format that represents structure with indentation); if 0, use a single line in flow style. Defaults to 1 |

## Returns
- On success: a YAML string
- If no arguments are provided: an empty string

## Description
Converts the value to a YAML string and returns it. This is the reverse of [PARSEYAML](PARSEYAML.md).

Unlike [DUMPJSON](DUMPJSON.md) and [DUMPXML](DUMPXML.md), the output is formatted by default (1).

### Value mappings

| YAYA | YAML |
|------|------|
| Hash | Mapping. Keys are converted to strings (`1` becomes `"1"`). The order is the order of the hash keys |
| Generic array | Sequence |
| Integer | Integer. 64-bit integers are written without loss of precision |
| Real number | Real number. A decimal point is always included (`1.0`, `0.1`, `1.0e+300`). NaN is written as `.nan`, and infinity as `.inf` / `-.inf` |
| String | String (see below) |
| Empty (VOID) | `null` |

- Integer values 1 / 0 become `1` / `0`. They do not become `true` / `false`
- The decimal point is always `.` regardless of the locale

Strings that can be written as-is and read back as the same string are written without quotes; other strings are enclosed in `"..."`. The following are written as `"..."`:

- Values that would be read as numbers, booleans, or null (`"123"` `"1.5"` `"true"` `"null"` `"~"`)
- Values that may be read as numbers or booleans by other implementations (YAML 1.1) (`"yes"` `"no"` `"on"` `"off"` `"0x1F"` `"2001-12-14"` `"12:30"`)
- Empty strings, strings that start or end with whitespace, and strings that start with a symbol (`- ? : , [ ] { } # & * ! | > ' " % @` and `` ` ``)
- Strings containing `: ` or ` #`, or control characters such as tabs

Inside `"..."`, only `"` `\` and control characters are escaped (a newline becomes `\n`). Non-ASCII characters, such as Japanese characters, are written as-is.

### Formatting (when pretty is 1)

- Indents with two spaces, uses LF for line breaks, and adds a newline after the last line
- Sequences are indented under their keys and listed with `- `. Hashes and arrays used as sequence items are written after `- `
- Empty arrays and hashes are written as `[]` / `{}`
- Strings containing newlines use block scalars (`|`). Strings without a trailing newline use `|-`; those with two or more trailing newlines use `|+`. However, strings whose first line starts with whitespace, that contain a line consisting only of whitespace, or that contain control characters such as CR are written as `"..."`

When pretty is 0, the output is a single line in flow style (for example, `{a: 1, b: [x, y]}`), with no trailing newline.

Reading the output back with [PARSEYAML](PARSEYAML.md) restores the original value (in either format).

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |

## Example
```
_h = IHASH()
_h["name"] = "さくら"
_h["tags"] = ("ghost", "shell")
_h["height"] = 158.5

DUMPYAML(_h)
// height: 158.5
// name: さくら
// tags:
//   - ghost
//   - shell

DUMPYAML(_h, 0)
// {height: 158.5, name: さくら, tags: [ghost, shell]}

DUMPYAML(("a", 1))          // "- a" + 改行 + "- 1" + 改行
DUMPYAML("123", 0)          // "123"（数値と区別するためクォートされる）
DUMPYAML(未定義の変数, 0)    // null
```

## Compatibility
- YAYA: Supported from the first release

## See Also
- [FWRITEYAML](FWRITEYAML.md)
- [PARSEYAML](PARSEYAML.md)
- [DUMPJSON](DUMPJSON.md)
- [DUMPTOML](DUMPTOML.md)
