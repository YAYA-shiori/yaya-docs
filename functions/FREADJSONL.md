# FREADJSONL
**Category:** ファイル操作

## Signature
```
FREADJSONL( path [, start [, maxlines [, key ...]]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 読み込む JSON Lines ファイルのパス（yaya.dll からの相対パス、または絶対パス） |
| start | 読み始めるバイト位置（省略可。既定は 0）。行の途中を指していたら、その行は飛ばして次の行から読む（[行の途中から読む](#行の途中から読む)）。0 以上 2147483647 以下 |
| maxlines | 読む行数の上限（省略可。既定は 0 で、ファイルの終わりまで）。空行や解けない行も数える |
| key | 取り出すキー（省略可。いくつでも指定できる）。各行が最上位のオブジェクトなら、そのキーの値だけを返す（[キーを指定して読む](#キーを指定して読む)）。文字列だけ |

## Returns
- 成功時: 次のキーを持つハッシュ
  - `rows`: JSON として解けた行の値の配列（[FREADJSON](FREADJSON.md#値の対応) と同じ変換）
  - `pos`: `rows` の各要素に対応する、その行の頭のバイト位置の配列（`rows` と同じ並び）
  - `end`: 読み終えた位置。続きを読むときは、これを `start` に渡す
  - `skipped`: JSON として解けずに読み飛ばした行の数
- 失敗時: 空（VOID）

## Description
JSON Lines（1 行に 1 つの JSON を書いたテキスト。`.jsonl`）のファイルを読み、行ごとの値の配列にして返す。[FOPEN](FOPEN.md) で開いておく必要はない。

[FREAD](FREAD.md) で 1 行ずつ読んで [PARSEJSON](PARSEJSON.md) で解くのと同じ結果が得られるが、ファイルを UTF-8 のまま 1 度に読んで行ごとに解析し、関数の呼び出しや文字列の変換を行の数だけ繰り返さないので速い。会話の記録や履歴のように、行が数万に増え、追記されていくファイルを読むのに向く。

- 文字コードは UTF-8 だけ。先頭の BOM は無視する
- 行の区切りは LF。行末の CR は無視する。空白だけの行は飛ばす
- JSON として解けない行は、警告を出さずに読み飛ばして `skipped` に数える。最上位がオブジェクトや配列でない行（`42` など）も、解けるなら `rows` に入る
- `/* */` や `//` のコメントは書けない（JSON Lines にコメントは無い。[FREADJSON](FREADJSON.md) との違い）
- `pos` の位置は、ファイルの先頭からのバイト数で、[FSEEK](FSEEK.md) や [FTELL](FTELL.md) で使うものと同じ

### 最後の行が書きかけのとき
最後の行が改行で終わっていないときは、JSON として解ければその行も読み、解けなければ（別のプログラムが書いている途中かもしれないので）読まずに残す。そのとき `end` は、その行の頭になる。`end` を次の `start` に渡せば、書き終わったあとの読み取りでその行から読める。

### 行の途中から読む
`start` の 1 つ前のバイトが改行でなければ、`start` は行の途中とみなして、最初の（欠けた）1 行を捨てる。ファイルの末尾だけを読みたいときに、`FSIZE` から読みたいバイト数を引いた位置を渡せばよい。`start` が行の頭（0 や、前回の `end`、`pos` の値）なら、その行から読む。

`start` がファイルの大きさ以上のときは何も読まず、`rows` と `pos` は空の配列、`end` は `start` になる。

### キーを指定して読む
`key` を指定すると、各行が最上位のオブジェクトのとき、そのキーの値だけをハッシュにして `rows` に入れる。行の JSON は全体を解析するが、結果の変換（文字列の変換とハッシュの作成）を指定したキーだけで済ませるので、依頼の本文のような大きな値を含む行から、時刻などだけを取り出すときに速く、結果も小さくなる。

- キーは最上位のものだけ。`.` で下の階層を指すことはできない（`"a.b"` は、名前に `.` を含むキーを指す）
- 行にないキーは、結果のハッシュにも作らない。値が `null` のキーは、全体を変換するときと同じく VOID の値で残る
- 最上位がオブジェクトでない行は、`key` を使わずに全体を変換する
- キーは配列で渡してもよい（関数の引数では、外側の配列が展開される）。`FREADJSONL("a.jsonl", 0, 0, _keys)` のように書ける

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数がない | W0008 | 8 |
| path が文字列でない。start・maxlines が整数でない。key が文字列でない | W0009 | 9 |
| start が負、または 2147483647 を超える。maxlines が負 | W0012 | 12 |
| ファイルを開けない | W0025 | 25 |

## Example
history.jsonl:
```
{"display":"こんにちは","timestamp":1790311762291,"project":"C:\\work\\a"}
{"display":"つづき","timestamp":1790311800000,"project":"C:\\work\\b"}
```

```
_r = FREADJSONL("history.jsonl", 0, 0, "timestamp", "project")
_r["rows"][0]["project"]    // C:\work\a
_r["rows"][1]["timestamp"]  // 1790311800000
_r["pos"][1]                // 2 行目の頭のバイト位置
_r["skipped"]               // 0
```

増えた分だけを読む（`end` を覚えておき、次の呼び出しの `start` に渡す）:
```
if GETTYPE(lastpos) == 0 {
    lastpos = 0
}
_r = FREADJSONL("history.jsonl", lastpos, 0, "timestamp", "project")
lastpos = _r["end"]
foreach _r["rows"]; _row {
    // 新しく書き足された行だけが順に入る
}
```

## Compatibility
- Tc608-6: 追加

## See Also
- [FREADJSON](FREADJSON.md)
- [PARSEJSON](PARSEJSON.md)
- [FREAD](FREAD.md)
- [FSEEK](FSEEK.md)
