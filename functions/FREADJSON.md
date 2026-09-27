# FREADJSON
**Category:** ファイル操作

## Signature
```
FREADJSON( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 読み込む JSON ファイルのパス（yaya.dll からの相対パス、または絶対パス） |
| charset | ファイルの文字コード（省略可）。文字列（`"UTF-8"` `"Shift_JIS"` など）または数値で指定する。省略時は UTF-8 |

## Returns
- 成功時: JSON を変換した値（下記の [値の対応](#値の対応)）
- 失敗時: 空（VOID）

## Description
JSON ファイルを丸ごと読み込んで解析し、ハッシュ・配列などの値にして返す。[FOPEN](FOPEN.md) で開いておく必要はない。

JSON の解析には [parson](https://github.com/kgabis/parson) を使っている。

- 先頭の UTF-8 の BOM は無視する
- `/* */` と `//` のコメントを書ける（JSON の規格外だが、設定ファイルなどで使えるよう許している）
- 最上位はオブジェクトや配列でなくてもよい（`123` や `"abc"` だけのファイルも読める）

### 値の対応

| JSON | YAYA |
|------|------|
| オブジェクト | ハッシュ |
| 配列 | 汎用配列（要素に配列やハッシュを含む入れ子になる） |
| 文字列 | 文字列 |
| 数値（整数の値） | 整数 |
| 数値（それ以外） | 実数 |
| `true` / `false` | 整数 1 / 0 |
| `null` | 空（VOID） |

- 数値は内部で実数として解析するため、`1.0` のように小数点があっても値が整数なら整数になる。また、2^53 を超える整数は誤差を含むことがある。整数の範囲（-2^63 以上 2^63 未満）を超える値は実数になる
- オブジェクトのキーの並びは保たれない。ハッシュのキーの順（数値 < 文字列）になる（[HASH_KEYS](HASH_KEYS.md) を参照）
- `"1"` と `"01"` のように、YAYA のハッシュで同じキーとみなされないものは別のキーのまま残る。`"1"` のような正規形の整数文字列のキーは `h[1]` でも `h["1"]` でも引ける
- `null` の値のキーもハッシュに残る。[HASH_EXIST](HASH_EXIST.md) は 1 を返す

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| path が文字列でない | W0009 | 9 |
| charset が不正 | W0012 / W0009 | 12 / 9 |
| ファイルを開けない | W0025 | 25 |
| JSON として解析できない | W0026 | 26 |

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
- YAYA: Tc601-1以降
- Tc602-1: 小数点が `,` のロケール（ドイツ語など）の環境で、小数を含む JSON の解析に失敗していたのを修正

## See Also
- [PARSEJSON](PARSEJSON.md)
- [FWRITEJSON](FWRITEJSON.md)
- [FREADXML](FREADXML.md)
- [値の入れ子と多次元代入](../grammar/13-nesting.md)
