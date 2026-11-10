# 教學 1：準備

## 下載所需項目

- **[SSP](http://ssp.shillest.net/)（最新版本）**：目前主流的 baseware。功能豐富、執行輕巧，且持續更新；如果沒有特別偏好，建議使用這個。本教學也會以使用此 baseware 為前提進行說明。
- **yaya.dll（最新版本）**：YAYA 的 SHIORI 本體。請從 [yaya-shiori 的發行版本](https://github.com/YAYA-shiori/yaya-shiori/releases)下載。
- **[範本人格](creating-ghost.md)**：範本有數種，這裡將以 [SimpleYAYA 範本](../other/simple-yaya-template.md)說明。請將它安裝到上方準備好的最新版本 SSP 中。

大多數情況下，人格附帶的 yaya.dll 都是舊版。請將它替換為剛才下載的最新版本（位置為「（ssp.exe 所在資料夾）\ghost\（範本人格的資料夾名稱）\ghost\master」）。

## 準備適合開發的環境

### SSP 開發面板

首先啟動 SSP，在人格上按右鍵 → 設定 → 本體設定 → 一般 → 勾選「啟用開發者功能」（雖然會出現警告對話框，但直接確認即可）。

接著，按右鍵 → 功能 → 開啟開發面板。這裡備有許多方便製作人格的除錯功能。開發期間建議一直保持開啟。

![SSP 的開發面板](../attachment/img_tutorial_01_002.png)

### YAYA 除錯工具

下載[除錯器「玉」](http://umeici.onjn.jp/)，並解壓縮至方便使用的位置。參考：[使用玉檢查辭典錯誤](../tips/tama-error-check.md)

## 準備文字編輯器＋YAYA 專用語法上色設定（選擇性）

使用 Windows 標準的記事本也能製作人格，但設定 YAYA 專用的語法上色後，辭典會更容易閱讀。請從[編輯器語法上色檔案](../tips/editor-color-files.md)中選擇喜歡的設定。使用 JmEditor 時，畫面會像以下這樣。

![使用 JmEditor 的語法上色範例](../attachment/img_tutorial_01_001.png)

## 設定檔案關聯

請將「.dic」（辭典）、「.log」（執行記錄）和「.cfg」（存檔資料）這 3 種副檔名設定為可在按兩下後以文字編輯器開啟。檔案關聯的設定方式因作業系統而異，因此這裡不予說明。請自行使用搜尋網站等查詢。

如果已準備好設定 YAYA 專用語法上色的文字編輯器，請將「.dic」設定為以該文字編輯器開啟。

## 下一步

- [教學 2：試著撰寫對話](./tutorial-02-writing-dialogue.md)

## 相關

- [SimpleYAYA 範本](../other/simple-yaya-template.md)
- [遇到問題時的處理方式](../other/troubleshooting.md)
