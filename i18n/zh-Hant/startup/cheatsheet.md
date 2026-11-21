# 速查表

這是將 YAYA 的寫法整理成一頁的速查表。詳細說明請參閱各項目的連結。

## YAYA 的基本概念

- 辭典是**函式的集合**。以 `名前 { ... }` 的形式定義，若使用 `OnBoot` 這類事件名稱，就會成為該事件的回應。
- 函式中的**運算式或字串每行各是一個「輸出候選」**。呼叫函式時，會從候選中隨機選取一個並傳回。指派（`_a = 1`）等敘述不會成為候選。
- 字串要用 `"..."` 包住。Sakura Script 也是字串，因此一定要包住。
- 變數有型別（整數、實數、字串、陣列、雜湊），不需要宣告。名稱以 `_` 開頭的是區域變數。
- 函式外不能寫敘述或變數，只有 `#define` 等前置處理器指令可以寫在外面。
- `if` `while` 的條件運算式可用括號包住，也可以不包（`if (_a == 1)` 和 `if _a == 1` 相同）。`for` `foreach` 也可以用 `( )` 包住整個標頭（Tc603-6 以後；更早的版本會發生錯誤）。
- 符號請使用半形字元（不能使用全形的 `（` 或 `＋`）。

## 函式的寫法

```
OnBoot
{
  _name = "さくら"
  "\0\s[0]こんにちは、%(_name)さん。\e"
  "\0\s[0]起動しましたね。\e"
}
```

- 在上例中，會隨機傳回 `"\0\s[0]こんにちは…"` 或 `"\0\s[0]起動しましたね。\e"`（`_name = …` 不會成為候選）。
- 候選**每行一個**。若像 `"a" "b"` 一樣寫在同一行，就會發生錯誤。`"a" / "b"` 中的 `/` 是除法，不是候選的分隔符號。
- 在單獨一行寫上 `--`，會將前後的候選分成不同群組，從各群組選取一個並串接（[函式](../grammar/02-functions.md)）。
- `{` 可以寫在函式名稱的同一行，也可以寫在下一行。
- 註解的寫法有 `// 行末まで` 和 `/* 複数行 */`。
- 在同一行寫多個敘述時，請用 `;` 分隔（`_a = 1 ; _b = 2`）。

### 引數與傳回值

| 寫法 | 意義 |
|--------|------|
| `Func(1, "a")` | 帶引數呼叫。若沒有引數，只寫 `Func` 即可 |
| `_argv[0]` `_argv[1]` | 接收到的引數（從 0 開始） |
| `_argc` | 引數的數量 |
| `Func(&_v)` | 以參照方式傳遞變數。在 `Func` 中執行 `_argv[0] = 99`，就會改變 `_v` |
| `return` | 在此結束函式。從此前的候選中傳回一個 |
| `return 式` | **捨棄所有**此前的候選，傳回運算式的值（Tc573-1 以後） |

### 候選的選取方式

在函式名稱後用 `:` 指定（`Seq : sequential`）。

| 指定 | 行為 |
|------|------|
| （無） | 從候選中隨機選取一個 |
| `nonoverlap` | 不會連續選取與上次相同的候選 |
| `sequential` | 從上到下依序傳回，到最後後回到開頭 |
| `array` | 將所有候選組成通用陣列後傳回 |
| `void` | 執行內容，但不傳回任何值 |
| `all` | 傳回將所有候選串接成的一個字串（Tc567-1 以後） |
| `last` | 傳回最後一個候選（Tc567-1 以後） |

除了選取方式，還可以加上以下修飾符。

| 指定 | 行為 |
|------|------|
| `_pool` | 將內層區塊（包含 `if` 的內容）的候選拆開，使其與外層候選以相同機率被選取 |
| `_pool_nonoverlap` `_pool_sequential` | 對拆開後的所有候選套用避免重複或依序選取 |
| `melt_` | 若選取的輸出是通用陣列，則將元素拆開並加入外層區塊的候選 |

```
OnTest : _pool
{
  "x"
  {
    "y"
    "z"
  }
}
```

