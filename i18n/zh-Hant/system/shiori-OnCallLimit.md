# shiori.OnCallLimit

## 概要

呼叫深度達到上限時呼叫的使用者自訂函式。

## Signature

```
shiori.OnCallLimit(_filename_, _linenum_)
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
- 呼叫深度上限可在基本設定的 [`fncdepth`](../grammar/01-basic-settings.md#fncdepth-depth) 中變更（預設：32 層）
- 即使尚未達到深度上限，堆疊剩餘空間不足時也會呼叫此函式（Tc607-4 以後）。若執行此函式時堆疊空間進一步不足，則不會再次呼叫此函式，而是只輸出錯誤記錄（E0097）並停止呼叫

## Compatibility

- YAYA：Tc564-2 以後
- Tc607-4：修改為堆疊剩餘空間不足時也會呼叫（在此之前，將 `fncdepth` 設為 0 會導致 baseware 一併崩潰）

## See Also

- [shiori.OnLoopLimit](./shiori-OnLoopLimit.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
