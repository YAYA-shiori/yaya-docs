# 錯誤處理函式

## 概要

錯誤處理函式是在指令碼執行期間發生錯誤時，自動呼叫的使用者自訂函式。

這些函式可選擇是否實作。即使沒有在辭典中定義，指令碼仍可正常運作，但實作這些函式有助於除錯及分析使用者環境中的錯誤。

## 共通特性

所有錯誤處理函式都具備以下特性：

- **可選擇是否實作** — 不需要錯誤處理時，可以不在辭典中撰寫
- **忽略傳回值** — 系統會忽略傳回值
- 使用 **`GETCALLSTACK`** 函式可以找出問題所在

## 錯誤處理函式一覽

| 函式 | 說明 |
|------|------|
| [shiori.OnCallLimit](./shiori-OnCallLimit.md) | 呼叫深度達到上限時 |
| [shiori.OnLoopLimit](./shiori-OnLoopLimit.md) | 迴圈反覆次數達到上限時 |
| [shiori.OnMemoryError](./shiori-OnMemoryError.md) | 發生記憶體錯誤時 |
| [shiori.OnMemoryLimit](./shiori-OnMemoryLimit.md) | 記憶體用量達到上限時 |

## 相關內容

- [GETCALLSTACK](../functions/GETCALLSTACK.md)
