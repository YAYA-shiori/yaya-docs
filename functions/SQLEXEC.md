# SQLEXEC
**Category:** データベース

## Signature
```
SQLEXEC( path, sql [, param...] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | [SQLOPEN](SQLOPEN.md) で開いたデータベースのパス |
| sql | 実行する SQL。`;` で区切って複数の文を書ける |
| param | SQL のパラメータに入れる値（省略可。下記の [パラメータ](#パラメータ)） |

## Returns
- 成功時: INSERT・UPDATE・DELETE で変更された行数の合計（それ以外の文だけなら 0）
- 失敗時: -1

## Description
SQL を実行する。表を作る、行を追加・変更・削除する、トランザクションを始める、といった結果の行を使わない SQL に使う。SELECT の結果を受け取るときは [SQLQUERY](SQLQUERY.md) を使う（SQLEXEC で SELECT を実行すると、結果の行は捨てられる）。

sql に複数の文があれば、先頭から順に実行する。途中の文でエラーになったら、そこで止まる。それまでに実行した文は取り消されないので、まとめて取り消したいときはトランザクション（`BEGIN` 〜 `COMMIT`）の中で実行する。

### パラメータ
SQL の中の `?`（または `?1` のような番号付き）や `:名前` `@名前` `$名前` の位置に値を入れられる。値を SQL の文字列に直接埋め込むと、`'` を含む文字列でエラーになったり、意図しない SQL が実行されたりする（SQL インジェクション）。外から受け取った文字列は必ずパラメータで渡すこと。

param の渡し方は2通りある。

1. **値を並べる**: param がすべて整数・実数・文字列・VOID のとき、1回だけ実行する。`?` に先頭から順に入る
2. **1回分ずつ配列かハッシュにする**: param がすべて配列かハッシュのとき、1つを1回分として、その数だけ実行する
    - ハッシュ: `:名前` `@名前` `$名前` に、キーが「名前」の値が入る
    - 配列: `?` に要素が先頭から順に入る

値が足りないパラメータや、ハッシュにキーが無いパラメータには NULL が入る。値とハッシュ・配列を混ぜて渡すと W0009 になる。

逆に、値がパラメータより多いときは、余った値は使われず、W0030 の警告が出る（実行はする）。1 の形では param の数が、2 の形では配列の要素数が、`?` の数（`?3` のような番号付きなら最大の番号）より多いと警告になる。ハッシュは使われなかったキーがあっても警告しない。

関数に配列を渡すと、いちばん外側の配列は引数に展開される（[値の入れ子と多次元代入](../grammar/13-nesting.md)）。そのため、値の配列 `(1, "a")` を渡すと 1 の「値を並べる」になり、ハッシュの配列や、配列の配列（[PARSEJSON](PARSEJSON.md) などで得たもの）を渡すと 2 の「1回分ずつ」になる。

`(1, 2), (3, 4)` と書いたり、値の配列の変数を2つ並べたりしても、`,` で1つの配列につながるので「1回分ずつ」にはならず、1 の形で1回だけ実行される（`?` が 2 つなら 3 と 4 は使われず、W0030 になる）。1回分ずつにしたいときは、配列の配列やハッシュの配列を作って渡す。

sql に複数の文があるときは、どの文にも同じパラメータが使われる（`?` の番号は文ごとに 1 から数える）。前の文の続きの値が次の文に入るわけではない。`INSERT INTO t VALUES (?); INSERT INTO u VALUES (?)` に `"first", "second"` を渡すと、どちらの文にも `"first"` が入り、`"second"` は使われない（W0030）。文ごとに違う値を入れたいときは、文を分けて実行するか、ハッシュで `:名前` を使う。

2 の形で多くの行を追加するときは、`BEGIN` と `COMMIT` で囲むと、1行ずつファイルに書き込まれないので速い。

