# SQLQUERY
**Category:** データベース

## Signature
```
SQLQUERY( path, sql [, param...] )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| path | 使用 [SQLOPEN](SQLOPEN.md) 打开的数据库路径 |
| sql | 要执行的 SQL（主要是 SELECT） |
| param | 要传入 SQL 参数的值（可省略。与 [SQLEXEC](SQLEXEC.md#パラメータ) 相同） |

## Returns
- 成功时：结果行组成的通用数组。每一行是一个「列名 → 值」的哈希。没有行时返回空的通用数组
- 失败时：空（VOID）

## Description
执行 SQL 并返回结果行。参数的传递方式、值的对应关系和错误与 [SQLEXEC](SQLEXEC.md) 相同。

- 列名与 SELECT 中写出的名称相同。对于表达式列或有多个同名列的情况（如 `a.id` 和 `b.id`），请使用 `AS` 设置不同的名称。同名列只保留后面的列
- NULL 列会变为空（VOID）。哈希中的键仍会保留
- sql 中有多条语句时，会按顺序连接并返回结果行。即使按每次调用分别传入数组或哈希形式的 param，也会连接并返回所有调用的行
- 所有行都会先读入内存再返回。读取行数较多的表时，请使用 `LIMIT` 或 `WHERE` 筛选。SQLite 处理期间，SHIORI 的响应会停止

可通过 [GETTYPE](GETTYPE.md) 区分空结果（空的通用数组）和失败（VOID）（分别为 4 和 0）。

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
- YAYA：Tc602-11 及之后
- Tc602-13：当值的数量多于参数时，会发出警告 W0030

## See Also
- [SQLEXEC](SQLEXEC.md)
- [SQLOPEN](SQLOPEN.md)
- [SQLCLOSE](SQLCLOSE.md)
- [PARSEJSON](PARSEJSON.md)
