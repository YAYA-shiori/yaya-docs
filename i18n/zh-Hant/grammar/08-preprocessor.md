# 前處理器

## 概要

載入辭典檔案時執行的前處理器指令。

## #define

直接對辭典檔案的原始文字進行字串取代：

```
#define before after
```

從宣告之後到該檔案結尾的所有文字都會套用取代。取代會依宣告順序執行，因此請先寫應該優先轉換的項目。

## #globaldefine

與 `#define` 類似，但作用範圍較廣：

```
#globaldefine before after
```

對之後載入的所有辭典檔案都有效。若放在第一個辭典檔案的開頭，效果會涵蓋整個專案。

**處理順序：**先執行 `#define` 的取代，再執行 `#globaldefine` 的取代：

```
#globaldefine tea green
#define tea milk
"teacup"
```

結果: `"milkcup"` （`#define` 優先）

## \_\_AYA\_SYSTEM\_FILE\_\_

YAYA Tc543-1 之後的版本可使用。傳回目前檔案相對於 DLL 的路徑：

```
"__AYA_SYSTEM_FILE__"
```

範例：輸出 `"aya_aitalk.txt"`

## \_\_AYA\_SYSTEM\_LINE\_\_

Tc543-1 之後的版本可使用。機制與 `__AYA_SYSTEM_FILE__` 相同，傳回執行中檔案的目前行號。

## \_\_AYA\_SYSTEM\_FUNC\_\_

Tc574-2 之後的版本可使用（600 系列為 Tc602-2 之後）。寫在函式內時，會取代為該函式的名稱：

```
OnTest
{
	LOGGING("__AYA_SYSTEM_FUNC__: called")
}
```

範例：輸出 `"OnTest: called"`

- 只會取代函式 `{` `}` 內的內容。不包含附加在函式名稱上的避免重複選項（例如 `:nonoverlap`）
- 即使包含在 `#define` 取代後的字串中，也會進行取代，因此可用於記錄輸出的巨集
- 也可用於透過 [APPEND_RUNTIME_DIC](../functions/APPEND_RUNTIME_DIC.md) 新增的函式

## #ifdef / #ifndef / #elifdef / #elifndef / #else / #endif

Tc574-2 之後的版本可使用（600 系列為 Tc602-2 之後）。依名稱是否已定義，切換是否載入辭典的一部分：

```
#ifdef 名前
（名前が定義されていれば読み込む）
#elifdef 別の名前
（最初の名前が未定義で、別の名前が定義されていれば読み込む）
#else
（どれにも当てはまらなければ読み込む）
#endif
```

- `#ifndef` / `#elifndef` 表示「若未定義」
- `#elifdef` / `#elifndef` / `#else` 可省略。`#elifdef` / `#elifndef` 可寫任意多個
- 可以巢狀使用
- 會忽略行首空白，因此可以縮排。也可在函式內使用
- 行尾可寫 `//` 註解
- 不能寫條件運算式（沒有 `#if`）

不會載入的區段，其行不會進行語法解析。呼叫不存在的系統函式，或寫下該 YAYA 不認得的語法，都不會發生錯誤。區段內的 `#define` / `#globaldefine` 也不會登錄。

不過，註解（`/* */`）、以行尾的 `/` 合併行，以及 here document 都會先處理。寫在 here document 內的 `#endif` 等內容不會被當作前處理器指令。

### 判定目標名稱

| 名稱 | 已定義的條件 |
|---|---|
| `#define` 的名稱 | 在該檔案中，於該行之前已定義 |
| `#globaldefine` 的名稱 | 在之前載入的辭典檔案中定義（若為同一檔案，則須在該行之前） |
| `__AYA_SYSTEM_YAYA5__` | 500 系列的 YAYA |
| `__AYA_SYSTEM_YAYA6__` | 600 系列的 YAYA |
| `__AYA_SYSTEM_SYSFUNC_関数名__` | 存在該系統函式（例如：`__AYA_SYSTEM_SYSFUNC_FREADJSON__`） |
| `__AYA_SYSTEM_FILE__` / `__AYA_SYSTEM_LINE__` / `__AYA_SYSTEM_FUNC__` | 永遠都已定義 |

`__AYA_SYSTEM_YAYA5__` / `__AYA_SYSTEM_YAYA6__` / `__AYA_SYSTEM_SYSFUNC_関数名__` 是只供 `#ifdef` 系列判定使用的名稱，不會取代辭典中的字串。

`#globaldefine` 會受到載入順序影響。之後載入的辭典檔案中的 `#globaldefine` 不會被看見。

### 供 500 系列與 600 系列共用的辭典

若使用 600 系列新增的語法或函式，500 系列會在載入時發生錯誤（例如呼叫未知函式會出現 E0071）。使用 `#ifdef` 區分寫法，就能避免兩者發生錯誤：

```
#ifdef __AYA_SYSTEM_YAYA6__
LoadConfig
{
	FREADJSON('config.json')
}
#else
LoadConfig
{
	// 500 系向けの代わりの処理
}
#endif
```

若要依特定系統函式是否存在來區分寫法，請使用 `__AYA_SYSTEM_SYSFUNC_関数名__`。日後版本新增函式時，這種寫法也能直接沿用：

```
#ifdef __AYA_SYSTEM_SYSFUNC_DUMPJSON__
	_s = DUMPJSON(_data)
#else
	_s = ''
#endif
```

不認得 `#ifdef` 的舊版 YAYA（Tc574-1 以前、Tc602-1 以前），會將 `#ifdef` 等行視為錯誤 E0076，並解析區段中的所有內容。散布共用辭典時，請明確標示所需的 YAYA 版本。

## #error / #warning

Tc574-2 之後的版本可使用（600 系列為 Tc602-2 之後）。在載入時輸出錯誤或警告：

```
#ifndef __AYA_SYSTEM_YAYA6__
#error この辞書は YAYA 600 系（Tc602-2 以降）が必要です
#endif
```

- `#error` 會輸出錯誤 E0104。由於會成為辭典錯誤，因此會在緊急模式下載入
- `#warning` 會輸出警告 W0028。載入會繼續
- 後面寫的字串會接續輸出為訊息（不包含行尾的 `//` 註解）
- 位於 `#ifdef` 等指令不會載入的區段時，不會執行任何動作

## 錯誤

| 編號 | 內容 |
|---|---|
| E0074 | `#ifdef` 系列沒有名稱、名稱超過一個，或 `#else` / `#endif` 後面有字串 |
| E0101 | 沒有對應的 `#ifdef` / `#ifndef` 的 `#elifdef` / `#elifndef` / `#else` / `#endif` |
| E0102 | `#else` 之後出現 `#elifdef` / `#elifndef` / `#else` |
| E0103 | `#ifdef` / `#ifndef` 沒有以 `#endif` 關閉（顯示最內層 `#ifdef` 所在的行） |
| E0104 | `#error` |
| W0028 | `#warning` |
