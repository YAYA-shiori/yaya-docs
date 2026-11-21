# FREADJSON
**Category:** ファイル操作

## Signature
```
FREADJSON( path [, charset [, key ...]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path to the JSON file to read (relative to yaya.dll, or absolute) |
| charset | Character encoding of the file (optional). Specify a string (such as `"UTF-8"` or `"Shift_JIS"`; see [Character encoding names](../grammar/11-character-encoding.md#文字コードの名前)) or a number. Defaults to UTF-8 |
| key | Key to retrieve (optional; any number can be specified; Tc608-6 and later). If the top-level value is an object, returns only the values of these keys ([Reading specified keys](#キーを指定して読む)). Strings only. When specifying keys, also specify `charset` (such as `"UTF-8"`) |

## Returns
- On success: The converted JSON value (see [Value mapping](#値の対応) below)
- On failure: Empty (VOID)

## Description
Reads and parses an entire JSON file, then returns its value as a hash, array, or other value. There is no need to open it with [FOPEN](FOPEN.md).

[parson](https://github.com/kgabis/parson) is used to parse JSON.

- An initial UTF-8 BOM is ignored
- `/* */` and `//` comments are allowed (they are not part of the JSON standard, but are permitted for use in configuration files and similar files)
- The top-level value does not have to be an object or array (files containing only `123` or `"abc"`, for example, can also be read)

### Value mapping

| JSON | YAYA |
|------|------|
| Object | Hash |
| Array | Generic array (nested arrays and hashes can appear as elements) |
| String | String |
| Number (integer value) | Integer |
| Number (otherwise) | Real number |
| `true` / `false` | Integer 1 / 0 |
| `null` | Empty (VOID) |

- Numbers are parsed internally as real numbers, so a value is converted to an integer if it is integral, even if it has a decimal point, as in `1.0`. Integers greater than 2^53 may also contain rounding errors. Values outside the integer range (-2^63 inclusive to 2^63 exclusive) become real numbers
- The order of object keys is not preserved. Keys follow hash key order (numbers < strings) (see [HASH_KEYS](HASH_KEYS.md))
- Keys such as `"1"` and `"01"`, which are not considered the same key in a YAYA hash, remain separate. A key that is a canonical integer string, such as `"1"`, can be accessed with either `h[1]` or `h["1"]`
- Keys with `null` values also remain in the hash. [HASH_EXIST](HASH_EXIST.md) returns 1

### Reading specified keys
When `key` is specified and the top-level value is an object, only the values of those keys are returned in a hash (Tc608-6 and later). The entire file is parsed as JSON, but only the specified keys are converted (string conversion and hash creation), making this faster and producing a smaller result when only part of a large JSON file is needed.

- Only top-level keys can be specified. `.` cannot be used to refer to lower levels (`"a.b"` refers to a key whose name contains `.`)
- Keys absent from the file are not created in the resulting hash. Keys with `null` values remain with a VOID value, as when converting the entire file
- If the top-level value is not an object, the entire value is converted without using `key`
- Keys may also be passed as an array (the outer array is expanded in function arguments)

### Errors
| Condition | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| path is not a string. key is not a string | W0009 | 9 |
| Invalid charset | W0012 / W0009 | 12 / 9 |
| Cannot open file | W0025 | 25 |
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

_j = FREADJSON("data.json", "UTF-8", "name", "tags")   // Tc608-6 以降。このキーだけのハッシュ
_j["name"]                  // さくら
HASH_EXIST("age", _j)       // 0（取り出していない）
```

## Compatibility
- YAYA: Tc601-1 and later
- Tc602-1: Fixed a failure to parse JSON containing decimals in locales where the decimal separator is `,` (such as German)
- Tc603-1: Changed unknown character encoding names to cause a failure with warning W0012 (previously they were treated as the OS default without a warning)
- Tc608-6: Added support for specifying keys to retrieve after `charset`

## See Also
- [FREADJSONL](FREADJSONL.md)
- [PARSEJSON](PARSEJSON.md)
- [FWRITEJSON](FWRITEJSON.md)
- [FREADXML](FREADXML.md)
- [Nested values and multidimensional assignment](../grammar/13-nesting.md)
