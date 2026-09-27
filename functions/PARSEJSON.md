# PARSEJSON
**Category:** 型取得/変換

## Signature
```
PARSEJSON( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | JSON の文字列 |

## Returns
- 成功時: JSON を変換した値
- 失敗時: 空（VOID）

## Description
JSON の文字列を解析し、ハッシュ・配列などの値にして返す。値の対応やコメントの扱いは [FREADJSON](FREADJSON.md#値の対応) と同じ。

SAORI や外部から受け取った JSON の文字列を扱うときに使う。ファイルから読むときは [FREADJSON](FREADJSON.md) を使う。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| str が文字列でない | W0009 | 9 |
| JSON として解析できない | W0026 | 26 |

## Example
```
_j = PARSEJSON('{"result": [{"id": 1, "text": "こんにちは"}]}')
_j["result"][0]["text"]     // こんにちは
_j["result"][0]["id"]       // 1

PARSEJSON('[1, 2.5, "a"]')  // 整数 1、実数 2.5、文字列 a の汎用配列
PARSEJSON('{')              // 空（警告 W0026）
```

## Compatibility
- YAYA: Tc601-1以降

## See Also
- [FREADJSON](FREADJSON.md)
- [PARSEXML](PARSEXML.md)
