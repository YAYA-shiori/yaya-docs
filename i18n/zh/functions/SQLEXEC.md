# SQLEXEC
**Category:** データベース

## Signature
```
SQLEXEC( path, sql [, param...] )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| path | 由 [SQLOPEN](SQLOPEN.md) 打开的数据库路径 |
| sql | 要执行的 SQL。可以用 `;` 分隔，写入多条语句 |
| param | 要填入 SQL 参数的值（可省略。参见下方的 [参数](#パラメータ)） |

## Returns
- 成功时：INSERT、UPDATE、DELETE 所更改行数的总和（如果只有其他类型的语句，则为 0）
- 失败时：-1

## Description
执行 SQL。适用于创建表、添加/更改/删除行、开始事务等不需要使用结果行的 SQL。接收 SELECT 的结果时，请使用 [SQLQUERY](SQLQUERY.md)（使用 SQLEXEC 执行 SELECT 时，结果行会被丢弃）。

如果 sql 中有多条语句，则从开头开始依次执行。如果中途某条语句出错，就会在该处停止。此前已经执行的语句不会撤销；如果想要将它们一并撤销，请在事务（`BEGIN` ～ `COMMIT`）中执行。

### 参数
可以在 SQL 中的 `?`（或 `?1` 这类带编号的参数）以及 `:名称` `@名称` `$名称` 的位置填入值。直接将值嵌入 SQL 字符串，可能会因为字符串中包含 `'` 而出错，或导致执行非预期的 SQL（SQL 注入）。务必通过参数传递从外部接收的字符串。

param 有两种传递方式。

1. **依次列出值**：当 param 全部为整数、实数、字符串或 VOID 时，只执行一次。按顺序填入 `?`
2. **将每次执行的参数分别放入数组或哈希**：当 param 全部为数组或哈希时，将每个数组或哈希作为一次执行的参数，执行相应次数
    - 哈希：将键为“名称”的值填入 `:名称` `@名称` `$名称`
    - 数组：按顺序将元素填入 `?`

缺少对应值的参数，以及哈希中没有对应键的参数，会填入 NULL。混合传递值与哈希、数组会产生 W0009。

反过来，如果值多于参数，则多余的值不会被使用，并会发出 W0030 警告（但仍会执行）。形式 1 中 param 的数量，或形式 2 中数组的元素数量，多于 `?` 的数量时会产生警告（如果是 `?3` 这样的带编号参数，则比较最大编号）。哈希即使有未使用的键，也不会发出警告。

向函数传递数组时，最外层数组会展开为参数（[值的嵌套与多维赋值](../grammar/13-nesting.md)）。因此，传递值数组 `(1, "a")` 时，会采用形式 1 的“依次列出值”；而传递哈希数组或数组的数组（例如通过 [PARSEJSON](PARSEJSON.md) 等获得的数组）时，则会采用形式 2 的“分别作为每次执行的参数”。

即使写成 `(1, 2), (3, 4)`，或连续传递两个值数组变量，它们也会通过 `,` 连接成一个数组，因此不会采用“分别作为每次执行的参数”，而是以形式 1 只执行一次（如果有两个 `?`，则不会使用 3 和 4，并会产生 W0030）。要分别执行多次，请创建并传递数组的数组或哈希的数组。

sql 中有多条语句时，所有语句都会使用相同的参数（`?` 的编号对每条语句都从 1 开始计算）。下一条语句不会接收上一条语句之后剩余的值。向 `INSERT INTO t VALUES (?); INSERT INTO u VALUES (?)` 传递 `"first", "second"` 时，两条语句都会填入 `"first"`，而 `"second"` 不会被使用（W0030）。如果想为每条语句填入不同的值，请分开执行语句，或使用哈希和 `:名称`。

使用形式 2 添加大量行时，用 `BEGIN` 和 `COMMIT` 括起来会更快，因为不会逐行写入文件。

### 值的对应关系
| YAYA | SQLite | 返回 YAYA 时 |
|------|--------|------|
| 整数 | INTEGER | 整数 |
| 实数 | REAL | 实数 |
| 字符串 | TEXT（UTF-8） | 字符串 |
| 空（VOID） | NULL | 空（VOID） |
| ― | BLOB | 十六进制字符串（与 `hex()` 相同，使用大写字母） |

- 空字符串 `""` 不会变成 NULL，而是成为长度为 0 的 TEXT。要填入 NULL，请省略参数，或不要在哈希中加入该键
- 数组或哈希不能作为单个参数传入（W0009）。如果要以 JSON 形式保存，请先用 [DUMPJSON](DUMPJSON.md) 转换为字符串，再传递。可以使用 SQLite 的 JSON 函数（如 `json_extract`、`->>`、`json_each`）搜索其中的内容
- 要填入 BLOB，请传递十六进制字符串，并在 SQL 端使用 `unhex(?)`

### 重用已准备的语句
使用相同的 sql 字符串执行时，会复用 SQLite 上次解析的结果（已准备的语句），因此速度更快。适合通过参数更改值，并多次执行相同的 sql。如果将值嵌入 SQL 字符串，每次都会生成不同的 sql，无法复用。

### 错误
| 情况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 参数不足 | W0008 | 8 |
| path 或 sql 不是字符串，或 param 不属于上述任一种形式 | W0009 | 9 |
| 数据库未打开 | W0015 | 15 |
| SQL 执行失败（语法错误、违反约束、只读等） | W0029 | 29 |
| param 的值多于参数（执行仍会成功） | W0030 | 30 |

W0029 警告会附带 SQLite 错误消息（例如：`SQLEXEC : UNIQUE constraint failed: talk.id`）。W0030 警告会附带参数数量和值的数量（例如：`SQLEXEC : parameters 2, values 4`）。

W0030 会在执行成功时发出，因此返回值与成功时相同（更改的行数）。即使执行成功，GETLASTERROR 也不会重置为 0；检查 W0030 时，请先调用 [SETLASTERROR](SETLASTERROR.md)`(0)`。

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
- YAYA：Tc602-11 及以后
- Tc602-13：调整为在值多于参数时发出 W0030 警告

## See Also
- [SQLQUERY](SQLQUERY.md)
- [SQLOPEN](SQLOPEN.md)
- [SQLCLOSE](SQLCLOSE.md)
- [DUMPJSON](DUMPJSON.md)
