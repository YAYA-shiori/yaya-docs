# DUMPXML
**Category:** 型取得/変換

## Signature
```
DUMPXML( element [, pretty] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| element | ルート要素を表すハッシュ（[FREADXML](FREADXML.md#要素の形) が返すのと同じ形） |
| pretty | 1 なら改行とインデントを入れて整形する。省略時は 0（1行にする） |

## Returns
- 成功時: XML 宣言（`<?xml version="1.0" encoding="UTF-8"?>`）付きの XML の文字列
- 失敗時: 空文字列

## Description
要素のハッシュを XML の文字列にして返す。[PARSEXML](PARSEXML.md) の逆の変換になる。

要素のハッシュのキーは次のとおり。`name` 以外は無くてもよい（空でもよい）。

| キー | 値 |
|------|----|
| `name` | タグ名（必須）。文字列 |
| `attr` | 属性名 → 属性値 のハッシュ。値は整数・実数・文字列（文字列にして書く） |
| `children` | 子要素のハッシュの汎用配列 |
| `text` | 要素のテキスト。整数・実数・文字列 |

- テキストは子要素より前に書く。[FREADXML](FREADXML.md) で読んだ要素がテキストと子要素の混在したもの（`<p>a<b>x</b>c</p>`）だと、元の並びには戻らない（`<p>ac<b>x</b></p>` になる）
- `&` `<` `>` と、属性値の `"` はエスケープする
- タグ名と属性名は、ASCII の範囲だけ XML の名前の規則（先頭は英字・`_`・`:`、2文字目以降は数字・`-`・`.` も可）で調べる。日本語などの非 ASCII の文字は使える

整形するときは、4つの空白でインデントし、改行は LF にする。テキストを持つ要素の中でも、2つ目以降の子要素の前には改行とインデントが入る。[FREADXML](FREADXML.md) / [PARSEXML](PARSEXML.md) は要素の間の空白だけのテキストを無視するので、読み戻したときの `text` には影響しない。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| 要素がハッシュでない、`name` が無い・不正、`attr` がハッシュでない、属性名が不正、属性値や `text` が配列・ハッシュ、`children` が配列でない、子要素がハッシュでない | W0027（どこが不正かも出力する） | 27 |

## Example
```
_item = IHASH("name", "item", "text", "りんご")
_item["attr"] = IHASH("id", 1)
_shop = IHASH("name", "shop")
_shop["children"] = IARRAY()
_shop["children"] ,= _item

DUMPXML(_shop)
// <?xml version="1.0" encoding="UTF-8"?><shop><item id="1">りんご</item></shop>

DUMPXML(_shop, 1)
// <?xml version="1.0" encoding="UTF-8"?>
// <shop>
//     <item id="1">りんご</item>
// </shop>

DUMPXML(PARSEXML('<a x="1"><b/></a>'))
// <?xml version="1.0" encoding="UTF-8"?><a x="1"><b/></a>
```

## Compatibility
- YAYA: Tc602-1以降

## See Also
- [FWRITEXML](FWRITEXML.md)
- [PARSEXML](PARSEXML.md)
- [DUMPJSON](DUMPJSON.md)
