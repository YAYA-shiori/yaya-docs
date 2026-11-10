# PARSETOML
**Category:** 型取得/変換

## Signature
```
PARSETOML( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | TOML string |

## Returns
- On success: a hash converted from TOML
- On failure: empty (VOID)

## Description
Parses a TOML string and returns it as a hash. Value mappings are the same as for [FREADTOML](FREADTOML.md#値の対応).

Use [FREADTOML](FREADTOML.md) to read from a file.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| str is not a string | W0009 | 9 |
| Cannot parse as TOML | W0026 (also outputs the line number and cause) | 26 |

## Example
```
_t = PARSETOML("a = 1" + CHR(10) + "b.c = 'x'")
_t["a"]                     // 1
_t["b"]["c"]                // x

PARSETOML("a = 1" + CHR(10) + "a = 2")
// 空（警告 W0026 : line 2 : duplicate key : a）
```

## Compatibility
- YAYA: Tc602-5 and later

## See Also
- [FREADTOML](FREADTOML.md)
- [DUMPTOML](DUMPTOML.md)
- [PARSEJSON](PARSEJSON.md)
- [PARSEYAML](PARSEYAML.md)
