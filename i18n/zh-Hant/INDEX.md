# YAYA 手冊

本手冊整理了伺か（Ukagaka）的 SHIORI「YAYA」的使用方法與規格，也收集了 YAYA 及其前身 AYA 相關資訊和 Tips。

本手冊以讓沒有程式設計經驗的人也能看懂為目標。如果發現難以理解的地方或錯誤，歡迎透過[整備班BTS](https://bts.shillest.net/)（回報表單）告訴我們。熟悉 GitHub 的讀者也可以透過 [Issues](https://github.com/YAYA-shiori/yaya-docs/issues) 或 Pull Request 回報。

> 我們為 AI 代理準備了尋找資訊的指南 [llms.txt](https://yaya-shiori.github.io/yaya-docs/llms.txt)。各頁面的 Markdown 原稿可透過與儲存庫相同路徑的 `.md` 取得（例如：`https://yaya-shiori.github.io/yaya-docs/startup/cheatsheet.md`）。

## 下載

- [下載（GitHub Releases）](https://github.com/YAYA-shiori/yaya-shiori/releases)
- [更新記錄](https://github.com/YAYA-shiori/yaya-shiori/wiki/ChangeLog)

## YAYA v6（通稱 Tc600 系列）

- 這是整合 [steve green](https://github.com/steve02081504) 的開發分支、調整相容性後，以大幅強化版形式發行的版本。
- 在維持與 500 系列高度相容的同時，也進行了大幅改寫，包括提升變數的靈活性、加快標頭解析速度，以及加入 XML/JSON 等剖析器和 DB（SQLite）等功能。
- 想先大致了解 → [YAYA 6 登場](other/yaya6-launch.md)
- 想從 YAYA Tc5xx-x 移轉至 Tc6xx-x（從 v5 系列移轉至 v6 系列）→ [600 的變更項目](other/changes-600.md)（只要替換 `yaya.dll`，辭典和存檔檔案都能照常運作。需要留意的地方只有函式名稱衝突等幾點）

## 初次接觸的讀者

- YAYA 或 AYA 是什麼？ → [關於 YAYA](other/yaya.md)
- 想快速確認 YAYA 的寫法 → [速查表](startup/cheatsheet.md)
- 想開始製作人格？ → [人格製作方法](startup/creating-ghost.md)
- 之前用 AYA 製作人格，想改用 YAYA → [從 AYA 移轉](startup/migration-from-aya.md)
- 想從 Satori 移轉至 YAYA → [從 Satori 移轉](startup/migration-from-satolili.md)

## 查詢資訊

- 完全沒有程式設計經驗！ → [基礎](basic/)
- 想了解 YAYA 的語法 → [語法](grammar/)、[速查表](startup/cheatsheet.md)
- 有哪些內建（系統）函式？ → [依用途分類的函式清單](functions/)
- 想依函式名稱查找 → [系統函式清單](system/system-functions-index.md)
- 想查詢或處理錯誤 → [錯誤處理函式](system/error-handling-functions.md)

也可以使用頁面上方的搜尋框查找。

## 系統辭典與範本

- 關於系統辭典 → [yaya_shiori3.dic](system/yaya-shiori3-dic.md)、[yaya_optional.dic](system/yaya-optional-dic.md)
- 關於範本人格 → [人格製作方法](startup/creating-ghost.md)、[簡易 YAYA 範本](other/simple-yaya-template.md)
- 想輕鬆撰寫對話 → [talklib](other/talklib.md)
- SHIORI 以外的用途 → [將 YAYA 作為 SAORI 使用](other/yaya-as-saori.md)、[將 YAYA 作為 MAKOTO 使用](other/yaya-as-makoto.md)、[將 YAYA 作為外掛程式使用](other/yaya-as-plugin.md)

## 遇到問題時

- 想了解各種技巧 → [Tips](tips/)
- 製作時遇到問題 → [疑難排解](other/troubleshooting.md)
- 如果仍無法解決，或懷疑是 YAYA 的問題 → 到[整備班BTS](https://bts.shillest.net/)（回報表單）詢問。熟悉 GitHub 的讀者也可以透過 [yaya-shiori 的 Issues](https://github.com/YAYA-shiori/yaya-shiori/issues) 或 Pull Request 詢問
- 也可以在[開發資訊搜尋](http://ukadev.shillest.net/)中搜尋，或許能找到答案

## 相關工具

- [紺野ややめ (Konnoyayame)](https://github.com/YAYA-shiori/konnoyayame) — YAYA 範本人格
- [玉（tama）](https://github.com/YAYA-shiori/tama/releases) — 用於檢查辭典錯誤和除錯的工具
- [yaya-CI-check](https://github.com/YAYA-shiori/yaya-CI-check) — 使用 GitHub Actions 檢查辭典的 CI 工具
- [ukagaka-doc-mcp](https://github.com/finelagusaz/ukagaka-doc-mcp) - 在使用 AI 進行開發時，自動搜尋伺か相關規格的工具
