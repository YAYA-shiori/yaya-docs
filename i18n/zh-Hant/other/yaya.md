# 關於 YAYA

## YAYA、AYA 是什麼

- 讀作「やや」。這是用於處理字串的 DLL。
- 它是稱為 SHIORI（栞、しおり）的基本元件之一，負責掌管人格（在桌面上顯示角色的軟體，也就是在 [SSP](http://ssp.shillest.net/) 等 baseware 上運作的角色）的思維。
- SHIORI 還有[里々](https://ukatech.shillest.net/satori-docs/)、[華和梨](https://ukatech.shillest.net/kawari-docs/)、結奈等。
- 想從里々轉換過來的讀者，請參閱[從里々轉換](../startup/migration-from-satolili.md)。

## 概念

- 特色是使用類似 C 語言的寫法。有程式設計經驗的人，或許能輕鬆上手。
- 為了讓沒有程式設計經驗的讀者也能使用，本手冊也準備了[基礎](../basic/)內容。
- YAYA 是以通用語言為目標設計的，因此用途不限於 SHIORI。關於 SHIORI 以外的用途，請參閱以下頁面。
  - [作為 SAORI 的 YAYA](yaya-as-saori.md)
  - [作為 MAKOTO 的 YAYA](yaya-as-makoto.md)
  - [作為外掛程式的 YAYA](yaya-as-plugin.md)
- 也有人替換系統辭典，將 YAYA 用作 SAORI。
- 除了用於人格，也可以將它作為通用的字串處理嵌入式語言使用。關於作為通用語言 DLL 的 YAYA，請參閱[作為 WindowsDLL 的 YAYA](../grammar/10-yaya-as-windows-dll.md)。
- 發布的二進位檔是供 Windows 使用的 `yaya.dll`。原始碼也能在 Linux、FreeBSD、macOS 上建置，並已確認可以運作（但目前只發布 Windows 版本）。如果發現有無法運作的地方，請告訴我們。

## 「以通用語言為目標設計」是什麼意思

- 單獨使用 `yaya.dll` 時，完全不具備作為 SHIORI 使用的功能。它只是 DLL 格式符合 SHIORI 規範的通用語言 DLL。
- 因此，YAYA 會使用一系列稱為「系統辭典」的 YAYA 腳本檔案，讓自己能作為 SHIORI 運作。
- 本手冊的[文法](../grammar/)與[系統函式](../functions/)說明的是作為通用語言的 YAYA。作為 SHIORI 的運作方式，則在[系統辭典](../system/)頁面中說明。
- 因此，如果是為了了解「作為人格的 SHIORI 使用」而參考本手冊的文法，可能會感到不太習慣（「沒有 request 函式啊！」「On〜 事件會在什麼時候呼叫？」）。
- 想深入了解「作為人格 SHIORI 的 YAYA」時，也建議一併閱讀 [yaya_shiori3.dic](../system/yaya-shiori3-dic.md) 頁面。

## YAYA 與 AYA 的差異

- AYA 是 umeici 先生製作的 SHIORI。最後一個版本是 5.8，可從 [::: et cetera.](http://umeici.onjn.jp/) 取得。
- YAYA 以 umeici 先生的 AYA Ver.5 為原型，由 YAYA 開發團隊（整備班）接手後，持續進行改良與發展。
- YAYA 分為 500 系（Tc5xx-x）與 600 系（Tc6xx-x，也就是 YAYA 6）。600 系新增了雜湊、巢狀陣列、JSON・XML 等格式的讀寫，以及 SQLite 的支援。500 系的辭典只要替換 `yaya.dll`，幾乎就能原封不動地運作。詳細資訊請參閱 [YAYA 6 登場](yaya6-launch.md)與[600 的變更內容](changes-600.md)。

### 該使用哪一個？

如果不確定該使用 AYA 還是 YAYA，以下提供簡單的比較。

|  | 新功能・更新 | 穩定性 |
|---|---|---|
| AYA | △ AYA 已停止更新。 | ○ 雖然 AYA 5.8 已推出一段時間，但仍相當穩定。 |
| YAYA | ○ YAYA 開發團隊持續新增功能與更新。 | △ 由於更新頻繁，不同版本的運作方式可能有所差異。更新時請確認變更記錄。 |

簡單來說……

- 如果人格已經使用 AYA 運作，而且沒有特別不滿意功能上的限制，繼續使用 AYA 就沒問題。
- 如果準備開始製作人格，或想不斷嘗試新功能，請使用 YAYA。想從 AYA 轉換過來時，請參閱[從 AYA 轉換](../startup/migration-from-aya.md)。

本手冊主要刊載 YAYA 的相關資訊。

## 發布・相關工具

- [下載（GitHub Releases）](https://github.com/YAYA-shiori/yaya-shiori/releases)
- [變更記錄](https://github.com/YAYA-shiori/yaya-shiori/wiki/ChangeLog)
- [紺野ややめ (Konnoyayame)](https://github.com/YAYA-shiori/konnoyayame) — YAYA 的範本人格
- [玉（tama）](https://github.com/YAYA-shiori/tama/releases) — 用於檢查辭典錯誤與除錯的工具
- [yaya-CI-check](https://github.com/YAYA-shiori/yaya-CI-check) — 使用 GitHub Actions 檢查辭典的 CI 工具

## 本手冊的架構

| 想了解的內容 | 頁面 |
|---|---|
| 想快速確認 YAYA 的寫法 | [速查表](../startup/cheatsheet.md) |
| 想第一次製作人格 | [人格製作方式](../startup/creating-ghost.md)、[教學](../startup/tutorial-01-preparation.md) |
| 沒有程式設計經驗 | [基礎](../basic/) |
| 想了解文法 | [文法](../grammar/) |
| 想查詢內建函式 | [依用途分類的函式一覽](../functions/)、[系統函式一覽](../system/system-functions-index.md) |
| 想了解系統辭典 | [yaya_shiori3.dic](../system/yaya-shiori3-dic.md)、[yaya_optional.dic](../system/yaya-optional-dic.md) |
| 想了解各種技巧 | [Tips](../tips/) |
| 遇到問題時 | [疑難排解](troubleshooting.md) |
