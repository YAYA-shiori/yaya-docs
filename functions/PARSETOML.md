# PARSETOML
**Category:** 型取得/変換

## Signature
```
PARSETOML( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | TOML の文字列 |

## Returns
- 成功時: TOML を変換したハッシュ
- 失敗時: 空（VOID）

## Description
TOML の文字列を解析し、ハッシュにして返す。値の対応は [FREADTOML](FREADTOML.md#値の対応) と同じ。

ファイルから読むときは [FREADTOML](FREADTOML.md) を使う。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| str が文字列でない | W0009 | 9 |
| TOML として解析できない | W0026（行番号と原因も出力する） | 26 |

## Example
```
_t = PARSETOML("a = 1" + CHR(10) + "b.c = 'x'")
_t["a"]                     // 1
_t["b"]["c"]                // x

PARSETOML("a = 1" + CHR(10) + "a = 2")
// 空（警告 W0026 : line 2 : duplicate key : a）
```

## Compatibility
- YAYA: Tc602-5以降

## See Also
- [FREADTOML](FREADTOML.md)
- [DUMPTOML](DUMPTOML.md)
- [PARSEJSON](PARSEJSON.md)
- [PARSEYAML](PARSEYAML.md)
