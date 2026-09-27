# SQLQUERY
**Category:** データベース

## Signature
```
SQLQUERY( path, sql [, param...] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | [SQLOPEN](SQLOPEN.md) で開いたデータベースのパス |
| sql | 実行する SQL（主に SELECT） |
| param | SQL のパラメータに入れる値（省略可。[SQLEXEC](SQLEXEC.md#パラメータ) と同じ） |

## Returns
- 成功時: 結果の行の汎用配列。1行が「列名 → 値」のハッシュになる。行が無ければ空の汎用配列
- 失敗時: 空（VOID）

## Description
SQL を実行して、結果の行を返す。パラメータの渡し方、値の対応、エラーは [SQLEXEC](SQLEXEC.md) と同じ。

- 列名は SELECT に書いた名前になる。式の列や、同じ名前の列が複数あるとき（`a.id` と `b.id` など）は、`AS` で別の名前を付けること。同じ名前の列は後のものだけが残る
- NULL の列は空（VOID）になる。ハッシュにキーは残る
- sql に複数の文があれば、結果の行を順につなげて返す。1回分ずつ配列・ハッシュで param を渡したときも、すべての回の行をつなげて返す
- 行はすべてメモリに読み込んでから返す。行の多い表を読むときは `LIMIT` や `WHERE` で絞ること。SQLite の処理中は SHIORI の応答が止まる

空の結果（空の汎用配列）と失敗（VOID）は [GETTYPE](GETTYPE.md) で見分けられる（それぞれ 4 と 0）。

## Example
```
SQLOPEN("ghost.db")

_rows = SQLQUERY("ghost.db", "SELECT id, text, score FROM talk WHERE score >= ? ORDER BY score DESC LIMIT 10", 2)
ARRAYSIZE(_rows)       // 行数
_rows[0]["text"]       // 1行目の text

foreach _rows; _r {
    // _r["id"] _r["text"] _r["score"]
}

// 集計には AS で名前を付ける
SQLQUERY("ghost.db", "SELECT count(*) AS n, avg(score) AS avg FROM talk")[0]["n"]

// JSON で保存した列を SQLite の JSON 関数で検索する
SQLEXEC("ghost.db", "CREATE TABLE IF NOT EXISTS ev(id TEXT PRIMARY KEY, json TEXT)")
_ev = PARSEJSON('{"id":"abc","tags":[["p","xyz"],["e","def"]]}')
SQLEXEC("ghost.db", "INSERT OR IGNORE INTO ev VALUES(?, ?)", _ev["id"], DUMPJSON(_ev))
SQLQUERY("ghost.db", "SELECT ev.id, t.value->>1 AS v FROM ev, json_each(ev.json, '$.tags') t WHERE t.value->>0 = ?", "e")
// → 要素1つ：IHASH("id", "abc", "v", "def")
```

## Compatibility
- YAYA: Tc602-11以降
- Tc602-13: 値がパラメータより多いときに警告 W0030 を出すようにした

## See Also
- [SQLEXEC](SQLEXEC.md)
- [SQLOPEN](SQLOPEN.md)
- [SQLCLOSE](SQLCLOSE.md)
- [PARSEJSON](PARSEJSON.md)
