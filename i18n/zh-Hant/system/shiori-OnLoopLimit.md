# shiori.OnLoopLimit

## 概要

迴圈反覆次數達到上限時呼叫的使用者自訂函式。

## Signature

```
shiori.OnLoopLimit(_filename_, _linenum_)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| *filename* | 發生錯誤的辭典檔案名稱 |
| *linenum* | 發生錯誤的行號 |

## Returns

傳回值會被系統忽略。

## Notes

- 可選擇是否實作。不需要錯誤處理時，可以不在辭典中撰寫
- 可以使用 `GETCALLSTACK` 函式找出問題所在
- 迴圈上限可在基本設定的 [`looplimit`](../grammar/01-basic-settings.md#looplimit-count) 中變更（預設：1000000）。`foreach` 不適用
- 只有在達到上限而中止時才會呼叫。`for` / `while` 恰好在上限次數時自然結束的情況下，不會呼叫

## Compatibility

- YAYA：Tc564-2 以後
- 迴圈上限預設值在 Tc574-10 / Tc606-4 從 10000 改為 1000000
- 在 Tc574-10 / Tc606-4 之前，即使 `for` / `while` 在上限次數前一刻開始，並於上限次數內自然結束（或執行 `break` / `return`），也可能會呼叫

## See Also

- [shiori.OnCallLimit](./shiori-OnCallLimit.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