- 沒有 `_pool` 時，內層的 `{ }` 整體算作一個候選（`x` 的機率為 1/2，`y` `z` 各為 1/4）。加上 `_pool` 後，`x` `y` `z` 各為 1/3。
- 若 `if` 的條件為假，就不會加入其中的候選。使用 `if 条件 { "b" "c" }` 可以寫出「僅在條件為真時增加候選」的形式。
- `while` `for` `foreach` 中的候選，每次反覆執行都會加入一個。
- 像 `nonoverlap : {` 這樣指定了選取方式的區塊不會被拆開，仍算作一個候選。

詳見[函式](../grammar/02-functions.md)。

## 值與型別

| 類型 | 寫法 | 範例 |
|------|--------|----|
| 整數 | 十進位、`0b`（二進位）、`0x`（十六進位）。64 位元 | `10` `0b1010` `0xa` |
| 實數 | 加上小數點 | `3.14` |
| 字串 | `"..."`（會展開）、`'...'`（不展開） | `"a%(_x)"` `'a%(_x)'` |
| 多行字串 | `<<"` … `">>`（會展開）、`<<'` … `'>>`（不展開） | |
| 通用陣列 | `(1, "a", 2.5)` | [陣列](../grammar/05-arrays.md) |
| 簡易陣列 | 以逗號分隔的字串 `"a,b,c"` | 同上 |
| 雜湊 | `IHASH("キー", 値, …)`（Tc600-3 以後） | [雜湊](../grammar/12-hash.md) |
| VOID | 未定義的變數、超出範圍的元素 | 作為字串時為空，作為數值時為 0 |

- 字串中的 `"` 要連寫兩次（`"1""2"` → `1"2`）。
- 使用 [GETTYPE](../functions/GETTYPE.md) 查詢型別（VOID 為 0、整數為 1、實數為 2、字串為 3、通用陣列為 4、雜湊為 5）。
- 實數轉成字串時會保留小數點後 6 位（`3.0/4*100` → `75.000000`）。
- 整數之間的除法會捨去小數部分（`4/3` → `1`）。將其中一個改為實數，結果就會是實數。

## 變數

| 寫法 | 意義 |
|--------|------|
| `_a = 1` | 區域變數。只在該函式內（及其內層區塊）有效。離開區塊後便會消失 |
| `a = 1` | 全域變數。任何函式都可以使用。結束時自動儲存，並在下次啟動時還原 |
| `ERASEVAR("a")` | 刪除全域變數 |
| `_a++` `_a--` `_a += 2` | 加法、減法、複合指派（另有 `-=` `*=` `/=` `%=`） |

- 未定義的變數在計算時為 0，作為字串時為空字串（`UNDEF + 1` 為 `1`）。
- 不能使用以數字開頭的名稱，也不能使用與保留字或函式名稱相同的名稱（[保留字](../grammar/09-reserved-words.md)）。

## 運算子

依優先順序由高至低排列（[算術運算](../grammar/04-arithmetic.md)）。

| 種類 | 運算子 |
|------|--------|
| 括號・索引 | `( )` `[ ]` |
| 否定 | `!` |
| 遞增遞減 | `++` `--` |
| 乘除 | `*` `/` `%` |
| 加減 | `+` `-` |
| 比較 | `==` `!=` `>=` `<=` `>` `<` `_in_` `!_in_` |
| 邏輯 | `&&` `\|\|` |
| 指派 | `=` `+=` `-=` `*=` `/=` `%=` `,=` |
| 逗號（建立陣列） | `,` |

- `0` 為假，非 0 為真。比較結果為 `1` 或 `0`。
- `"or" _in_ "World"` 在右側字串包含左側字串時為 `1`。
- `+` 的任一運算元為字串時會進行**串接**（`"5" + 1` 的結果為 `"51"`）。`*` 則以數值計算（`"5" * 2` 的結果為 `10`）。
- `==` 會區分大小寫（`"abc" == "ABC"` 的結果為 `0`）。
- 沒有三元運算子（`? :`）。

## 控制結構

```
if _a < 3
{
  "小"
}
elseif _a < 10
{
  "中"
}
else
{
  "大"
}
```

