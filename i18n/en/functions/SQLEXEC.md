# SQLEXEC
**Category:** データベース

## Signature
```
SQLEXEC( path, sql [, param...] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Database path opened with [SQLOPEN](SQLOPEN.md) |
| sql | SQL to execute. Multiple statements can be written, separated by `;` |
| param | Values to use for SQL parameters (optional; see [Parameters](#パラメータ) below) |

## Returns
- On success: Total number of rows changed by INSERT, UPDATE, and DELETE (0 if only other statements are used)
- On failure: -1

## Description
Executes SQL. Use this for SQL that does not use result rows, such as creating a table, adding, changing, or deleting rows, or starting a transaction. To receive the results of a SELECT statement, use [SQLQUERY](SQLQUERY.md) (if you execute SELECT with SQLEXEC, the result rows are discarded).

If sql contains multiple statements, they are executed in order from the beginning. If a statement encounters an error, execution stops there. Statements executed up to that point are not rolled back, so if you want to roll them all back, execute them inside a transaction (`BEGIN` 〜 `COMMIT`).

### Parameters
You can provide values for `?` (or numbered placeholders such as `?1`), `:name`, `@name`, and `$name` in SQL. Embedding values directly in the SQL string can cause errors when a string contains `'` or cause unintended SQL to be executed (SQL injection). Always pass strings received from external sources as parameters.

There are two ways to pass param.

1. **List values**: If all param values are integers, real numbers, strings, or VOID, the statement is executed once. Values are assigned to `?` in order, starting from the first
2. **Use an array or hash for each execution**: If all param values are arrays or hashes, each one is used for a single execution, and the statement is executed that many times
    - Hash: The value whose key is "name" is assigned to `:name`, `@name`, or `$name`
    - Array: Elements are assigned to `?` in order, starting from the first

Parameters without enough values, and parameters without a corresponding key in a hash, are assigned NULL. Mixing values with hashes or arrays results in W0009.

Conversely, when there are more values than parameters, the extra values are not used and a W0030 warning is issued (execution still takes place). In form 1, a warning is issued if the number of param values is greater than the number of `?` placeholders; in form 2, a warning is issued if the number of array elements is greater than that number. For numbered placeholders such as `?3`, the maximum number is used. Unused hash keys do not cause a warning.

When you pass an array to a function, the outermost array is expanded into arguments ([Nested Values and Multidimensional Assignment](../grammar/13-nesting.md)). Therefore, passing an array of values `(1, "a")` uses form 1, "List values"; passing an array of hashes, or an array of arrays (such as those returned by [PARSEJSON](PARSEJSON.md)), uses form 2, "one execution at a time".

Even if you write `(1, 2), (3, 4)` or list two variables containing arrays of values, they are joined into one array by `,`, so this does not use "one execution at a time"; instead, the statement is executed once in form 1 (if there are two `?` placeholders, 3 and 4 are unused, and W0030 is issued). To execute one batch at a time, create and pass an array of arrays or an array of hashes.

When sql contains multiple statements, the same parameters are used for every statement (numbered `?` placeholders are counted from 1 separately for each statement). Values left over from a previous statement are not passed to the next one. If you pass `"first", "second"` to `INSERT INTO t VALUES (?); INSERT INTO u VALUES (?)`, `"first"` is assigned to both statements, and `"second"` is unused (W0030). To provide different values for each statement, execute them separately or use `:name` with a hash.

When adding many rows in form 2, wrapping the statements in `BEGIN` and `COMMIT` is faster because the file is not written after every row.

### Value Mapping
| YAYA | SQLite | When returned to YAYA |
|------|--------|------|
| Integer | INTEGER | Integer |
| Real number | REAL | Real number |
| String | TEXT (UTF-8) | String |
| Empty (VOID) | NULL | Empty (VOID) |
| — | BLOB | Hexadecimal string (same uppercase letters as `hex()`) |

- An empty string `""` becomes TEXT with length 0, not NULL. To insert NULL, omit the parameter or leave out its key from the hash
- Arrays and hashes cannot be used as a single parameter (W0009). To store them as JSON, convert them to a string with [DUMPJSON](DUMPJSON.md) before passing them. You can search their contents using SQLite JSON functions such as `json_extract`, `->>`, and `json_each`
- To insert a BLOB, pass a hexadecimal string and use `unhex(?)` on the SQL side

### Reusing Prepared Statements
When executing with the same sql string, SQLite reuses the result of its previous parse (the prepared statement), making execution faster. It is useful to execute the same sql repeatedly while changing values through parameters. Embedding values in the SQL string makes each sql different, so it cannot be reused.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| Not enough arguments | W0008 | 8 |
| path or sql is not a string, or param is neither of the forms described above | W0009 | 9 |
| Database is not open | W0015 | 15 |
| SQL execution failed (syntax error, constraint violation, read-only database, etc.) | W0029 | 29 |
| More param values than parameters (execution succeeds) | W0030 | 30 |

The W0029 warning includes the SQLite error message (for example, `SQLEXEC : UNIQUE constraint failed: talk.id`). The W0030 warning includes the number of parameters and values (for example, `SQLEXEC : parameters 2, values 4`).

W0030 is issued when execution succeeds, so the return value is the same as on success (the number of changed rows). GETLASTERROR does not reset to 0 even after success, so when checking for W0030, first call [SETLASTERROR](SETLASTERROR.md)`(0)`.

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
- YAYA: Tc602-11 and later
- Tc602-13: Added a W0030 warning when there are more values than parameters

## See Also
- [SQLQUERY](SQLQUERY.md)
- [SQLOPEN](SQLOPEN.md)
- [SQLCLOSE](SQLCLOSE.md)
- [DUMPJSON](DUMPJSON.md)
