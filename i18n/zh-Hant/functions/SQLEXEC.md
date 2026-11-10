# SQLEXEC
**Category:** データベース

## Signature
```
SQLEXEC( path, sql [, param...] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 以 [SQLOPEN](SQLOPEN.md) 開啟的資料庫路徑 |
| sql | 要執行的 SQL。可以用 `;` 分隔並撰寫多個陳述式 |
| param | 要代入 SQL 參數的值（可省略。請參閱下方的[參數](#パラメータ)） |

## Returns
- 成功時：INSERT、UPDATE、DELETE 所變更的資料列總數（若只包含其他陳述式則為 0）
- 失敗時：-1

## Description
執行 SQL。用於建立資料表、新增、變更或刪除資料列、開始交易等不使用結果資料列的 SQL。要接收 SELECT 的結果時，請使用 [SQLQUERY](SQLQUERY.md)（使用 SQLEXEC 執行 SELECT 時，結果資料列會被捨棄）。

sql 中有多個陳述式時，會從第一個開始依序執行。若中途的陳述式發生錯誤，便會停止。先前已執行的陳述式不會復原，因此若要一次復原所有變更，請在交易（`BEGIN` ～ `COMMIT`）中執行。

### 參數
可以在 SQL 中的 `?`（或 `?1` 這類帶編號的參數）、`:名前`、`@名前`、`$名前` 位置填入值。若直接將值嵌入 SQL 字串，可能會因字串包含 `'` 而發生錯誤，或執行非預期的 SQL（SQL 注入）。請務必以參數傳遞從外部取得的字串。

傳遞 param 的方式有兩種。

1. **依序排列值**：當 param 全部都是整數、實數、字串或 VOID 時，只執行一次。值會依序填入 `?`
2. **將每次執行所需的值分別放入陣列或雜湊**：當 param 全部都是陣列或雜湊時，每個陣列或雜湊代表一次執行，並依其數量執行
    - 雜湊：在 `:名前`、`@名前`、`$名前` 位置填入鍵為「名前」的值
    - 陣列：依序將元素填入 `?`

參數的值不足，或雜湊中沒有對應鍵的參數，會填入 NULL。混合傳遞值與雜湊、陣列會導致 W0009。

反之，當值多於參數時，多出的值不會使用，並會發出 W0030 警告（仍會執行）。第 1 種形式中 param 的數量，或第 2 種形式中陣列的元素數量，若多於 `?` 的數量（帶編號的參數，例如 `?3`，則以最大編號為準），就會發出警告。雜湊即使有未使用的鍵，也不會發出警告。

將陣列傳遞給函式時，最外層的陣列會展開為引數（[巢狀值與多維指派](../grammar/13-nesting.md)）。因此，傳遞值的陣列 `(1, "a")` 時會採用第 1 種「依序排列值」的形式；傳遞雜湊的陣列或陣列的陣列（例如透過 [PARSEJSON](PARSEJSON.md) 取得的陣列）時，則會採用第 2 種「分別代表每次執行」的形式。

即使寫成 `(1, 2), (3, 4)`，或連續排列兩個值的陣列變數，它們也會以 `,` 串接成一個陣列，因此不會採用「分別代表每次執行」的形式，而是以第 1 種形式只執行一次（若有兩個 `?`，則不會使用 3 和 4，並會發出 W0030）。若要逐次執行，請建立陣列的陣列或雜湊的陣列再傳遞。

sql 中有多個陳述式時，每個陳述式都會使用相同的參數（`?` 的編號會在每個陳述式中從 1 開始計算）。前一個陳述式剩下的值不會傳入下一個陳述式。將 `"first", "second"` 傳遞給 `INSERT INTO t VALUES (?); INSERT INTO u VALUES (?)` 時，兩個陳述式都會填入 `"first"`，而 `"second"` 不會使用（W0030）。若要為每個陳述式填入不同的值，請分開執行陳述式，或使用雜湊搭配 `:名前`。

以形式 2 新增多筆資料時，若以 `BEGIN` 和 `COMMIT` 包住，就不會逐筆寫入檔案，因此速度較快。

### 值的對應
| YAYA | SQLite | 傳回 YAYA 時 |
|------|--------|------|
| 整數 | INTEGER | 整數 |
| 實數 | REAL | 實數 |
| 字串 | TEXT（UTF-8） | 字串 |
| 空（VOID） | NULL | 空（VOID） |
| ― | BLOB | 十六進位字串（與 `hex()` 相同的大寫格式） |

- 空字串 `""` 並非 NULL，而是長度為 0 的 TEXT。若要寫入 NULL，請省略參數，或不要在雜湊中加入該索引鍵
- 陣列和雜湊無法放入單一參數（W0009）。若要以 JSON 格式儲存，請先使用 [DUMPJSON](DUMPJSON.md) 將其轉換成字串，再傳入。可使用 SQLite 的 JSON 函式（例如 `json_extract`、`->>`、`json_each`）搜尋其內容
- 若要寫入 BLOB，請傳入十六進位字串，並在 SQL 端使用 `unhex(?)`

### 重複使用準備好的陳述式
使用相同的 sql 字串執行時，會重複使用 SQLite 上次解析的結果（準備好的陳述式），因此速度較快。建議變更參數中的值，並多次執行相同的 sql。若將值嵌入 SQL 字串中，每次執行都會形成不同的 sql，無法重複使用。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 引數不足 | W0008 | 8 |
| path 或 sql 不是字串，param 不是上述任一種形式 | W0009 | 9 |
| 資料庫尚未開啟 | W0015 | 15 |
| SQL 執行失敗（語法錯誤、違反限制、唯讀等） | W0029 | 29 |
| param 的值多於參數數量（執行成功） | W0030 | 30 |

W0029 警告會附上 SQLite 的錯誤訊息（例如：`SQLEXEC : UNIQUE constraint failed: talk.id`）。W0030 警告會附上參數數量與值的數量（例如：`SQLEXEC : parameters 2, values 4`）。

W0030 會在執行成功時出現，因此傳回值與成功時相同（變更的行數）。GETLASTERROR 即使執行成功也不會重設為 0，因此檢查 W0030 時，請先呼叫 [SETLASTERROR](SETLASTERROR.md)`(0)`。

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
- YAYA：Tc602-11 之後
- Tc602-13：值多於參數時，會發出警告 W0030

## See Also
- [SQLQUERY](SQLQUERY.md)
- [SQLOPEN](SQLOPEN.md)
- [SQLCLOSE](SQLCLOSE.md)
- [DUMPJSON](DUMPJSON.md)
