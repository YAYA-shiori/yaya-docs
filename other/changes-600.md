# 600 での変更点（Tc600-3以降）

Tc600-3 以降の YAYA（600 系）で、500 系（Tc574-1 まで）から変わった仕様をまとめる。

## 概要

| 項目 | 500 系 | 600 系 |
|---|---|---|
| 値の型 | VOID / 整数 / 実数 / 文字列 / 汎用配列 | ＋ **ハッシュ**（連想配列） |
| `GETTYPE` / `GETTYPEEX` | 0〜4 | ハッシュは **5** |
| 配列の要素 | スカラーだけ | 配列やハッシュも要素にできる（**入れ子**） |
| 要素への代入 | `a[x] = v` だけ | `a[x][y]... = v`（**多次元代入**）も可 |
| foreach | `foreach 式 ; 変数` | ＋ `foreach 式 ; キー変数, 値変数` |
| セーブファイル | 配列 `a:b:c` | ＋ ハッシュ `"k"=v:...`、入れ子 `IARRAY{...}` / `IHASH{...}` |
| 新しいシステム関数 | ― | [IHASH](../functions/IHASH.md) [HASH_KEYS](../functions/HASH_KEYS.md) [HASH_VALUES](../functions/HASH_VALUES.md) [HASH_SPLIT](../functions/HASH_SPLIT.md) [HASH_EXIST](../functions/HASH_EXIST.md) [HASH_SIZE](../functions/HASH_SIZE.md)、Tc601-1 から [FREADJSON](../functions/FREADJSON.md) [FREADXML](../functions/FREADXML.md) [PARSEJSON](../functions/PARSEJSON.md) [PARSEXML](../functions/PARSEXML.md)、Tc602-1 から [FWRITEJSON](../functions/FWRITEJSON.md) [FWRITEXML](../functions/FWRITEXML.md) [DUMPJSON](../functions/DUMPJSON.md) [DUMPXML](../functions/DUMPXML.md) |
| 新しい警告 | ― | W0024（ハッシュを `-` `*` `/` `%` に使った）、Tc601-1 から W0025（ファイルを開けない）・W0026（JSON/XML を解析できない）、Tc602-1 から W0027（JSON/XML に変換できない） |

ハッシュ・入れ子・多次元代入の文法は [ハッシュと値の入れ子](../grammar/12-hash.md) を参照。

500 系の `a[x][y] = v` は読み込み時にエラー E0029 だったので、この構文を含む既存の辞書は無い。

## 既存の辞書に影響しうる変更

### 配列の要素の VOID 同士の比較

配列の要素同士を比べるとき、**両方が VOID** なら等しいとみなすようになった。スカラー同士の VOID の比較と揃えたもの。

- `(1, 未定義の変数) == (1, 未定義の変数)` が 0 から 1 になる
- `ASEARCH(未定義の変数, 配列)` が、配列の中の VOID の要素の位置を返すようになる（500 系では -1）
- `HASH_EXIST`、`ARRAYDEDUP`、ハッシュ同士の `==` でも同じ

キーと要素の両方が VOID のときだけの変更で、整数・実数・文字列の比較は変わらない。

### ARRAYDEDUP に型の混ざった配列を渡したとき

500 系では、整数・実数・文字列が混ざった配列を渡すと、結果が並び方しだいで変わっていた。600 系では、ハッシュのキーと同じ規則で重複を除き、数値 < 文字列 の順に並べる。

```
ARRAYDEDUP((10, "9", 9, "a", 1.0, 1, "1"))
// 500 系: 1,1.000000,9,10,9,a
// 600 系: 1.000000,9,10,a
```

`1.0`、`1`、`"1"` は同じ値とみなされ、最初のもの（`1.0`）が残る。整数だけ、実数だけ、文字列だけの配列の結果は 500 系と同じ。

### setter・watcher に渡る配列

[FUNCDECL_WRITE](../functions/FUNCDECL_WRITE.md)（setter）と [FUNCDECL_READ](../functions/FUNCDECL_READ.md)（watcher）に渡る値が汎用配列のとき、500 系では値が壊れていた（setter の `_argv[1]` `_argv[2]` が空になる、watcher の `_argv[1]` が先頭要素だけになる、setter の戻り値をそのまま返すと変数が空になる）。

600 系では、配列は `_argv` の要素として入れ子のまま渡る。`_argv` の要素数は setter が 3、watcher が 2 のまま変わらない。

500 系で配列の変数に setter や watcher を付けても正しく動いていなかったので、実害はないはず。なお、添字への代入（`a[0] = v`）で setter が呼ばれないのは 500 系と同じ。

### 新しいシステム関数と同じ名前

- `IHASH` `HASH_KEYS` などと同じ名前のユーザー関数は、`Conflict.名前` に改名され、呼び出しはシステム関数に向く（TOAUTOEX が追加されたときと同じ仕組み）
- 同じ名前のグローバル変数は使えない。セーブファイルから復元するときに警告 W0002 が出る

## セーブファイルの互換性

- ハッシュや入れ子を含まない変数は、書き出す内容も読み込む結果も 500 系と同じ。500 系のセーブファイルはそのまま読める
- ハッシュや入れ子を含む変数は新しい書式で保存される（[SAVEVAR](../functions/SAVEVAR.md) を参照）
- **ダウングレードに注意**: 600 系で保存したファイルを 500 系で読むと、ハッシュや入れ子を含む変数だけが崩れる（落ちはしない。ほかの変数には影響しない）。崩れたまま保存し直すと、元の内容は失われる

## 性能

`_a ,= x` と `_a[i] = x` は、500 系では1回ごとに配列を丸ごと複製していた（ループで配列を育てると要素数の2乗に比例して遅くなる）。600 系ではこの複製をしないので、ループで配列を育てる処理が大幅に速くなった。

## 関連

- [ハッシュと値の入れ子](../grammar/12-hash.md)
- [フロー制御（foreach）](../grammar/07-flow-control.md#foreach-ループ)
- [SAVEVAR](../functions/SAVEVAR.md)
