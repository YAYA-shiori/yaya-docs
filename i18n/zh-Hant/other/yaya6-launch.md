# YAYA 6 登場

<div class="y6-hero" markdown>

![YAYA 6 — 有史以來最聰明的 YAYA。](../assets/yaya6/hero.svg)

</div>

<div class="y6-lead" markdown>

**YAYA 6（Tc600 系列）已正式發布。**

可以自由組合雜湊與巢狀值，直接讀寫 JSON、XML、YAML、TOML，將回憶存進 SQLite，陣列就算透過迴圈不斷擴充，也不會變得遲鈍。有史以來最聰明的 YAYA，現在來到你的幽靈身邊。

當然，**以 500 系列編寫的辭典幾乎都能直接運作。**

</div>

<div class="y6-cta" markdown>

[下載（GitHub Releases）](https://github.com/YAYA-shiori/yaya-shiori/releases) [從 500 系列移轉指南](changes-600.md)

</div>

!!! note "注意事項"
    本頁是氣氛歡樂的介紹頁面，為了營造氣氛，省略了許多細節。詳細規格請參閱[600 的變更內容](changes-600.md)及各參考文件。

<div class="y6-stats" markdown>

- **6** 種值的型別（新增雜湊）
- **4** 種結構化資料格式的讀寫
- **1** 個內建資料庫（SQLite）
- **1/5000** 擴充陣列時的複製次數（理論值）

</div>

## 特色

### 🗝️ 將雜湊掌握在手中

YAYA 6 終於加入原生的**雜湊（關聯式陣列）**。可以透過名稱取得值。光是這一點，就能讓人格的記憶變得如此清晰。

```
OnMouseDoubleClick
{
    if GETTYPE(nadenade) != 5 {
        nadenade = IHASH()          // ハッシュは IHASH で作る（GETTYPE は 5）
    }
    nadenade[reference[4]] += 1     // 当たり判定の名前ごとに数える

    _n = nadenade[reference[4]]
    "\0\s[0]%(reference[4])を触られたの、これで%(_n)回目だよ。\e"
}
```

`nadenade` 會以雜湊形式儲存在存檔中，因此下次啟動時也會完整保留記憶。寫成 `foreach _h ; _k, _v { ... }`，就能在迴圈中同時取得鍵和值。

→ [雜湊](../grammar/12-hash.md)

### 🧩 隨心所欲地組合值

500 系列的陣列元素只能是數值或字串。YAYA 6 則允許在陣列中放入陣列、在雜湊中放入陣列、在陣列中放入雜湊——可以自由組合成**巢狀結構**。只要連接 `[ ]`，就能直接讀寫任何深度的值（**多維指派**）。

```
_ghost = IHASH()
_ghost["sakura"] = IHASH("name", "さくら")
_ghost["sakura"]["surface"] = (0, 5, 7)
_ghost["kero"] = IHASH("name", "うにゅう")
_ghost["kero"]["surface"] = (10, 11)

_ghost["sakura"]["surface"] ,= 8       // 奥の配列に追加
_ghost["kero"]["name"] = "けろちゃん"    // 奥の値を直接書き換え
_ghost["sakura"]["surface"][0]         // 0

foreach _ghost ; _id, _g {
    // _g["name"] で名前、_g["surface"] で表情の一覧
}
```

- 不只 `=`，`+=` 和 `,=` 也能直接用於深層的值
- 可以將巢狀結構**儲存在存檔中**，也能以原本的結構寫出為 JSON 等格式
- 使用 `DUMPVAR` 就能一眼確認內容

中間層的雜湊不會自動建立，因此就像上面的範例一樣，先用 `IHASH()` 建立是常見的做法。

→ [值的巢狀結構與多維指派](../grammar/13-nesting.md)

### 🌐 多格式解析

![JSON、XML、YAML、TOML、SQLite、HTML 與 YAYA 6 雜湊之間的轉換示意圖](../assets/yaya6/formats.svg)

JSON、XML、YAML、TOML 都能在讀取後轉換成巢狀的雜湊與陣列。修改後也能直接寫回。設定檔，以及其他工具或 SAORI 輸出的資料，都不必再用 `STRSTR` 和 `SUBSTR` 剖開處理。

```
_conf = FREADJSON("config.json")
_name = _conf["user"]["name"]
_conf["boot"] += 1
FWRITEJSON("config.json", _conf, "UTF-8", 1)   // 整形して書き戻す
```

也能讀取 HTML（僅限讀取）。即使 HTML 缺少結束標籤而格式不正確，也會依照與瀏覽器相同的規則補齊並轉成標籤樹，因此要從網頁中擷取需要的部分也很簡單。

```
_h = PARSEHTML(_raw)
_body = _h["children"][1]                // <body>
foreach _body["children"]; _e {
    // _e["name"]（タグ名）、_e["attr"]（属性）、_e["text"]（テキスト）
}
```

此外，`PARSEHEADER` 能立即將 SHIORI、SSTP、HTTP 等「`鍵: 值`」格式的字串拆解成雜湊。

```
_r = PARSEHEADER(_raw)
_r["start"]               // 1 行目（"HTTP/1.1 200 OK" など）
_r["header"]["Charset"]   // ヘッダの値
_r["body"]                // 空行より後ろ
```

### 🧠 讓人格擁有長期記憶

內建了 SQLite。開啟資料庫後，就能隨心所欲地用 SQL 記住並取回資料。即使是數萬筆對話記錄，也不必擔心。

```
OnLoad
{
    SQLOPEN("memory.db")
    SQLEXEC("memory.db", "CREATE TABLE IF NOT EXISTS said(word TEXT)")
}

Remember
{
    SQLEXEC("memory.db", "INSERT INTO said VALUES(?)", _argv[0])
}

OnKuchiguse
{
    _sql = "SELECT word, count(*) AS n FROM said GROUP BY word ORDER BY n DESC LIMIT 1"
    _top = SQLQUERY("memory.db", _sql)
    "\0\s[0]あなたの口ぐせは「%(_top[0]['word'])」だね。\e"
}
```

查詢結果的每一列會直接以「欄名 → 值」的雜湊形式傳回。

→ [SQLOPEN](../functions/SQLOPEN.md)・[SQLEXEC](../functions/SQLEXEC.md)・[SQLQUERY](../functions/SQLQUERY.md)

### ⚡ 擴充陣列也不會變慢

![以迴圈將陣列擴充至 1 萬個元素時的元素複製次數（理論值）。YAYA 5 約 5,000 萬次，YAYA 6 約 1 萬次](../assets/yaya6/bench.svg)

在 500 系列中，每次執行 `_a ,= x` 或 `_a[i] = x` 都會複製整個陣列。元素越多，每次操作所需的時間也越長，因此透過迴圈擴充陣列時，速度會隨元素數量的平方成比例下降。YAYA 6 不再進行這種複製。建立大型陣列的辭典，應該能明顯感受到差異。

## 基準測試

與 YAYA 5 的比較（內部測試）。

| 項目 | YAYA 5（Tc574） | YAYA 6（Tc603） |
|---|---|---|
| 值的型別數量 | 5 | **6** |
| `GETTYPE` 傳回的最大值 | 4 | **5** |
| 可作為陣列元素的項目 | 僅純量 | **陣列和雜湊也可以** |
| `a[x][y] = v` | 讀取錯誤 | **可以使用** |
| foreach 可接收的變數 | 1 | **2**（鍵和值） |
| 可讀寫的結構化資料格式 | 0 | **4**（JSON / XML / YAML / TOML） |
| 內建資料庫 | 無 | **SQLite** |
| 擴充 1 萬個元素的陣列時的複製次數（理論值） | 約 5,000 萬次 | **約 1 萬次** |
| 500 系列的存檔檔案 | ― | **可直接讀取** |

## 發展軌跡

![從 Tc600-3 到 Tc603-1 的主要新增功能年表](../assets/yaya6/timeline.svg)

YAYA 600 系列從 Tc600-3 的雜湊與巢狀結構起步，隨著版本發布不斷增添功能。接著在 Tc603-1 成為第一個正式版。

## 安全性與相容性

即使功能更強大，也不會讓你的辭典無法繼續使用。

- **500 系列的辭典幾乎可以原樣運作。** 除了極少數情況，500 系列原有功能的運作方式都不會改變（變更之處請參閱下方的「已知限制事項」）。多維指派 `a[x][y] = v` 在 500 系列中會造成讀取錯誤，因此也不會改變現有辭典的含義
- **500 系列的存檔檔案可以直接讀取。** 不含雜湊或巢狀結構的變數，匯出的內容也與 500 系列相同
- **即使名稱與新函式重複也沒問題。** 名稱與 `IHASH` 等相同的使用者自訂函式會自動重新命名為 `Conflict.名稱`
- **也可以編寫能在兩個系列中運作的辭典。** 使用 `#ifdef __AYA_SYSTEM_YAYA6__` 區分 600 系列專用內容，這樣在 500 系列中也不會發生錯誤（[前置處理](../grammar/08-preprocessor.md#500-系と-600-系で共用する辞書)）

### 已知限制事項

- **請注意降級。** 使用 600 系列儲存的存檔檔案，若以 500 系列讀取，含有雜湊或巢狀結構的變數會損毀。若以損毀狀態重新儲存，就無法復原
- 不能使用與新系統函式同名的全域變數
- 讀取不存在的元素、比較 VOID 等細節行為有幾處變更。大多數辭典不會受到影響，完整清單請參閱[600 系列的變更點](changes-600.md#既存の辞書に影響しうる変更)

## 模型卡

<div class="y6-card" markdown>

| 項目 | 內容 |
|---|---|
| 名稱 | YAYA 6（Tc600 系列） |
| 種類 | SHIORI（也可作為 [SAORI](yaya-as-saori.md)、[MAKOTO](yaya-as-makoto.md)、[外掛程式](yaya-as-plugin.md)運作） |
| 開發 | YAYA 維護團隊、[steve green 氏](https://github.com/steve02081504) |
| 架構 | 以 C++ 製作的字串處理 DLL |
| 語法 | 類似 C 語言 |
| 訓練資料 | 無。**你編寫的辭典就是全部** |
| 參數數量 | 與 `_argv` 的數量相同 |
| 上下文長度 | 只要記憶體足夠，就能持續增加 |
| 幻覺 | 不會說出辭典中沒有寫的內容 |
| 授權條款 | BSD 3-Clause |
| 費用 | 免費（輸入與輸出皆免費） |

</div>

## 致謝

YAYA 6 整合了 [steve green 氏](https://github.com/steve02081504)的開發分支，並調整了與 500 系列的相容性，因而誕生。也感謝所有多年來持續使用 YAYA 編寫辭典的人格作者。

## 開始使用

### 若要開始製作人格：紺野ややめ ＋ 伺か Vibe Coding 工具箱

範本人格 **[紺野ややめ](https://github.com/YAYA-shiori/konnoyayame)** 已內建 600 系列的 YAYA。修改後即可直接成為你自己的人格。

此外，還隨附可與 AI 程式設計代理（Claude Code、Codex、GitHub Copilot 等）共同開發的 **Vibe Coding 工具箱**（開發套件）。從檢查辭典到確認在 SSP 上的運作情形，代理都能提供協助。只要請代理幫忙，就能迅速將 YAYA 6 的新功能加入辭典。

1. 從 [Releases](https://github.com/YAYA-shiori/konnoyayame/releases) 下載 `konnoyayame.nar`，並安裝到 SSP
2. 若要手動修改，請編輯 `ghost/master/dic/normal/` 中的辭典（辭典結構請見 [GHOST.md](https://github.com/YAYA-shiori/konnoyayame/blob/master/GHOST.md)）
3. 若要使用 AI 修改，請在人格資料夾中啟動代理，並要求它「進行設定」（準備事項請見 [DEVKIT-GUIDE.md](https://github.com/YAYA-shiori/konnoyayame/blob/master/DEVKIT-GUIDE.md)）

工具箱以 Windows 和 Claude Code 的組合製作，並已確認可正常運作。

### 若要將現有的人格升級至 YAYA 6

1. 從 [GitHub Releases](https://github.com/YAYA-shiori/yaya-shiori/releases) 下載最新版
2. 替換人格中的 `yaya.dll`（以防萬一，請先備份人格）
3. 大致閱讀[600 系列的變更點](changes-600.md)
4. 試著在辭典中寫下 `IHASH()`

即使不是以紺野ややめ為基礎製作的人格，也可以只安裝 Vibe Coding 工具箱（[在其他 YAYA 人格中安裝開發套件](https://github.com/YAYA-shiori/konnoyayame/blob/master/DEVKIT-GUIDE.md#別の-yaya-ゴーストに開発キットを入れる)）。

## 發現問題時

如果發現運作方式與 500 系列不同，或是沒有按照編寫內容運作，請透過[維護團隊 BTS](https://bts.shillest.net/)（回報表單）告知我們。熟悉 GitHub 的使用者也可以透過 [yaya-shiori 的 Issues](https://github.com/YAYA-shiori/yaya-shiori/issues) 或 Pull Request 提出問題。

## 相關

- [600 的變更](changes-600.md)
- [雜湊](../grammar/12-hash.md)
- [值的巢狀結構與多維指派](../grammar/13-nesting.md)
- [前置處理](../grammar/08-preprocessor.md)
- [關於 YAYA](yaya.md)

<div class="y6-byline" markdown>

---

YAYA 6 的相容性確保、除錯、文字與插圖：**[Claudia](https://ponadocs.shillest.net/claudia/)**

</div>
