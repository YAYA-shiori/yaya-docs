# FREADTOML
**Category:** ファイル操作

## Signature
```
FREADTOML( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 読み込む TOML ファイルのパス（yaya.dll からの相対パス、または絶対パス） |
| charset | ファイルの文字コード（省略可）。文字列（`"UTF-8"` `"Shift_JIS"` など）または数値で指定する。省略時は UTF-8（TOML の規格では UTF-8 と決まっている） |

## Returns
- 成功時: TOML を変換したハッシュ（下記の [値の対応](#値の対応)）
- 失敗時: 空（VOID）

## Description
TOML ファイルを丸ごと読み込んで解析し、ハッシュにして返す。[FOPEN](FOPEN.md) で開いておく必要はない。

TOML の解析は YAYA が自前で行う。[TOML v1.0.0](https://toml.io/ja/v1.0.0) に対応している。v1.1 で加わった、インライン表の中の改行と末尾のカンマ、`\e` `\xHH` のエスケープも受け付ける。

- 先頭の UTF-8 の BOM は無視する。改行は CRLF / LF のどちらでもよい
- 最上位は常にハッシュになる。空のファイルや、コメントだけのファイルは空のハッシュになる
- 同じキーや表を2回定義する、ドットのキーで作った表を `[表]` で定義し直す、インライン表に後から足す、などの規格で禁じられていることはエラーにする

### 値の対応

| TOML | YAYA |
|------|------|
| 表（`[table]`・インライン表 `{ }`・ドットのキー `a.b = 1`） | ハッシュ |
| 表の配列（`[[array]]`） | ハッシュの汎用配列 |
| 配列 | 汎用配列（要素に配列やハッシュを含む入れ子になる） |
| 文字列（`"..."` `'...'` `"""..."""` `'''...'''`） | 文字列 |
| 整数（`42` `1_000` `0xDEAD` `0o755` `0b1101`） | 整数 |
| 実数（`3.14` `5e+22` `inf` `nan`） | 実数 |
| `true` / `false` | 整数 1 / 0 |
| 日時（`1979-05-27T07:32:00Z`、`1979-05-27`、`07:32:00` など） | 書かれたとおりの文字列 |

- 整数の範囲（-2^63 以上 2^63 未満）を超える整数はエラーにする
- キーの並びは保たれない。ハッシュのキーの順になる（[HASH_KEYS](HASH_KEYS.md) を参照）

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| path が文字列でない | W0009 | 9 |
| charset が不正 | W0012 / W0009 | 12 / 9 |
| ファイルを開けない | W0025 | 25 |
| TOML として解析できない | W0026（行番号と原因も出力する） | 26 |

## Example
config.toml:
```toml
# ゴーストの設定
title = "設定"
updated = 2026-09-27T12:00:00+09:00

[ghost]
name = "さくら"
age = 17
visible = true
tags = ["ghost", "shell"]
path = 'C:\ssp\ghost'

[[friends]]
name = "うにゅう"

[[friends]]
name = "まゆら"
```

```
_t = FREADTOML("config.toml")
_t["title"]                 // 設定
_t["updated"]               // 文字列の 2026-09-27T12:00:00+09:00
_t["ghost"]["name"]         // さくら
_t["ghost"]["visible"]      // 1
_t["ghost"]["tags"][1]      // shell
_t["ghost"]["path"]         // C:\ssp\ghost
_t["friends"][1]["name"]    // まゆら

foreach _t["friends"]; _f {
    // _f に {name: うにゅう}、{name: まゆら} のハッシュが順に入る
}
```

## Compatibility
- YAYA: Tc602-5以降

## See Also
- [PARSETOML](PARSETOML.md)
- [FWRITETOML](FWRITETOML.md)
- [FREADJSON](FREADJSON.md)
- [FREADYAML](FREADYAML.md)
- [ハッシュと値の入れ子](../grammar/12-hash.md)
