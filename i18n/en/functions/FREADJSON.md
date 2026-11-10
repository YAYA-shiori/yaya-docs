# FREADJSON
**Category:** ファイル操作

## Signature
```
FREADJSON( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path of the JSON file to read (a path relative to yaya.dll or an absolute path) |
| charset | Character encoding of the file (optional). Specify as a string (such as `"UTF-8"` or `"Shift_JIS"`. [Character encoding names](../grammar/11-character-encoding.md#文字コードの名前)) or a number. Defaults to UTF-8 |

## Returns
- On success: The value converted from JSON (see [Value mapping](#値の対応) below)
- On failure: Empty (VOID)

## Description
Reads and parses the entire JSON file, then returns it as a value such as a hash or array. It does not need to be opened with [FOPEN](FOPEN.md).

JSON parsing uses [parson](https://github.com/kgabis/parson).

- A UTF-8 BOM at the beginning of the file is ignored
- Comments using `/* */` and `//` are allowed (although they are outside the JSON specification, they are permitted for use in configuration files and similar)
- The top level does not have to be an object or array (files containing only `123` or `"abc"` can also be read)

### Value mapping

| JSON | YAYA |
|------|------|
| Object | Hash |
| Array | Generic array (can be nested, with arrays or hashes as elements) |
| String | String |
| Number (integer value) | Integer |
| Number (other values) | Real number |
| `true` / `false` | Integer 1 / 0 |
| `null` | Empty (VOID) |

- Numbers are parsed internally as real numbers, so a value such as `1.0` becomes an integer if its value is an integer. Integers larger than 2^53 may contain rounding errors. Values outside the integer range (from -2^63 inclusive to 2^63 exclusive) become real numbers
- The order of object keys is not preserved. Keys are ordered as hash keys are (numbers < strings; see [HASH_KEYS](HASH_KEYS.md))
- Keys that YAYA hashes do not consider equivalent, such as `"1"` and `"01"`, remain separate keys. A key that is a canonical integer string, such as `"1"`, can be accessed with either `h[1]` or `h["1"]`
- Keys with `null` values remain in the hash. [HASH_EXIST](HASH_EXIST.md) returns 1

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| path is not a string | W0009 | 9 |
| charset is invalid | W0012 / W0009 | 12 / 9 |
| Cannot open the file | W0025 | 25 |
| Cannot parse as JSON | W0026 | 26 |

## Example
data.json:
```json
{
  "name": "さくら",
  "age": 17,
  "tags": ["ghost", "shell"],
  "profile": { "height": 158.5, "visible": true, "memo": null }
}
```

```
_j = FREADJSON("data.json")
_j["name"]                  // さくら
_j["tags"][1]               // shell
_j["profile"]["height"]     // 実数の 158.5
_j["profile"]["visible"]    // 1

foreach _j["tags"]; _t {
    // _t に "ghost"、"shell" が順に入る
}
```

## Compatibility
- YAYA: Since Tc601-1
- Tc602-1: Fixed a failure to parse JSON containing decimals in locales that use `,` as the decimal separator (such as German)
- Tc603-1: Passing an unknown character encoding name now causes a failure with warning W0012 (previously, no warning was issued and the OS default was used)

## See Also
- [PARSEJSON](PARSEJSON.md)
- [FWRITEJSON](FWRITEJSON.md)
- [FREADXML](FREADXML.md)
- [Nested values and multidimensional assignment](../grammar/13-nesting.md)
