# PARSEYAML
**Category:** 型取得/変換

## Signature
```
PARSEYAML( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | YAML string |

## Returns
- On success: the value converted from YAML
- On failure: empty (VOID)

## Description
Parses a YAML string and returns it as a hash, array, or other value. Supported syntax and value mappings are the same as for [FREADYAML](FREADYAML.md#対応している書き方).

Use [FREADYAML](FREADYAML.md) to read from a file.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| str is not a string | W0009 | 9 |
| Cannot parse as YAML, or syntax is unsupported | W0026 (also outputs the line number and cause) | 26 |

## Example
```
_y = PARSEYAML("{name: さくら, tags: [ghost, shell]}")
_y["name"]                  // さくら
_y["tags"][1]               // shell

PARSEYAML("- 1" + CHR(10) + "- 0x10" + CHR(10) + "- yes" + CHR(10) + "- '007'")
// 整数 1、整数 16、文字列 yes、文字列 007 の汎用配列

PARSEYAML("a: [1")          // 空（警告 W0026）
```

## Compatibility
- YAYA: Tc602-5 and later

## See Also
- [FREADYAML](FREADYAML.md)
- [DUMPYAML](DUMPYAML.md)
- [PARSEJSON](PARSEJSON.md)
- [PARSETOML](PARSETOML.md)
