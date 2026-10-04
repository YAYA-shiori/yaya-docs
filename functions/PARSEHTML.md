# PARSEHTML
**Category:** 型取得/変換

## Signature
```
PARSEHTML( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | HTML の文字列 |

## Returns
- 成功時: `<html>` 要素を表すハッシュ
- 失敗時: 空（VOID）

## Description
HTML の文字列を解析し、`<html>` 要素をハッシュにして返す。要素の形と解析の規則は [FREADHTML](FREADHTML.md#要素の形) と同じ。

文字列はすでに YAYA の文字列になっているので、`<meta charset>` は無視する。ファイルから読むときは [FREADHTML](FREADHTML.md) を使う。

HTML 全体ではなく一部分（`<p>a</p>` など）を渡しても、`<html>` `<head>` `<body>` が補われた木になる。部分は `<body>` の `children` から取り出す。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| str が文字列でない | W0009 | 9 |
| 入れ子が深すぎる（128段を超える） | W0026（原因も出力する） | 26 |

## Example
```
_h = PARSEHTML('<p class=a>x<b>y</b>z<br><img src="a.png" alt="&amp;"></p>')
_h["name"]                                   // html
_body = _h["children"][1]
_p = _body["children"][0]
_p["attr"]["class"]                          // a
_p["text"]                                   // xz
_p["children"][0]["text"]                    // y
_p["children"][2]["attr"]["alt"]             // &
```

## Compatibility
- YAYA: Tc605-1以降

## See Also
- [FREADHTML](FREADHTML.md)
- [PARSEXML](PARSEXML.md)
- [PARSEJSON](PARSEJSON.md)
