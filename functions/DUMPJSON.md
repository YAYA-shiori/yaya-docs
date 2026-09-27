# DUMPJSON
**Category:** 型取得/変換

## Signature
```
DUMPJSON( value [, pretty] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| value | JSON にする値。ハッシュや配列（入れ子を含む）も1つの引数として渡せる |
| pretty | 1 なら改行とインデントを入れて整形する。省略時は 0（1行にする） |

## Returns
- 成功時: JSON の文字列
- 引数がないとき: 空文字列

## Description
値を JSON の文字列にして返す。[PARSEJSON](PARSEJSON.md) の逆の変換になる。

### 値の対応

| YAYA | JSON |
|------|------|
| ハッシュ | オブジェクト。キーは文字列にする（`1` は `"1"`）。並びはハッシュのキーの順 |
| 汎用配列 | 配列 |
| 整数 | 数値。64bit の整数も誤差なく書く |
| 実数 | 数値。小数点か指数を必ず付ける（`1.0`、`0.1`、`1e+300`） |
| 文字列 | 文字列 |
| 空（VOID） | `null` |

- 整数の 1 / 0 は数値の `1` / `0` になる。`true` / `false` にはならない
- 実数は、読み戻して同じ値になる短い表記にする。NaN と無限大は JSON で表せないので `null` になる
- 文字列では `"` `\` と制御文字（改行・タブなど）だけをエスケープする。日本語などの非 ASCII の文字や `/` はそのまま書く
- 小数点はロケールによらず常に `.` になる

整形するときは、4つの空白でインデントし、改行は LF にする。空の配列・ハッシュは `[]` / `{}` と1つにまとめる。

[PARSEJSON](PARSEJSON.md) で読み戻すと元の値に戻る。ただし、値が整数の実数（`1.0`）は整数になる。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |

## Example
```
_h = IHASH()
_h["name"] = "さくら"
_h["tags"] = ("ghost", "shell")
_h["height"] = 158.5

DUMPJSON(_h)
// {"height":158.5,"name":"さくら","tags":["ghost","shell"]}

DUMPJSON(_h, 1)
// {
//     "height": 158.5,
//     "name": "さくら",
//     "tags": [
//         "ghost",
//         "shell"
//     ]
// }

DUMPJSON(("a", 1))          // ["a",1]
DUMPJSON(未定義の変数)       // null
```

## Compatibility
- YAYA: Tc602-1以降
- Tc602-5: 整数の最小値（-9223372036854775808）が `-` だけになり、正しい JSON にならなかったのを修正

## See Also
- [FWRITEJSON](FWRITEJSON.md)
- [PARSEJSON](PARSEJSON.md)
- [DUMPXML](DUMPXML.md)