| 目的 | 寫法 |
|--------------|--------|
| 雙分支・多分支 | `if` / `elseif` / `else`（巢狀的 `if` 除外，只有一個敘述時可省略 `{ }`） |
| 依值分支 | `case 式 { when 値 { … } when 値1, 値2 { … } others { … } }` |
| 依位置選擇 | `switch 式 { 候補0 候補1 … }`（候選項目每行一個，從 0 開始） |
| 依條件重複 | `while 条件 { … }` |
| 依次數重複 | `for _i = 0 ; _i < 10 ; _i++ { … }`（三個部分皆為必要。Tc603-6 以後可用 `( )` 包住整個標頭） |
| 依序遍歷陣列 | `foreach 配列 ; _v { … }` |
| 遍歷鍵和值 | `foreach 配列またはハッシュ ; _k, _v { … }`（Tc600-3 以後） |
| 跳出迴圈・進入下一次迭代 | `break` / `continue` |

```
case _name
{
  when "さくら" { "さくらだね" }
  when "うにゅう", "うに" { "うにゅうだね" }
  others { "だれ？" }
}
```

- `case` 的 `when` 中**只能寫常值**（不可使用變數或運算式）。範圍寫成 `3-5` 或 `"a"-"d"`。
- `when` 和 `others` 要寫在 `case 式` 後面的 `{ }` 中。若未加上 `{` 就接著寫 `when`，載入時會發生錯誤（E0051）。
- 迴圈的重複次數有上限（預設為 1000000 次；`looplimit`）。超過上限時會呼叫 `OnLoopLimit`。
- `while 1` 是無限迴圈。請務必寫入 `break`。

## 字串嵌入

| 寫法 | 意義 |
|--------|------|
| `"%(_a)"` `"%(1+2)"` | 評估運算式並嵌入（帶範圍的展開） |
| `"%_a"` | 以名稱的最長匹配方式嵌入。由於在執行時尋找名稱，因此較慢 |
| `'%(_a)'` | 使用單引號時不展開 |

詳情請參閱[字串嵌入](../grammar/06-string-embedding.md)。

## 陣列

```
_a = (10, 20, 30)
_a[1]            // 20
_a[0,1]          // 範囲（10,20）
_a ,= 40         // 末尾に追加
_a = ("先頭", _a) // 先頭に追加
_a + "!"         // 全要素に演算（10!,20!,…）
ARRAYSIZE(_a)    // 要素数
```

- 範圍外的元素為 VOID（`GETTYPE(_a[9])` 的結果為 0）。
- 簡易陣列保持字串形式，透過索引讀寫（`_s = "a,b,c"` → `_s[1]` 的結果為 `b`）。分隔符號可用 `_s[1,"|"]` 這類寫法指定。
- 取得陣列元素數量使用 [ARRAYSIZE](../functions/ARRAYSIZE.md)，搜尋使用 [ASEARCH](../functions/ASEARCH.md)，排序使用 [ASORT](../functions/ASORT.md)，分割使用 [SPLIT](../functions/SPLIT.md)。

## 雜湊（Tc600-3 以後）

```
_h = IHASH("name", "さくら", "age", 16)
_h["name"]        // さくら
_h["age"] += 1    // 複合代入も使える
_h["none"]        // VOID（キーが無い）
foreach _h ; _k, _v { … }
```

- 雜湊必須先用 `IHASH()` 建立。
- 元素依鍵的順序排列（不是依加入的順序）。
- 元素中也可以放入陣列或雜湊（[值的巢狀結構](../grammar/13-nesting.md)）。

## 前置處理器

| 寫法 | 意義 |
|--------|------|
| `#define 前 後` | 取代該檔案中此行之後的字串 |
| `#globaldefine 前 後` | 在此之後載入的所有辭典中進行取代 |
| `#ifdef 名前` … `#else` … `#endif` | 若名稱已定義則載入（Tc574-2 / Tc602-2 以後） |
| `__AYA_SYSTEM_YAYA6__` | 600 系列中已定義（用於與 500 系列共用的辭典） |
| `__AYA_SYSTEM_FILE__` `__AYA_SYSTEM_LINE__` `__AYA_SYSTEM_FUNC__` | 分別取代為檔案名稱、行號及函式名稱 |

