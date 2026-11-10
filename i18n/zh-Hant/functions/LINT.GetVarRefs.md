# LINT.GetVarRefs
**Category:** デバッグ

## Signature
```
LINT.GetVarRefs(function_name)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| function_name | 要分析的函式名稱 |

## Returns
- 成功：通用陣列，其中每個元素都是以逗號分隔的字串，包含 `kind,category,name,access,line,depth,context` 這 7 個欄位
- 錯誤：-1

## Description
列舉指定函式內變數與函式的出現位置，以及區塊（大括號）的進入與離開情形；每次出現各列為一筆，並以通用陣列傳回。與 `LINT.GetLocalVarUsedBy` 等函式不同，內容還包含讀取／寫入的區別、行號、區塊種類，以及出現位置的語法種類。

每個元素都是以逗號分隔的字串，因此可直接當作簡易陣列取出各欄位。

```
_refs = LINT.GetVarRefs('OnTest')
foreach _refs ; _r {
	_kind = _r[0]
	_name = _r[2]
	_line = TOINT(_r[4])
}
```

### 欄位

| 編號 | 欄位 | 值 |
|------|------|-----|
| 0 | kind | `var`（變數） / `func`（函式） / `{`（區塊開始） / `}`（區塊結束） |
| 1 | category | `var` 時為 `local` / `global`，`func` 時為 `user` / `system`，`{` `}` 時為區塊種類 |
| 2 | name | 變數名稱或函式名稱（`{` `}` 時為空） |
| 3 | access | `var` 時為 `r`（讀取） / `w`（指派） / `rw`（讀取和寫入），`func` 時為 `call`（`{` `}` 時為空） |
| 4 | line | 辭典檔案中的行號 |
| 5 | depth | 區塊的巢狀深度（函式本體為 1） |
| 6 | context | 出現位置的陳述式種類（`{` `}` 時為空） |

### access

| 值 | 對象 |
|----|------|
| `r` | 除指派目標以外的所有出現位置 |
| `w` | `=` `:=` 的指派目標、對陣列元素使用 `=` 的指派目標（`_a[0] = 1` 中的 `_a`）、`foreach` 的迴圈變數（雙變數的 foreach 中兩者皆包含。Tc600-3 以後） |
| `rw` | `+=` `-=` `*=` `/=` `%=` `,=` 及其 `:=` 形式、`++` `--` 的對象（包含對陣列元素的複合指派） |

指派會在右側運算式求值後執行，因此同一個陳述式中的指派目標（`w` / `rw`）會列在最後。

```
_z = _z + 1
// var,local,_z,r,10,1,subst
// var,local,_z,w,10,1,subst
```

### 區塊種類（`{` `}` 的 category）

| 值 | 對象 |
|----|------|
| `function` | 函式本體 |
| `if` / `elseif` / `else` | if 語法 |
| `while` | while 語法 |
| `for` | for 語法 |
| `foreach` | foreach 語法 |
| `switch` | switch 語法 |
| `case` | case 語法 |
| `when` / `others` | case 語法中的 when / others |
| `plain` | 以上皆非（獨立的 `{ }` 或 switch 的各個區塊等） |

`}` 會包含與對應的 `{` 相同的種類和深度。

### context

| 值 | 對象 |
|----|------|
| `output` | 要輸出的運算式 |
| `subst` | 包含指派的運算式 |
| `if` / `elseif` / `while` / `switch` | 各語法的條件運算式 |
| `for-init` / `for-cond` / `for-step` | `for a ; b ; c` 中的 a / b / c |
| `foreach` / `foreach-var` | `foreach a ; b` 中的 a / b（`foreach a ; k, v` 中的 k 和 v 都是 `foreach-var`。Tc600-3 以後） |
| `case` / `when` | case 運算式 / when 條件 |
| `parallel` / `void` / `return` | 各語法的運算式 |

例如 `if _c = 1` 會以 `context` 為 `if`、`access` 為 `w` 的項目出現。

### 不會列舉的項目

- `case` 語法內部產生的區域變數（名稱以 `_CaSe_ExPr_PrEfIx_` 開頭）
- 不包含變數或函式的陳述式（`break` / `continue` / `return`（無運算式） / `--`、僅輸出常值等）
- when 標籤（常值）

限制的詳細資訊請參閱 [LINT 系列函式的規格與限制](../other/lint-functions.md)。

## Compatibility
- YAYA：Tc574-1 以後可使用

## See Also
- LINT.GetFuncUsedBy
- LINT.GetUserDefFuncUsedBy
- LINT.GetGlobalVarUsedBy
- LINT.GetGlobalVarLetted
- LINT.GetLocalVarUsedBy
- LINT.GetLocalVarLetted
