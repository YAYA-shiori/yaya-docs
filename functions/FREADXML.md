# FREADXML
**Category:** ファイル操作

## Signature
```
FREADXML( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 読み込む XML ファイルのパス（yaya.dll からの相対パス、または絶対パス） |
| charset | ファイルの文字コード（省略可）。文字列（`"UTF-8"` `"Shift_JIS"` など。[文字コードの名前](../grammar/11-character-encoding.md#文字コードの名前)）または数値で指定する。省略時は下記のとおり自動で決める |

## Returns
- 成功時: ルート要素を表すハッシュ（下記の [要素の形](#要素の形)）
- 失敗時: 空（VOID）

## Description
XML ファイルを丸ごと読み込んで解析し、ルート要素をハッシュにして返す。[FOPEN](FOPEN.md) で開いておく必要はない。

XML の解析には [TinyXML-2](https://github.com/ponapalt/tinyxml2) を使っている。

charset を省略したときの文字コードは次の順に決める。

1. 先頭に UTF-8 の BOM があれば UTF-8
2. XML 宣言（`<?xml version="1.0" encoding="Shift_JIS"?>`）の encoding。`Windows-31J` `CP932` も Shift_JIS として扱う
3. どちらも無い、または encoding が YAYA の知らない文字コードなら UTF-8

charset を指定したときは XML 宣言の encoding を無視する。

### 要素の形

要素は、次の4つのキーを持つハッシュになる。キーは中身が空でも必ずある。

| キー | 値 |
|------|----|
| `name` | タグ名（名前空間の接頭辞があれば `ns:tag` のまま） |
| `attr` | 属性名 → 属性値 のハッシュ。値はすべて文字列 |
| `children` | 子要素のハッシュの汎用配列（出現順） |
| `text` | 直下のテキスト（CDATA を含む）を順に連結した文字列 |

- 実体参照（`&amp;` `&#x3042;` など）は展開済みになる
- テキストの前後の空白や改行はそのまま残る。要素と要素の間の空白だけの部分は `text` に入らない
- 子要素とテキストが混在する場合、テキストと子要素の前後関係は失われる（`<p>a<b>x</b>c</p>` の `text` は `ac`）
- コメント、処理命令、DOCTYPE、XML 宣言は無視する。ルート要素より外にあるものも返らない
- 属性の並びは保たれない。ハッシュのキーの順になる

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| path が文字列でない | W0009 | 9 |
| charset が不正 | W0012 / W0009 | 12 / 9 |
| ファイルを開けない | W0025 | 25 |
| XML として解析できない | W0026（エラーの内容と行番号も出力する） | 26 |

## Example
shop.xml:
```xml
<?xml version="1.0" encoding="Shift_JIS"?>
<shop name="A">
  <item id="1">りんご</item>
  <item id="2">バナナ</item>
</shop>
```

```
_x = FREADXML("shop.xml")
_x["name"]                          // shop
_x["attr"]["name"]                  // A
_x["children"][1]["name"]           // item
_x["children"][1]["attr"]["id"]     // 2
_x["children"][1]["text"]           // バナナ

foreach _x["children"]; _item {
    // _item["attr"]["id"] と _item["text"] を順に扱える
}
```

## Compatibility
- YAYA: Tc601-1以降
- Tc603-1: 知らない文字コードの名前を渡すと警告 W0012 を出して失敗するようにした（それまでは警告を出さずに OS デフォルトとして扱っていた）

## See Also
- [PARSEXML](PARSEXML.md)
- [FWRITEXML](FWRITEXML.md)
- [FREADJSON](FREADJSON.md)
- [値の入れ子と多次元代入](../grammar/13-nesting.md)
