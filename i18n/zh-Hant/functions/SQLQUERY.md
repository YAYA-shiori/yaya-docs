# SQLQUERY
**Category:** データベース

## Signature
```
SQLQUERY( path, sql [, param...] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 以 [SQLOPEN](SQLOPEN.md) 開啟的資料庫路徑 |
| sql | 要執行的 SQL（主要是 SELECT） |
| param | 要傳入 SQL 參數的值（可省略。與 [SQLEXEC](SQLEXEC.md#パラメータ) 相同） |

## Returns
- 成功時：結果列的通用陣列。每一列會成為「欄名 → 值」的雜湊。沒有列時傳回空的通用陣列
- 失敗時：空值（VOID）

## Description
執行 SQL 並傳回結果列。傳遞參數的方式、值的對應及錯誤，皆與 [SQLEXEC](SQLEXEC.md) 相同。

- 欄名會是 SELECT 中指定的名稱。如果是運算式欄，或有多個欄名相同（例如 `a.id` 和 `b.id`），請使用 `AS` 指定不同名稱。欄名相同時只會保留後面的欄
- NULL 欄會變成空值（VOID）。雜湊中的索引鍵仍會保留
- 如果 sql 中有多個陳述式，會依序串接各陳述式的結果列並傳回。即使每次呼叫分別以陣列或雜湊傳遞 param，也會串接所有次數的結果列並傳回
- 會先將所有列載入記憶體，再傳回結果。讀取列數很多的資料表時，請使用 `LIMIT` 或 `WHERE` 篩選。在 SQLite 處理期間，SHIORI 不會回應

空的結果（空的通用陣列）和失敗（VOID）可透過 [GETTYPE](GETTYPE.md) 區分（分別為 4 和 0）。

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
- YAYA：Tc602-11 之後
- Tc602-13：值的數量多於參數時，會顯示警告 W0030

## See Also
- [SQLEXEC](SQLEXEC.md)
- [SQLOPEN](SQLOPEN.md)
- [SQLCLOSE](SQLCLOSE.md)
- [PARSEJSON](PARSEJSON.md)