### 値の対応
| YAYA | SQLite | YAYA に戻したとき |
|------|--------|------|
| 整数 | INTEGER | 整数 |
| 実数 | REAL | 実数 |
| 文字列 | TEXT（UTF-8） | 文字列 |
| 空（VOID） | NULL | 空（VOID） |
| ― | BLOB | 16進数の文字列（`hex()` と同じ大文字） |

- 空文字列 `""` は NULL ではなく、長さ 0 の TEXT になる。NULL を入れたいときは、パラメータを省くか、ハッシュにそのキーを入れない
- 配列やハッシュは1つのパラメータに入れられない（W0009）。JSON として保存したいときは [DUMPJSON](DUMPJSON.md) で文字列にしてから渡す。SQLite の JSON 関数（`json_extract` や `->>`、`json_each` など）で中身を検索できる
- BLOB を入れたいときは、16進数の文字列を渡して SQL 側で `unhex(?)` にする

### 準備済みの文の再利用
同じ sql の文字列で実行すると、前回 SQLite が解析した結果（準備済みの文）を使い回すので速い。パラメータで値を変えながら同じ sql を何度も実行するとよい。値を SQL の文字列に埋め込むと毎回別の sql になり、使い回せない。

### エラー
| 状況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引数が足りない | W0008 | 8 |
| path または sql が文字列でない、param が上記のどちらの形でもない | W0009 | 9 |
| データベースを開いていない | W0015 | 15 |
| SQL の実行に失敗した（文法の誤り、制約違反、読み取り専用など） | W0029 | 29 |
| param の値がパラメータより多い（実行は成功する） | W0030 | 30 |

W0029 の警告には SQLite のエラーメッセージが付く（例: `SQLEXEC : UNIQUE constraint failed: talk.id`）。W0030 の警告にはパラメータの数と値の数が付く（例: `SQLEXEC : parameters 2, values 4`）。

W0030 は実行に成功したときに出るので、返値は成功時と同じ（変更された行数）。GETLASTERROR は成功しても 0 に戻らないので、W0030 を調べるときは先に [SETLASTERROR](SETLASTERROR.md)`(0)` しておく。

## Example
```
SQLOPEN("ghost.db")
SQLEXEC("ghost.db", "CREATE TABLE IF NOT EXISTS talk(id INTEGER PRIMARY KEY, text TEXT, score REAL); CREATE INDEX IF NOT EXISTS talk_score ON talk(score)")

// 値を並べる
SQLEXEC("ghost.db", "INSERT INTO talk(text, score) VALUES(?, ?)", "こんにちは", 1.5)   // 1

// ハッシュで名前を指定する
_h = IHASH("text", "こんばんは", "score", 2)
SQLEXEC("ghost.db", "INSERT INTO talk(text, score) VALUES(:text, :score)", _h)   // 1

// ハッシュの配列で、まとめて追加する
_rows = (IHASH("text", "a", "score", 3), IHASH("text", "b", "score", 4))
SQLEXEC("ghost.db", "BEGIN")
SQLEXEC("ghost.db", "INSERT INTO talk(text, score) VALUES(:text, :score)", _rows)   // 2
SQLEXEC("ghost.db", "COMMIT")

SQLEXEC("ghost.db", "UPDATE talk SET score = score + 1 WHERE score >= ?", 3)   // 2
SQLEXEC("ghost.db", "DELETE FROM talk WHERE text = ?", "a")                     // 1

// 直前に追加した行の id は SQL の関数で得る
SQLQUERY("ghost.db", "SELECT last_insert_rowid() AS id")[0]["id"]
```

## Compatibility
- YAYA: Tc602-11以降
- Tc602-13: 値がパラメータより多いときに警告 W0030 を出すようにした

## See Also
- [SQLQUERY](SQLQUERY.md)
- [SQLOPEN](SQLOPEN.md)
- [SQLCLOSE](SQLCLOSE.md)
- [DUMPJSON](DUMPJSON.md)
