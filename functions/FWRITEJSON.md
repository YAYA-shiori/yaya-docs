# FWRITEJSON
**Category:** ファイル操作

## Signature
```
FWRITEJSON( path, value [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 書き込むファイルのパス（yaya.dll からの相対パス、または絶対パス） |
| value | JSON にする値。ハッシュや配列（入れ子を含む）も1つの引数として渡せる |
| charset | ファイルの文字コード（省略可）。文字列（`"UTF-8"` `"Shift_JIS"` など）または数値で指定する。省略時、または空文字列のときは UTF-8（BOM なし） |
| pretty | 1 なら改行とインデントを入れて整形する。省略時は 1（整形する） |

## Returns
- 成功時: 1
- 失敗時: 0

## Description
値を JSON にしてファイルに書き込む。ファイルが既にあれば上書きする。[FOPEN](FOPEN.md) で開いておく必要はない。

値の対応と整形の形は [DUMPJSON](DUMPJSON.md#値の対応) と同じ。整形したときはファイルの末尾に改行（LF）を付ける。

書き込んだファイルは [FREADJSON](FREADJSON.md) で読み戻せる（UTF-8 以外で書いたときは同じ charset を指定する）。

ディレクトリは作らない。存在しないディレクトリの中には書き込めない。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数が足りない | W0008 | 8 |
| path が文字列でない | W0009 | 9 |
| charset が不正 | W0012 / W0009 | 12 / 9 |
| ファイルを開けない | W0025 | 25 |
| 文字コードを変換できない | W0027 | 27 |
| 書き込みに失敗した | W0013 | 13 |

## Example
```
_conf = IHASH()
_conf["volume"] = 80
_conf["friends"] = ("うにゅう", "まゆら")

FWRITEJSON("config.json", _conf)
// config.json:
// {
//     "friends": [
//         "うにゅう",
//         "まゆら"
//     ],
//     "volume": 80
// }

FWRITEJSON("config.min.json", _conf, "", 0)   // UTF-8 で1行に
```

## Compatibility
- YAYA: Tc602-1以降

## See Also
- [DUMPJSON](DUMPJSON.md)
- [FREADJSON](FREADJSON.md)
- [FWRITEXML](FWRITEXML.md)
