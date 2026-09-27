# PARSEYAML
**Category:** 型取得/変換

## Signature
```
PARSEYAML( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | YAML の文字列 |

## Returns
- 成功時: YAML を変換した値
- 失敗時: 空（VOID）

## Description
YAML の文字列を解析し、ハッシュ・配列などの値にして返す。対応している書き方と値の対応は [FREADYAML](FREADYAML.md#対応している書き方) と同じ。

ファイルから読むときは [FREADYAML](FREADYAML.md) を使う。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| str が文字列でない | W0009 | 9 |
| YAML として解析できない、対応していない書き方 | W0026（行番号と原因も出力する） | 26 |

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
- YAYA: Tc602-5以降

## See Also
- [FREADYAML](FREADYAML.md)
- [DUMPYAML](DUMPYAML.md)
- [PARSEJSON](PARSEJSON.md)
- [PARSETOML](PARSETOML.md)
