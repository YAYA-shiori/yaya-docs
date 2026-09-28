# FWRITEYAML
**Category:** ファイル操作

## Signature
```
FWRITEYAML( path, value [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 書き込むファイルのパス（yaya.dll からの相対パス、または絶対パス） |
| value | YAML にする値。ハッシュや配列（入れ子を含む）も1つの引数として渡せる |
| charset | ファイルの文字コード（省略可）。文字列（`"UTF-8"` `"Shift_JIS"` など。[文字コードの名前](../grammar/11-character-encoding.md#文字コードの名前)）または数値で指定する。省略時、または空文字列のときは UTF-8（BOM なし） |
| pretty | 1 ならブロック形式、0 ならフロー形式の1行にする。省略時は 1 |

## Returns
- 成功時: 1
- 失敗時: 0

## Description
値を YAML にしてファイルに書き込む。ファイルが既にあれば上書きする。[FOPEN](FOPEN.md) で開いておく必要はない。

値の対応と整形の形は [DUMPYAML](DUMPYAML.md#値の対応) と同じ。ブロック形式のときはファイルの末尾に改行（LF）を付ける。

書き込んだファイルは [FREADYAML](FREADYAML.md) で読み戻せる（UTF-8 以外で書いたときは同じ charset を指定する）。

charset で表せない文字（Shift_JIS での絵文字など）を含む文字列は、クォートしない形やブロックスカラー（`|`）にはせず、`"..."` で囲んでその文字を `\uXXXX`（BMP の外の文字は `\U0001F600` のような8桁）で書く。キーも同じ。読み戻すと元の文字に戻る。

ディレクトリは作らない。存在しないディレクトリの中には書き込めない。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数が足りない | W0008 | 8 |
| path が文字列でない | W0009 | 9 |
| charset が不正 | W0012 / W0009 | 12 / 9 |
| ファイルを開けない | W0025 | 25 |
| 文字コードの変換そのものに失敗した | W0027 | 27 |
| 書き込みに失敗した | W0013 | 13 |

## Example
```
_conf = IHASH()
_conf["volume"] = 80
_conf["friends"] = ("うにゅう", "まゆら")
_conf["memo"] = "1行目" + CHR(10) + "2行目"

FWRITEYAML("config.yaml", _conf)
// config.yaml:
// friends:
//   - うにゅう
//   - まゆら
// memo: |-
//   1行目
//   2行目
// volume: 80

FWRITEYAML("config.flow.yaml", _conf, "", 0)
// {friends: [うにゅう, まゆら], memo: "1行目\n2行目", volume: 80}
```

## Compatibility
- YAYA: Tc602-5以降
- Tc603-1: charset で表せない文字を、黙って `?` にせず、形式のエスケープで書くようにした。知らない文字コードの名前を渡すと警告 W0012 を出して失敗するようにした（それまでは警告を出さずに OS デフォルトとして扱っていた）

## See Also
- [DUMPYAML](DUMPYAML.md)
- [FREADYAML](FREADYAML.md)
- [FWRITEJSON](FWRITEJSON.md)
- [FWRITETOML](FWRITETOML.md)
