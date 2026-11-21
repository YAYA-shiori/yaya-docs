# PARSEJSON
**Category:** 型取得/変換

## Signature
```
PARSEJSON( str [, key ...] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | JSON string |
| key | Key to extract (optional; any number may be specified; Tc608-6 or later). If the top level is an object, returns only the values of the specified keys ([Parsing with specified keys](#キーを指定して解析する)). Strings only |

## Returns
- On success: The value converted from JSON
- On failure: Empty (VOID)

## Description
Parses a JSON string and returns its value as a hash, array, or other value. Value mappings and comment handling are the same as for [FREADJSON](FREADJSON.md#値の対応).

Use this to handle JSON strings received from SAORI or external sources. To read from a file, use [FREADJSON](FREADJSON.md).

### Parsing with specified keys
When `key` is specified and the top level is an object, returns a hash containing only the values of those keys (Tc608-6 or later). The entire JSON is parsed, but only the specified keys are converted (string conversion and hash creation). This is faster and produces a smaller result when using only part of JSON containing long strings or large nested structures.

- Only top-level keys can be specified. `.` cannot be used to address lower levels (`"a.b"` refers to a key whose name contains `.`)
- Keys absent from the JSON are not created in the resulting hash. Keys with a `null` value remain with a VOID value, as when converting the entire JSON
- If the top level is not an object, the entire JSON is converted without using `key`
- Keys may be passed as an array (the outer array is expanded in function arguments)
- To read a file containing one JSON value per line, [FREADJSONL](FREADJSONL.md) is faster

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| str is not a string, or key is not a string | W0009 | 9 |
| Cannot be parsed as JSON | W0026 | 26 |

## Example
```
_j = PARSEJSON('{"result": [{"id": 1, "text": "こんにちは"}]}')
_j["result"][0]["text"]     // こんにちは
_j["result"][0]["id"]       // 1

PARSEJSON('[1, 2.5, "a"]')  // 整数 1、実数 2.5、文字列 a の汎用配列
PARSEJSON('{')              // 空（警告 W0026）

_j = PARSEJSON('{"a": 1, "b": [1, 2], "c": {"d": 4}}', "a", "c")   // Tc608-6 以降。このキーだけのハッシュ
_j["c"]["d"]                // 4
HASH_EXIST("b", _j)         // 0（取り出していない）
```

## Compatibility
- YAYA: Tc601-1 or later
- Tc602-1: Fixed a failure to parse JSON containing decimals in locales that use `,` as the decimal separator, such as German
- Tc608-6: Added the ability to specify keys to extract after `str`

## See Also
- [FREADJSON](FREADJSON.md)
- [FREADJSONL](FREADJSONL.md)
- [DUMPJSON](DUMPJSON.md)
- [PARSEXML](PARSEXML.md)
