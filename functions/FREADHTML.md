# FREADHTML
**Category:** ファイル操作

## Signature
```
FREADHTML( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 読み込む HTML ファイルのパス（yaya.dll からの相対パス、または絶対パス） |
| charset | ファイルの文字コード（省略可）。文字列（`"UTF-8"` `"Shift_JIS"` など。[文字コードの名前](../grammar/11-character-encoding.md#文字コードの名前)）または数値で指定する。省略時は下記のとおり自動で決める |

## Returns
- 成功時: `<html>` 要素を表すハッシュ（下記の [要素の形](#要素の形)）
- 失敗時: 空（VOID）

## Description
HTML ファイルを丸ごと読み込んで解析し、`<html>` 要素をハッシュにして返す。[FOPEN](FOPEN.md) で開いておく必要はない。

HTML の解析には [Gumbo](https://github.com/ponapalt/gumbo-parser-mirror)（HTML5 の構文解析規則に従うパーサ）を使っている。閉じタグの抜けや壊れた入れ子があっても、ブラウザと同じ規則で補って木にするので、解析自体は失敗しない。`<html>` `<head>` `<body>` も無ければ補われる。

charset を省略したときの文字コードは次の順に決める。

1. 先頭に UTF-8 の BOM があれば UTF-8
2. 先頭 1024 バイト以内の `<meta charset="Shift_JIS">`、または `<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">` の文字コード。コメントの中は読まない。`Windows-31J` `CP932` も Shift_JIS として扱う
3. どちらも無い、または YAYA の知らない文字コード（`UTF-16` を含む）なら UTF-8

charset を指定したときは `<meta>` を無視する。

### 要素の形

要素は [FREADXML](FREADXML.md#要素の形) と同じく、次の4つのキーを持つハッシュになる。キーは中身が空でも必ずある。

| キー | 値 |
|------|----|
| `name` | タグ名（HTML の要素は小文字。`div` `custom-tag` など） |
| `attr` | 属性名 → 属性値 のハッシュ。値はすべて文字列。属性名は小文字になる |
| `children` | 子要素のハッシュの汎用配列（出現順） |
| `text` | 直下のテキストを順に連結した文字列 |

- 文字参照（`&amp;` `&#x3042;` `&nbsp;` など）は展開済みになる
- `<br>` `<img>` のような中身の無い要素も、`children` と `text` が空の要素になる
- 子要素とテキストが混在する場合、テキストと子要素の前後関係は失われる（`<p>a<b>x</b>c</p>` の `text` は `ac`）
- 子要素を持つ要素では、空白だけのテキスト（要素と要素の間の改行や字下げ）は `text` に入らない。子要素が無い要素では空白だけでも残る（`<pre> </pre>` の `text` は半角空白）
- `<script>` `<style>` `<textarea>` の中身も `text` に入る
- コメント、DOCTYPE、処理命令は無視する
- SVG・MathML の中の `xlink:href` `xml:lang` のような属性は、接頭辞付きの名前になる
- 入れ子が 128 段を超える HTML は失敗する（`<html>` を1段目として数える）
- 属性の並びは保たれない。ハッシュのキーの順になる

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| path が文字列でない | W0009 | 9 |
| charset が不正 | W0012 / W0009 | 12 / 9 |
| ファイルを開けない | W0025 | 25 |
| 入れ子が深すぎる | W0026（原因も出力する） | 26 |

## Example
page.html:
```html
<!DOCTYPE html>
<html>
<head><meta charset="Shift_JIS"><title>お知らせ</title></head>
<body>
<h1>お知らせ</h1>
<ul>
  <li><a href="a.html">その1</a></li>
  <li><a href="b.html">その2</a></li>
</ul>
</body>
</html>
```

```
_h = FREADHTML("page.html")
_h["children"][0]["children"][1]["text"]     // お知らせ（<title>。[0] は <meta>）
_body = _h["children"][1]
_body["children"][0]["text"]                 // お知らせ（<h1>）
_ul = _body["children"][1]
foreach _ul["children"]; _li {
    _a = _li["children"][0]
    // _a["attr"]["href"] と _a["text"] を順に扱える
}
```

## Compatibility
- YAYA: Tc605-1以降

## See Also
- [PARSEHTML](PARSEHTML.md)
- [FREADXML](FREADXML.md)
- [FREADJSON](FREADJSON.md)
- [値の入れ子と多次元代入](../grammar/13-nesting.md)
