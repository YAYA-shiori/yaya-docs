# DUMPTOML
**Category:** 型取得/変換

## Signature
```
DUMPTOML( value [, pretty] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| value | TOML にするハッシュ（入れ子を含む）。TOML の最上位は表なので、ハッシュ以外は渡せない |
| pretty | 1 なら `[表]` の見出しを使って整形する、0 なら最上位のキー1つにつき1行にする。省略時は 1 |

## Returns
- 成功時: TOML の文字列
- 失敗時・引数がないとき: 空文字列

## Description
ハッシュを TOML の文字列にして返す。[PARSETOML](PARSETOML.md) の逆の変換になる。

[DUMPJSON](DUMPJSON.md) / [DUMPXML](DUMPXML.md) と違い、pretty の省略時は整形する（1）。

### 値の対応

| YAYA | TOML |
|------|------|
| ハッシュ | 表。キーは英数字・`_`・`-` だけならそのまま、それ以外は `"..."` で書く。並びはハッシュのキーの順 |
| ハッシュだけの汎用配列 | 表の配列（pretty が 1 のとき `[[名前]]`） |
| 汎用配列 | 配列 |
| 整数 | 整数。64bit の整数も誤差なく書く |
| 実数 | 実数。小数点か指数を必ず付ける（`1.0`、`0.1`、`1e+300`）。NaN は `nan`、無限大は `inf` / `-inf` |
| 文字列 | 文字列（下記） |
| 空（VOID） | 書かない（TOML には null が無いため、そのキーごと省く） |

- 整数の 1 / 0 は `1` / `0` になる。`true` / `false` にはならない
- 日時の文字列（[FREADTOML](FREADTOML.md) で読んだもの）も文字列として `"..."` で書く
- 配列の要素が空（VOID）のときは表せないのでエラー W0027 になる
- 小数点はロケールによらず常に `.` になる

文字列は、ふつうは `"..."` で書き、`"` `\` と制御文字をエスケープする。`\` を含み `'` と改行を含まないもの（Windows のパスなど）は、読みやすいようエスケープなしの `'...'` で書く。

### 整形の形（pretty が 1）

- その表のキーと値 → 下の階層の表（`[a.b]`）→ 表の配列（`[[a.c]]`）の順に書き、表と表の間には空行を入れる
- キーと値を持たず、下の階層の表だけを持つ表は見出しを省く（`[a.b]` だけで `a` も定義される）
- 改行を含む文字列は複数行の `"""..."""` にする
- 80 文字を超える配列や、配列・ハッシュを要素に持つ配列は、1要素1行（4つの空白で字下げし、各要素の後にカンマ）にする
- 改行は LF で、最後の行の後にも改行を付ける

pretty が 0 のときは、最上位のキー1つにつき1行とし、下の階層のハッシュはインライン表（`{ k = v }`）、表の配列はインライン表の配列にする。

[PARSETOML](PARSETOML.md) で読み戻すと元の値に戻る（空の値を省いた分を除く）。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| value がハッシュでない、配列の要素に空（VOID）がある | W0027（原因も出力する） | 27 |

## Example
```
_n = IHASH()
_n["title"] = "設定"
_n["ghost"] = IHASH("name", "さくら", "age", 17)
_n["ghost"]["shell"] = IHASH("name", "master")

DUMPTOML(_n)
// title = "設定"
//
// [ghost]
// age = 17
// name = "さくら"
//
// [ghost.shell]
// name = "master"

DUMPTOML(_n, 0)
// ghost = { age = 17, name = "さくら", shell = { name = "master" } }
// title = "設定"

DUMPTOML(("a", 1))          // 空文字列（警告 W0027）
```

## Compatibility
- YAYA: Tc602-5以降

## See Also
- [FWRITETOML](FWRITETOML.md)
- [PARSETOML](PARSETOML.md)
- [DUMPJSON](DUMPJSON.md)
- [DUMPYAML](DUMPYAML.md)
