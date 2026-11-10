# PARSEJSON
**Category:** 型取得/変換

## Signature
```
PARSEJSON( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | JSON string |

## Returns
- On success: the value converted from JSON
- On failure: empty (VOID)

## Description
Parses a JSON string and returns it as a hash, array, or other value. Supported value mappings and comment handling are the same as for [FREADJSON](FREADJSON.md#値の対応).

Use this to process JSON strings received from a SAORI or another external source. Use [FREADJSON](FREADJSON.md) to read from a file.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| str is not a string | W0009 | 9 |
| Cannot parse as JSON | W0026 | 26 |

## Example
```
_j = PARSEJSON('{"result": [{"id": 1, "text": "こんにちは"}]}')
_j["result"][0]["text"]     // こんにちは
_j["result"][0]["id"]       // 1

PARSEJSON('[1, 2.5, "a"]')  // 整数 1、実数 2.5、文字列 a の汎用配列
PARSEJSON('{')              // 空（警告 W0026）
```

## Compatibility
- YAYA: Tc601-1 and later
- Tc602-1: Fixed a failure to parse JSON containing decimal numbers in environments with a locale that uses `,` as the decimal separator (such as German)

## See Also
- [FREADJSON](FREADJSON.md)
- [DUMPJSON](DUMPJSON.md)
- [PARSEXML](PARSEXML.md)
