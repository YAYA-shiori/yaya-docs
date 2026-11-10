# YAYA 作為 SAORI

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### 概要

這是由摂理氏製作、以 SAORI 形式呼叫 yaya.dll 的模組。<br>
如此一來，便能從 YAYA 以外的 SHIORI 使用 YAYA 的功能。

在預設狀態下，只能使用 YAYA 的內建（系統）函式。<br>
加入額外模組後，還能擴展更多用途。了解 YAYA 語法的人也可以自行製作這些額外模組。<br>

### 下載

- ~~[yaya_as_saori_2021_10_08.zip](../attachment/yaya_as_saori_2021_10_08.zip)~~
- [Releases · YAYA-shiori/yaya-as-saori · GitHub](https://github.com/YAYA-shiori/yaya-as-saori/releases)

### 額外模組

- [json 解析器與類似物件的功能](http://c-lege.hacca.jp/ukgk/ukst.html)
  - 能將 json 載入為類似 javascript 物件的格式，並可進行取出元素等操作的模組。
- [calendae](http://gallnuts.webcrow.jp/dump.shtml)
  - 提供曆法相關計算功能的模組。
- [sub-edittext](http://gallnuts.webcrow.jp/dump.shtml)
  - 提供文字檔案編輯功能的模組。
- [ssu.aym](http://rabbitbike.oh.land.to/nicky/log200803.html)
  - 使其執行方式與 ssu（隨 Satori 附帶的 SAORI）相同。
- [Reta](http://navy.nm.land.to/post/)
  - 讀取文字檔案、已安裝人格的外殼名稱，以及文／Satori／Kawari／美坂的存檔資料。

### 說明網站

- [SAORI/YAYA - Satori Wiki](http://soliton.sub.jp/satori/index.php?SAORI%2FYAYA)
  - 說明如何從 Satori 使用。
- [AYA as SAORI：Satori 簡易說明](http://navy.nm.land.to/post/a_a_s.html)
  - 這是 AYA as SAORI 的說明，但也能用於 YAYA as SAORI（不過不包含 YAYA 新增的函式）

### 示範人格

- [紺野さやめ](http://navy.nm.land.to/post/)
  - Satori 用的示範人格。由於隨附的 SAORI 版本較舊，建議替換。

### 自行製作模組

- 和一般辭典一樣，只要在[yaya.txt](../grammar/01-basic-settings.md)中追加內容，就能自由擴充。<br>依照慣例，常使用「.aym」副檔名（※aya module 的縮寫），但使用其他副檔名也不會影響運作。
- SAORI 的引數會儲存在模組內名為`REQ.ARGS[*]`的陣列中。<br>Argument0 對應`REQ.ARGS[0]`，之後的引數也依此類推。
- SAORI 的傳回值可在模組內指派給 RES.RESULT 及名為`RES.VALUE*`的變數，以此傳回。<br>單一傳回值 Result 會傳回至 RES.RESULT，多個傳回值 Value\* 則會各自傳回至`RES.VALUE*`。<br>請注意，`RES.VALUE*`**不是陣列**。指派時，系統函式[EVAL](../functions/EVAL.md)或許會很方便。
- 如果因引數不正確等原因，導致 SAORI 功能無法正常執行，請將數值 -1 作為函式的傳回值（而非 SAORI 傳回值）。<br>YAYA as SAORI 的系統部分收到 -1 作為傳回值時，會將其視為不正確的呼叫並通知錯誤。<br>此時，建議使用 YAYA 的系統函式[LOGGING](../functions/LOGGING.md)，將發生錯誤的 SAORI 函式名稱與錯誤說明寫入記錄。
- 函式名稱可以自由設定，但將函式命名為「模組名稱.函式名稱」至少有兩個好處。
  - 第一，對於這類命名方式的函式，YAYA as SAORI 提供了載入及卸載模組的機制。<br>呼叫包含句點的函式名稱（例如模組名稱.函式名稱）時，YAYA as SAORI 會記住模組名稱的部分。<br>接著，第一次呼叫具有相同模組名稱的函式時，系統會尋找是否有名為**模組名稱.Load**的函式；若有，便會執行。<br>此外，yaya.dll 卸載時，系統會尋找是否有名為**模組名稱.Unload**的函式；若有，便會執行。<br>若要在整個模組中使用共通的全域變數，可以利用這套機制進行初始化及收尾處理。
  - 第二，像這樣在函式名稱前加上模組名稱，可以降低函式名稱重複的機率。<br>不同作者製作的多個模組可能會同時使用，當然，同一位作者也可能分別製作多個模組。<br>預先考慮到這些情況並採用這種命名方式，就能在一定程度上降低函式名稱重複的風險。

## 附件

- [yaya_as_saori_2014_01_04.zip](../attachment/yaya_as_saori_2014_01_04.zip)
- [yaya_as_saori_2014_11_08.zip](../attachment/yaya_as_saori_2014_11_08.zip)
- [yaya_as_saori_2014_11_08b.zip](../attachment/yaya_as_saori_2014_11_08b.zip)
- [yaya_as_saori_2015_12_30.zip](../attachment/yaya_as_saori_2015_12_30.zip)
- [yaya_as_saori_2021_06_14-2.zip](../attachment/yaya_as_saori_2021_06_14-2.zip)
- [yaya_as_saori_2021_06_14.zip](../attachment/yaya_as_saori_2021_06_14.zip)
- [yaya_as_saori_2021_06_17.zip](../attachment/yaya_as_saori_2021_06_17.zip)
- [yaya_as_saori_2021_06_24-2.zip](../attachment/yaya_as_saori_2021_06_24-2.zip)
- [yaya_as_saori_2021_06_24.zip](../attachment/yaya_as_saori_2021_06_24.zip)
- [yaya_as_saori_2021_06_25.zip](../attachment/yaya_as_saori_2021_06_25.zip)
- [yaya_as_saori_2021_06_28.zip](../attachment/yaya_as_saori_2021_06_28.zip)
- [yaya_as_saori_2021_06_30.zip](../attachment/yaya_as_saori_2021_06_30.zip)
- [yaya_as_saori_2021_07_10.zip](../attachment/yaya_as_saori_2021_07_10.zip)
- [yaya_as_saori_2021_07_11-2.zip](../attachment/yaya_as_saori_2021_07_11-2.zip)
- [yaya_as_saori_2021_07_11.zip](../attachment/yaya_as_saori_2021_07_11.zip)
- [yaya_as_saori_2021_07_16.zip](../attachment/yaya_as_saori_2021_07_16.zip)
- [yaya_as_saori_2021_08_31.zip](../attachment/yaya_as_saori_2021_08_31.zip)
- [yaya_as_saori_2021_10_08.zip](../attachment/yaya_as_saori_2021_10_08.zip)
