# LINT 系函式的規格與限制

`LINT.*` 系函式是一組除錯用函式，可從已載入辭典的解析結果（函式內的陳述式與運算式項目）擷取函式與變數的使用位置。這些資訊可作為在 YAYA 辭典中自行建置類似 yayalint 的靜態檢查工具的素材，但有以下規格與限制。

## 函式一覽

| 函式 | 對象 | 重複 | 範圍 `{` `}` | 讀寫區分 | 行 |
|------|------|------|------|------|------|
| [LINT.GetVarRefs](../functions/LINT.GetVarRefs.md) | 變數、函式、區塊 | 每次出現 | 有（含種類） | 有 | 有 |
| [LINT.GetFuncUsedBy](../functions/LINT.GetFuncUsedBy.md) | 函式（使用者自訂・系統） | 去除重複・依名稱排序 | 無 | - | 無 |
| [LINT.GetUserDefFuncUsedBy](../functions/LINT.GetUserDefFuncUsedBy.md) | 使用者自訂函式 | 去除重複・依名稱排序 | 無 | - | 無 |
| [LINT.GetGlobalVarUsedBy](../functions/LINT.GetGlobalVarUsedBy.md) | 全域變數（讀寫皆包含） | 去除重複・依名稱排序 | 無 | 無 | 無 |
| [LINT.GetGlobalVarLetted](../functions/LINT.GetGlobalVarLetted.md) | 全域變數（僅指派） | 去除重複・依名稱排序 | 無 | - | 無 |
| [LINT.GetLocalVarUsedBy](../functions/LINT.GetLocalVarUsedBy.md) | 區域變數（讀寫皆包含） | 每次出現 | 有 | 無 | 無 |
| [LINT.GetLocalVarLetted](../functions/LINT.GetLocalVarLetted.md) | 區域變數（僅指派） | 每次出現 | 有 | - | 無 |

若要新建檢查，使用 `LINT.GetVarRefs` 即可取得包含其他函式所有資訊的結果。

## Tc574-1 的變更

- 新增了 `LINT.GetVarRefs`。
- `GetGlobalVarLetted` / `GetLocalVarLetted`
  - 現在會將指派給陣列元素（`_a[0] = 1`、`G_a[0] = 1`）列為對該變數的指派。
  - 現在會將 `foreach _list ; _v` 的迴圈變數 `_v` 列為指派。
- `GetLocalVarUsedBy`
  - 在同一個陳述式內，會將指派目標變數排在最後。由於指派是在右側運算式求值後進行，`_z = _z + 1` 的順序會是 `_z`（讀取）→ `_z`（指派）。
- `GetLocalVarUsedBy` / `GetLocalVarLetted`
  - 現在不會列出 `case` 語法在內部產生的區域變數（以 `_CaSe_ExPr_PrEfIx_` 開頭的名稱）。

## 限制

### 以辭典已載入為前提

分析對象是成功載入的辭典。若辭典因語法錯誤等原因無法載入，YAYA 會進入緊急模式，而使用 LINT 系函式的辭典本身也無法執行。重複定義、語法錯誤、帶括號的未定義函式呼叫（E0071）等錯誤，YAYA 本體會在載入時輸出。

### 位置資訊

- 可透過 `LINT.GetVarRefs` 取得行號。這是陳述式層級的行號。
- 以 `/` 延續行，或透過 here document 跨越多行的陳述式，會使用其**最後一行**的行號。
- 無法取得欄位位置。YAYA 內部也沒有保留這項資訊。這是因為載入時會合併行、替換 `#define`、移除註解，並以 `{` `}` `;` 分割內容。

### 名稱的呈現方式

- `#define` / `#globaldefine` 會在載入時以字串替換，因此會顯示替換後的名稱。
- 無法追蹤以字串指定的名稱，例如 `EVAL('名前')` 或 `LETTONAME('名前', …)`。
- 執行 LINT 的辭典本身所含的函式與變數也會列在清單中。請利用前綴等方式排除。
- 內嵌運算式 `%(式)` 展開時，內部使用的 `TOSTR` 會被列為函式呼叫（`LINT.GetFuncUsedBy` / `LINT.GetVarRefs`）。無法與使用者撰寫的 `TOSTR` 區分。

### 讀寫區分

- 在 `LINT.GetVarRefs` 中，`=` 的指派目標是 `w`，複合指派（例如 `+=`，也包含 `++` `--`）的指派目標是 `rw`。
- 對陣列元素使用 `=` 指派（`_a[0] = 1`）時，會視為 `w`。陣列的其他元素會保留，因為也允許對未定義的變數指派元素。
- 排序（將指派目標排在最後）是以陳述式為單位。若單一運算式包含多個指派，排序可能與實際執行順序不一致。
- 除了 `LINT.GetVarRefs` 以外的函式都沒有讀寫標記。
  - `GetGlobalVarUsedBy` / `GetGlobalVarLetted` 會去除重複項目，因此無法判別「有被指派，但從未讀取的全域變數」。
  - 無法將 `GetLocalVarUsedBy` 的各個項目逐一與 `GetLocalVarLetted` 比對，以判斷各項目是讀取還是指派。

### 語法資訊

- 可透過 `LINT.GetVarRefs` 取得區塊種類，以及出現的語法種類（條件式、for 的各個部分、case 的運算式等）。
- 不包含不含變數或函式的陳述式（`break` / `continue` / 沒有運算式的 `return` / `--`、只有常值的輸出等）。
- `others` 在內部會轉換成 `else`，因此會將「位於 case 區塊正下方的 else」判定為 `others`。
- `when` 在內部會轉換成 `if` / `elseif`，因此會根據是否包含 case 的內部變數來判定。

### 分析範圍

- 分支與迴圈的流程，必須由辭典端依據區塊種類與深度組合判斷。
- 跨函式分析（引數 `_argv` 的使用方式、全域變數的指派來源等），必須由辭典端比對各函式的結果。

## 檢查組合範例

| 檢查 | 可否 | 方法 |
|------|------|------|
| 未使用函式 | 可 | 收集 `GETFUNCLIST` 中所有函式的 `LINT.GetVarRefs` 結果之 `func,user`，並列出未出現在任何位置的函式（排除事件函式等由外部呼叫的函式） |
| 未使用的區域變數 | 可 | 以範圍（`{` `}`）為單位，找出只有 `w` 而沒有 `r` / `rw` 的變數 |
| 讀取未定義的區域變數 | 可（分支需由辭典端處理） | 從開頭依序追蹤，找出在該範圍或外層範圍中出現 `w` / `rw` 之前的 `r` / `rw` |
| 未使用的全域變數 | 可 | 收集所有函式的 `var,global`，並找出只有 `w` 的變數（無法追蹤透過 `EVAL` 等方式讀取的變數） |
| 條件式中的指派 | 可 | 尋找 `context` 為 `if` / `elseif` / `while` / `switch` / `for-cond`，且 `access` 為 `w` / `rw` 的項目 |
| 不正確的 case 子句 | 部分可 | 檢查 `case` 區塊正下方（深度+1）是否有 `when` / `others` 以外的區塊，或 `context` 不是 `when` 的項目。無法偵測不含變數或函式的內容 |
| 名稱拼寫錯誤候選 | 可 | 由辭典端計算與 `GETFUNCLIST` / `GETVARLIST` 的編輯距離 |
| 顯示行號與欄位位置 | 僅行號可 | 無法取得欄位位置 |
