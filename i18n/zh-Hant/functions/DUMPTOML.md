# DUMPTOML
**Category:** 型取得/変換

## Signature
```
DUMPTOML( value [, pretty] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| value | 要轉換為 TOML 的雜湊（包含巢狀結構）。TOML 的最上層是表格，因此不能傳入雜湊以外的值 |
| pretty | 為 1 時使用 `[表格]` 標題美化格式；為 0 時，每個最上層鍵各輸出一行。省略時為 1 |

## Returns
- 成功時：TOML 字串
- 失敗時或沒有引數時：空字串

## Description
將雜湊轉換為 TOML 字串並傳回。這是 [PARSETOML](PARSETOML.md) 的反向轉換。

與 [DUMPJSON](DUMPJSON.md) / [DUMPXML](DUMPXML.md) 不同，省略 pretty 時會美化格式（1）。

### 值的對應

| YAYA | TOML |
|------|------|
| 雜湊 | 表格。鍵只包含英數字、`_`、`-` 時會原樣寫入，否則會寫成 `"..."`。順序依照雜湊鍵的順序 |
| 只包含雜湊的通用陣列 | 表格陣列（pretty 為 1 時使用 `[[名稱]]`） |
| 通用陣列 | 陣列 |
| 整數 | 整數。64 位元整數也會以無誤差的方式寫入 |
| 實數 | 實數。一定會加上小數點或指數（`1.0`、`0.1`、`1e+300`）。NaN 會變成 `nan`，無限大會變成 `inf` / `-inf` |
| 字串 | 字串（如下所述） |
| 空（VOID） | 不寫入（TOML 沒有 null，因此會省略該鍵） |

- 整數的 1 / 0 會變成 `1` / `0`，不會變成 `true` / `false`
- 日期時間字串（以 [FREADTOML](FREADTOML.md) 讀取的內容）也會作為字串寫成 `"..."` 
- 陣列元素為空（VOID）時無法表示，會產生錯誤 W0027
- 小數點不受地區設定影響，一律使用 `.`

字串通常會寫成 `"..."`，並跳脫 `"`、`\` 和控制字元。包含 `\`，但不包含 `'` 和換行的字串（例如 Windows 路徑），會為了易讀而不跳脫，改寫成 `'...'`。

### 美化格式（pretty 為 1）

- 依序寫入該表格的鍵和值 → 下層表格（`[a.b]`）→ 表格陣列（`[[a.c]]`），表格之間會空一行
- 沒有鍵和值、只有下層表格的表格會省略標題（只寫 `[a.b]` 也會定義 `a`）
- 含有換行的字串會寫成多行的 `"""..."""` 
- 超過 80 個字元的陣列，或包含陣列、雜湊作為元素的陣列，會改為每個元素各寫一行（使用 4 個空白縮排，並在每個元素後加上逗號）
- 使用 LF 換行，最後一行之後也會加上換行

pretty 為 0 時，每個最上層鍵各寫一行；下層雜湊會寫成行內表格（`{ k = v }`），表格陣列則會寫成行內表格陣列。

使用 [PARSETOML](PARSETOML.md) 讀回時，會還原為原本的值（省略空值的部分除外）。

### 錯誤
| 狀況 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 沒有引數 | W0008 | 8 |
| value 不是雜湊，或陣列元素中包含空（VOID） | W0027（也會輸出原因） | 27 |

## Example
```
_n = IHASH()
_n["title"] = "設定"
_n["ghost"] = IHASH("name", "さくら", "age", 17)
_n["ghost"]["shell"] = IHASH("name", "master")

DUMPTOML(_n)
// title = "設定"
//
// [ghost]
// age = 17
// name = "さくら"
//
// [ghost.shell]
// name = "master"

DUMPTOML(_n, 0)
// ghost = { age = 17, name = "さくら", shell = { name = "master" } }
// title = "設定"

DUMPTOML(("a", 1))          // 空文字列（警告 W0027）
```

## Compatibility
- YAYA：Tc602-5 以後

## See Also
- [FWRITETOML](FWRITETOML.md)
- [PARSETOML](PARSETOML.md)
- [DUMPJSON](DUMPJSON.md)
- [DUMPYAML](DUMPYAML.md)