詳情請參閱[前置處理器](../grammar/08-preprocessor.md)。

## 設定檔（yaya.txt）

```
dic, basis.dic
charset, UTF-8
log, executelog.txt
```

| 設定 | 意義 |
|------|------|
| `dic, ファイル` | 載入辭典（`dicif` 只在檔案存在時載入，`dicdir` 載入資料夾內所有辭典） |
| `charset, UTF-8` | 字元編碼（也可透過 `charset.dic` 等設定依用途分別指定） |
| `log, ファイル` | 輸出執行紀錄 |
| `fncdepth, 数` | 函式呼叫深度上限（預設為 32。設為 0 時深度無上限，但堆疊剩餘空間不足時會停止） |
| `looplimit, 数` | 迴圈次數上限（預設為 1000000） |
| `embed.lazy, off` | 在載入時確定 `"%名前"` 的名稱（預設值 on 為在執行時尋找） |

- 設定檔名稱是在 DLL 名稱後加上 `.txt`（`yaya.txt`）。可用 `//` 和 `/* */` 撰寫註解。
- 若沒有設定檔，或沒有任何要載入的辭典，就會進入 **Shell 模式**。此模式會直接以 `EVAL` 評估送入的運算式並傳回結果，因此可用來確認運算式的運作（[基本設定](../grammar/01-basic-settings.md#シェルモード)）。

詳情請參閱[基本設定](../grammar/01-basic-settings.md)。

## 常用函式

完整清單請參閱[系統函式清單](../system/system-functions-index.md)。

| 用途 | 函式 |
|------|------|
| 查詢、轉換型別 | [GETTYPE](../functions/GETTYPE.md) [CVINT](../functions/CVINT.md) [CVSTR](../functions/CVSTR.md) [CVREAL](../functions/CVREAL.md) |
| 陣列 | [ARRAYSIZE](../functions/ARRAYSIZE.md) [ASEARCH](../functions/ASEARCH.md) [ASORT](../functions/ASORT.md) [SPLIT](../functions/SPLIT.md) |
| 雜湊 | [IHASH](../functions/IHASH.md) [HASH_KEYS](../functions/HASH_KEYS.md) [HASH_EXIST](../functions/HASH_EXIST.md) |
| 字串 | [STRLEN](../functions/STRLEN.md) [SUBSTR](../functions/SUBSTR.md) [STRSTR](../functions/STRSTR.md) [REPLACE](../functions/REPLACE.md) |
| 執行字串中的運算式 | [EVAL](../functions/EVAL.md) |
| 刪除變數 | [ERASEVAR](../functions/ERASEVAR.md) |
| 將變數轉為字串、從字串還原變數 | [SERIALIZEVAR](../functions/SERIALIZEVAR.md) [DESERIALIZEVAR](../functions/DESERIALIZEVAR.md) |
| 亂數 | [RAND](../functions/RAND.md) |
| 在另一個執行緒中執行耗時處理 | [THREADSTART](../functions/THREADSTART.md) [THREADSTATE](../functions/THREADSTATE.md) [THREADJOIN](../functions/THREADJOIN.md) [THREADRESULT](../functions/THREADRESULT.md) [THREADSTOP](../functions/THREADSTOP.md) [THREADCLOSE](../functions/THREADCLOSE.md) |
| 檔案 | [FOPEN](../functions/FOPEN.md) [FREAD](../functions/FREAD.md) [FCLOSE](../functions/FCLOSE.md) |
| 讀取 JSON | [PARSEJSON](../functions/PARSEJSON.md) [FREADJSON](../functions/FREADJSON.md) [FREADJSONL](../functions/FREADJSONL.md)（每行包含 1 個 JSON 的檔案） |

## 相關

- [人格製作方法](creating-ghost.md)
- [從 Satori 移轉](migration-from-satolili.md)
- [從 AYA 移轉](migration-from-aya.md)
