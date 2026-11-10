# 600 的變更（Tc600-3 之後）

整理 Tc600-3 之後的 YAYA（600 系列）相較於 500 系列（截至 Tc574-1）的規格變更。

!!! note "TL;DR"
    **只要替換 `yaya.dll`，500 系列的辭典和存檔檔案就能照常運作。** 不需要重寫。開發團隊也幾乎都是不多加考慮，直接替換。

    只有遇到以下情況時才需要留意。

    - 辭典中有與 `IHASH`、`HASH_KEYS` 等新系統函式同名的函式或變數 → 函式會改名為 `Conflict.名稱`，變數則無法使用（[詳細資訊](#新しいシステム関数と同じ名前)）
    - 依賴陣列元素彼此比較 VOID，或對混合型別的陣列使用 `ARRAYDEDUP` → 結果會改變（[詳細資訊](#既存の辞書に影響しうる変更)）
    - 將在 600 系列中運作過的存檔檔案還原到 500 系列 → 包含雜湊或巢狀結構的變數會損毀（[詳細資訊](#セーブファイルの互換性)）

    新功能（雜湊、巢狀陣列、JSON / XML / SQLite 等）可以等到需要時再使用。與 500 系列共用的辭典可以用 `#ifdef` 區分寫法（[詳細資訊](#500-系と共用する辞書)）。

## 概要

| 項目 | 500 系 | 600 系 |
|---|---|---|
| 值的型別 | VOID / 整數 / 實數 / 字串 / 通用陣列 | ＋ **雜湊**（關聯式陣列） |
| `GETTYPE` / `GETTYPEEX` | 0〜4 | 雜湊為 **5** |
| 陣列元素 | 僅純量 | 陣列和雜湊也可作為元素（**巢狀**） |
| 指派至元素 | 僅限 `a[x] = v` | 也可使用 `a[x][y]... = v`（**多維指派**） |
| foreach | `foreach 式 ; 變數` | ＋ `foreach 式 ; 鍵變數, 值變數` |
| 存檔檔案 | 陣列 `a:b:c` | ＋ 雜湊 `"k"=v:...`、巢狀 `IARRAY{...}` / `IHASH{...}` |
| 新增的系統函式 | ― | [IHASH](../functions/IHASH.md) [HASH_KEYS](../functions/HASH_KEYS.md) [HASH_VALUES](../functions/HASH_VALUES.md) [HASH_SPLIT](../functions/HASH_SPLIT.md) [HASH_EXIST](../functions/HASH_EXIST.md) [HASH_SIZE](../functions/HASH_SIZE.md)、自 Tc601-1 起提供 [FREADJSON](../functions/FREADJSON.md) [FREADXML](../functions/FREADXML.md) [PARSEJSON](../functions/PARSEJSON.md) [PARSEXML](../functions/PARSEXML.md)、自 Tc602-1 起提供 [FWRITEJSON](../functions/FWRITEJSON.md) [FWRITEXML](../functions/FWRITEXML.md) [DUMPJSON](../functions/DUMPJSON.md) [DUMPXML](../functions/DUMPXML.md)、自 Tc602-3 起提供 [PARSEHEADER](../functions/PARSEHEADER.md)、自 Tc602-5 起提供 [FREADYAML](../functions/FREADYAML.md) [FREADTOML](../functions/FREADTOML.md) [PARSEYAML](../functions/PARSEYAML.md) [PARSETOML](../functions/PARSETOML.md) [FWRITEYAML](../functions/FWRITEYAML.md) [FWRITETOML](../functions/FWRITETOML.md) [DUMPYAML](../functions/DUMPYAML.md) [DUMPTOML](../functions/DUMPTOML.md)、自 Tc602-11 起提供 [SQLOPEN](../functions/SQLOPEN.md) [SQLCLOSE](../functions/SQLCLOSE.md) [SQLEXEC](../functions/SQLEXEC.md) [SQLQUERY](../functions/SQLQUERY.md)、自 Tc605-1 起提供 [FREADHTML](../functions/FREADHTML.md) [PARSEHTML](../functions/PARSEHTML.md) |
| 新增的警告 | ― | W0024（將雜湊用於 `-` `*` `/` `%`）、自 Tc601-1 起提供 W0025（無法開啟檔案）・W0026（無法解析 JSON/XML/YAML/TOML）、自 Tc602-1 起提供 W0027（無法轉換為 JSON/XML/YAML/TOML）、自 Tc602-11 起提供 W0029（SQLite 處理失敗）、自 Tc602-13 起提供 W0030（傳入的值多於 SQL 參數）、自 Tc604-1 起提供 W0031（使用 `embed.lazy, off` 時，無法判定 `%` 後的名稱） |
| 正規表示式 | DEELX | 自 Tc606-6 起提供 uka_regexp（接近 PCRE2 的語法）。可使用變數或函式解析模式中的子常式呼叫（[正規表示式](../grammar/14-regular-expressions.md)） |

文法請參閱[雜湊](../grammar/12-hash.md)與[值的巢狀結構與多維指派](../grammar/13-nesting.md)。

500 系的 `a[x][y] = v` 在載入時會產生錯誤 E0029，因此不存在包含此語法的既有辭典。

## 可能影響既有辭典的變更

### 比較陣列元素中的 VOID

比較陣列元素時，**若兩者都是 VOID**，現在會視為相等。這與純量之間比較 VOID 的行為一致。

- `(1, 未定義の変数) == (1, 未定義の変数)` 的結果從 0 變為 1
- `ASEARCH(未定義の変数, 配列)` 現在會傳回陣列中 VOID 元素的位置（500 系會傳回 -1）
- `HASH_EXIST`、`ARRAYDEDUP` 及雜湊之間的 `==` 也會有相同變更

只有在鍵與元素都是 VOID 時才會有此變更；整數、實數與字串的比較不變。

### 傳入混合型別陣列至 ARRAYDEDUP 時

在 500 系中，傳入混有整數、實數與字串的陣列時，結果會依排列順序而異。600 系會依照與雜湊鍵相同的規則移除重複項目，並按數值 < 字串的順序排列。

```
ARRAYDEDUP((10, "9", 9, "a", 1.0, 1, "1"))
// 500 系: 1,1.000000,9,10,9,a
// 600 系: 1.000000,9,10,a
```

`1.0`、`1`、`"1"` 會視為相同的值，並保留最前面的項目（`1.0`）。只有整數、只有實數或只有字串的陣列，其結果與 500 系相同。

### 傳入 setter・watcher 的陣列

傳入 [FUNCDECL_WRITE](../functions/FUNCDECL_WRITE.md)（setter）和 [FUNCDECL_READ](../functions/FUNCDECL_READ.md)（watcher）的值為通用陣列時，在 500 系列中值會損壞（setter 的 `_argv[1]`、`_argv[2]` 會變成空值，watcher 的 `_argv[1]` 只會變成第一個元素，直接傳回 setter 的傳回值會讓變數變成空值）。

在 600 系列中，陣列會保持巢狀狀態，作為 `_argv` 的元素傳入。`_argv` 的元素數量維持不變，setter 為 3，watcher 為 2。

在 500 系列中，即使替陣列變數設定 setter 或 watcher，也無法正確運作，因此應該不會造成實際影響。另外，透過索引指派（`a[0] = v`）時不會呼叫 setter，這點與 500 系列相同。

### 與新系統函式同名

- 與 `IHASH`、`HASH_KEYS` 等同名的使用者自訂函式會改名為 `Conflict.名稱`，呼叫時會指向系統函式（與新增 TOAUTOEX 時使用相同機制）
- 無法使用同名的全域變數。從存檔檔案還原時會出現警告 W0002

### 對不存在的元素進行複合指派（Tc602-10 以後）

複合指派（`+=`、`-=`、`*=`、`/=`、`%=` 及帶冒號的變體）的左側若為通用陣列範圍外的元素，或雜湊中不存在的索引鍵，現在會和未定義的變數一樣，以 VOID 進行計算。在 500 系列和 Tc602-9 以前，這類情況會以空字串進行計算，因此 `+= 數值` 會變成字串串接。

```
_c = IHASH()
_c["a"] += 1
_c["a"] += 1     // 500 系・Tc602-9 まで: "11"（文字列）　Tc602-10 以降: 2（整数）

_a = IARRAY
_a[2] += 1       // 500 系・Tc602-9 まで: "1"（文字列）　Tc602-10 以降: 1（整数）
```

- 只有右側為數值的 `+=` 會改變。`-=`、`*=`、`/=`、`%=` 原本就會將空字串視為數值，因此結果相同。`+= "文字列"` 也相同
- 元素存在且值為空字串時（`_a[0] = ""` 之後執行 `_a[0] += 1`），結果仍和以往一樣為 `"1"`
- 簡易陣列（字串）中，範圍外的元素原本就會以 VOID 進行計算
- 在 Tc602-10 中，讀取（`h["none"]` 或超出範圍的 `a[9]`）仍會傳回空字串。從 Tc603-1 起，讀取也會變成 VOID（如下所述）
- 多維指派中，只有最後一層是處理對象。中間層不存在時（對空的 `_h` 執行 `_h["a"]["b"] += 1`），請依照[各中間值的處理方式](../grammar/13-nesting.md#途中の値ごとの動作)改寫。`_h["a"]` 在 Tc602-13 以前會是字串 `"1"`，從 Tc603-1 起則會是陣列 `(1)`
- `,=` 不變

### 讀取不存在的元素（Tc603-1 以後）

讀取通用陣列中超出範圍的元素、雜湊中不存在的鍵，或對 VOID 加上 `[ ]` 時，現在會和未定義的變數一樣傳回 VOID。在此之前會傳回空字串（簡易陣列和數值超出範圍時原本就會傳回 VOID）。500 系列也從 Tc574-8 起相同（雜湊除外）。詳情請參閱[超出範圍的元素](../grammar/05-arrays.md#範囲外の要素)。

```
_h = IHASH()
_h["none"] == 0      // Tc602-13 まで: 0　Tc603-1 以降: 1
_h["none"] + 1       // Tc602-13 まで: "1"（文字列）　Tc603-1 以降: 1（整数）
GETTYPE(_h["none"])  // Tc602-13 まで: 3　Tc603-1 以降: 0
```

`== ""`、if 的判定，以及與字串連接的結果都不會改變。

### 將值指派給陣列中的陣列或雜湊（Tc603-1 以後）

在非範圍指定的指派（`_v[0] = x`、`_v[0] ,= x`、`_v[0] += x` 等）中，當指派目標的元素是陣列或雜湊時，現在會將右側的值整個取代，而不展開右側的值。在此之前，若根節點是陣列，右側的陣列會被展開，導致巢狀結構崩解（即使是 `_v[0] = _v[0]` 也會崩解）。指派目標的元素是純量時的插入與刪除（`_a[1] = (8, 9)`、`_a[1] = IARRAY`）則不會改變。詳情請參閱[整個改寫內部的陣列或雜湊](../grammar/13-nesting.md#内側の配列やハッシュを丸ごと書き換える)。

```
_v = PARSEJSON('[[1,2],[3,4]]')
_v[0] ,= 5     // Tc602-13 まで: 1,2,5,(3,4)　Tc603-1 以降: (1,2,5),(3,4)
```

## 存檔檔案的相容性

- 不含雜湊或巢狀結構的變數，寫出的內容與讀取結果都和 500 系相同。可以直接讀取 500 系的存檔檔案
- 含有雜湊或巢狀結構的變數會以新格式儲存（請參閱 [SAVEVAR](../functions/SAVEVAR.md)）
- **請注意降級**：使用 600 系儲存的檔案若以 500 系讀取，只有含有雜湊或巢狀結構的變數會損壞（不會崩潰，也不會影響其他變數）。若在損壞的狀態下重新儲存，原始內容將會遺失

## 與 500 系共用的辭典

在 Tc574-2 之後的 500 系和 Tc602-2 之後的 600 系中，可以使用 `#ifdef __AYA_SYSTEM_YAYA6__` 或 `#ifdef __AYA_SYSTEM_SYSFUNC_関数名__` 區分撰寫 600 系適用的部分。由於不會解析未載入區段的語法，即使撰寫 600 系的新語法或函式，在 500 系中也不會發生錯誤。詳情請參閱 [前置處理](../grammar/08-preprocessor.md#500-系と-600-系で共用する辞書)。

## 效能

`_a ,= x` 和 `_a[i] = x` 在 500 系中每次都會複製整個陣列（在迴圈中逐漸擴充陣列時，速度會隨著元素數量的平方而變慢）。600 系不會進行這項複製，因此在迴圈中逐漸擴充陣列的處理速度大幅提升。

## 相關

- [雜湊](../grammar/12-hash.md)
- [值的巢狀結構與多維指派](../grammar/13-nesting.md)
- [流程控制（foreach）](../grammar/07-flow-control.md#foreach-ループ)
- [SAVEVAR](../functions/SAVEVAR.md)
- [前置處理](../grammar/08-preprocessor.md)
