# shiori.OnMemoryLimit

## 概要

記憶體達到上限時呼叫的使用者自訂函式。

## Signature

```
shiori.OnMemoryLimit()
```

## Parameters

無

## Returns

傳回值會被系統忽略。

## Notes

- 可選擇是否實作。不需要錯誤處理時，可以不在辭典中撰寫
- 可以使用 `GETCALLSTACK` 函式找出問題所在
- 執行期間記憶體耗盡時會呼叫。不過，無法捕捉堆疊溢位

## Compatibility

- YAYA：Tc567-2 以後

## See Also

- [shiori.OnMemoryError](./shiori-OnMemoryError.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
