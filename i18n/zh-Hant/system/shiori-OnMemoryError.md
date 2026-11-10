# shiori.OnMemoryError

## 概要

發生記憶體錯誤時呼叫的使用者自訂函式。

## Signature

```
shiori.OnMemoryError()
```

## Parameters

無

## Returns

傳回值會被系統忽略。

## Notes

- 可選擇是否實作。若未定義，系統只會產生錯誤記錄
- 可以使用 `GETCALLSTACK` 函式找出問題所在

## Compatibility

- YAYA：Tc567-2 以後

## See Also

- [shiori.OnMemoryLimit](./shiori-OnMemoryLimit.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
