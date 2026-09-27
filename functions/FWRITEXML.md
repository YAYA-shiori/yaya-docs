# FWRITEXML
**Category:** ファイル操作

## Signature
```
FWRITEXML( path, element [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 書き込むファイルのパス（yaya.dll からの相対パス、または絶対パス） |
| element | ルート要素を表すハッシュ（[FREADXML](FREADXML.md#要素の形) が返すのと同じ形） |
| charset | ファイルの文字コード（省略可）。文字列（`"UTF-8"` `"Shift_JIS"` など）または数値で指定する。省略時、または空文字列のときは UTF-8（BOM なし） |
| pretty | 1 なら改行とインデントを入れて整形する。省略時は 1（整形する） |

## Returns
- 成功時: 1
- 失敗時: 0

## Description
要素のハッシュを XML にしてファイルに書き込む。ファイルが既にあれば上書きする。[FOPEN](FOPEN.md) で開いておく必要はない。

要素のハッシュの形、エスケープ、整形の形は [DUMPXML](DUMPXML.md) と同じ。先頭には charset に合わせた XML 宣言を付ける。

| charset | XML 宣言の encoding |
|---------|------|
| UTF-8（省略時） | `UTF-8` |
| Shift_JIS | `Shift_JIS` |
| EUC-JP | `EUC-JP` |
| ISO-2022-JP | `ISO-2022-JP` |
| BIG5 | `Big5` |
| GB2312 | `GB2312` |
| EUC-KR | `EUC-KR` |
| default（OS の文字コード） | OS のコードページから決める（932 なら `Shift_JIS`） |

書き込んだファイルは、XML 宣言の encoding を見るので、[FREADXML](FREADXML.md) で charset を指定せずに読み戻せる。

ディレクトリは作らない。存在しないディレクトリの中には書き込めない。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数が足りない | W0008 | 8 |
| path が文字列でない | W0009 | 9 |
| charset が不正 | W0012 / W0009 | 12 / 9 |
| 要素のハッシュが不正（[DUMPXML](DUMPXML.md#エラー) を参照） | W0027 | 27 |
| ファイルを開けない | W0025 | 25 |
| 書き込みに失敗した | W0013 | 13 |

## Example
```
_x = FREADXML("shop.xml")
_x["children"][0]["text"] = "みかん"

FWRITEXML("shop.xml", _x, "Shift_JIS")
// shop.xml:
// <?xml version="1.0" encoding="Shift_JIS"?>
// <shop name="A">
//     <item id="1">みかん</item>
//     <item id="2">バナナ</item>
// </shop>
```

## Compatibility
- YAYA: Tc602-1以降

## See Also
- [DUMPXML](DUMPXML.md)
- [FREADXML](FREADXML.md)
- [FWRITEJSON](FWRITEJSON.md)
