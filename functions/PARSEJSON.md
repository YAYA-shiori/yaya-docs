# PARSEJSON
**Category:** 型取得/変換

## Signature
```
PARSEJSON( str [, key ...] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | JSON の文字列 |
| key | 取り出すキー（省略可。いくつでも指定できる。Tc608-6 以降）。最上位がオブジェクトなら、そのキーの値だけを返す（[キーを指定して解析する](#キーを指定して解析する)）。文字列だけ |

## Returns
- 成功時: JSON を変換した値
- 失敗時: 空（VOID）

## Description
JSON の文字列を解析し、ハッシュ・配列などの値にして返す。値の対応やコメントの扱いは [FREADJSON](FREADJSON.md#値の対応) と同じ。

SAORI や外部から受け取った JSON の文字列を扱うときに使う。ファイルから読むときは [FREADJSON](FREADJSON.md) を使う。

### キーを指定して解析する
`key` を指定すると、最上位がオブジェクトのとき、そのキーの値だけをハッシュにして返す（Tc608-6 以降）。JSON の解析は全体に対して行うが、結果の変換（文字列の変換とハッシュの作成）を指定したキーだけで済ませるので、長い文字列や大きな入れ子を含む JSON から一部だけを使うときに速く、結果も小さくなる。

- キーは最上位のものだけ。`.` で下の階層を指すことはできない（`"a.b"` は、名前に `.` を含むキーを指す）
- JSON にないキーは、結果のハッシュにも作らない。値が `null` のキーは、全体を変換するときと同じく VOID の値で残る
- 最上位がオブジェクトでなければ、`key` は使わずに全体を変換する
- キーは配列で渡してもよい（関数の引数では、外側の配列が展開される）
- 1 行に 1 つの JSON が並ぶファイルを読むなら、[FREADJSONL](FREADJSONL.md) のほうが速い

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| str が文字列でない。key が文字列でない | W0009 | 9 |
| JSON として解析できない | W0026 | 26 |

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
- YAYA: Tc601-1以降
- Tc602-1: 小数点が `,` のロケール（ドイツ語など）の環境で、小数を含む JSON の解析に失敗していたのを修正
- Tc608-6: `str` の後ろに、取り出すキーを指定できるようにした

## See Also
- [FREADJSON](FREADJSON.md)
- [FREADJSONL](FREADJSONL.md)
- [DUMPJSON](DUMPJSON.md)
- [PARSEXML](PARSEXML.md)
