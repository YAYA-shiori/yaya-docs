# FWRITETOML
**Category:** ファイル操作

## Signature
```
FWRITETOML( path, value [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 書き込むファイルのパス（yaya.dll からの相対パス、または絶対パス） |
| value | TOML にするハッシュ（入れ子を含む） |
| charset | ファイルの文字コード（省略可）。文字列（`"UTF-8"` `"Shift_JIS"` など）または数値で指定する。省略時、または空文字列のときは UTF-8（BOM なし）。TOML の規格では UTF-8 と決まっているので、ふつうは省略する |
| pretty | 1 なら `[表]` の見出しを使って整形する、0 なら最上位のキー1つにつき1行にする。省略時は 1 |

## Returns
- 成功時: 1
- 失敗時: 0

## Description
ハッシュを TOML にしてファイルに書き込む。ファイルが既にあれば上書きする。[FOPEN](FOPEN.md) で開いておく必要はない。

値の対応と整形の形は [DUMPTOML](DUMPTOML.md#値の対応) と同じ。

書き込んだファイルは [FREADTOML](FREADTOML.md) で読み戻せる。

ディレクトリは作らない。存在しないディレクトリの中には書き込めない。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数が足りない | W0008 | 8 |
| path が文字列でない | W0009 | 9 |
| charset が不正 | W0012 / W0009 | 12 / 9 |
| value がハッシュでない、配列の要素に空（VOID）がある | W0027（原因も出力する） | 27 |
| ファイルを開けない | W0025 | 25 |
| 文字コードを変換できない | W0027 | 27 |
| 書き込みに失敗した | W0013 | 13 |

## Example
```
_conf = IHASH()
_conf["volume"] = 80
_conf["friends"] = ("うにゅう", "まゆら")
_conf["memo"] = "1行目" + CHR(10) + "2行目"

FWRITETOML("config.toml", _conf)
// config.toml:
// friends = ["うにゅう", "まゆら"]
// memo = """
// 1行目
// 2行目"""
// volume = 80
```

## Compatibility
- YAYA: Tc602-5以降

## See Also
- [DUMPTOML](DUMPTOML.md)
- [FREADTOML](FREADTOML.md)
- [FWRITEJSON](FWRITEJSON.md)
- [FWRITEYAML](FWRITEYAML.md)
