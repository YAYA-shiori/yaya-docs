# SQLQUERY
**Category:** データベース

## Signature
```
SQLQUERY( path, sql [, param...] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path to a database opened with [SQLOPEN](SQLOPEN.md) |
| sql | SQL to execute (mainly SELECT statements) |
| param | Values to use for SQL parameters (optional; same as in [SQLEXEC](SQLEXEC.md#パラメータ)) |

## Returns
- On success: A generic array of result rows. Each row is a hash of "column name → value". Returns an empty generic array if there are no rows
- On failure: Empty (VOID)

## Description
Executes SQL and returns the result rows. Parameter passing, value mapping, and errors are the same as for [SQLEXEC](SQLEXEC.md).

- Column names are taken from the names specified in SELECT. For expression columns or multiple columns with the same name (such as `a.id` and `b.id`), assign different names with `AS`. If columns have the same name, only the later one remains
- A NULL column becomes empty (VOID). Its key remains in the hash
- If sql contains multiple statements, the rows from their results are concatenated in order. If param is passed as an array or hash for each execution, the rows from all executions are still concatenated
- All rows are loaded into memory before being returned. When reading a table with many rows, filter the results with `LIMIT` or `WHERE`. SHIORI responses are blocked while SQLite is processing

You can distinguish an empty result (an empty generic array) from a failure (VOID) with [GETTYPE](GETTYPE.md) (4 and 0, respectively).

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
- YAYA: Tc602-11 or later
- Tc602-13: Now issues warning W0030 when there are more values than parameters

## See Also
- [SQLEXEC](SQLEXEC.md)
- [SQLOPEN](SQLOPEN.md)
- [SQLCLOSE](SQLCLOSE.md)
- [PARSEJSON](PARSEJSON.md)
