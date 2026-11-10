# shiori.OnMemoryError

## 概述

发生内存错误时调用的用户自定义函数。

## Signature

```
shiori.OnMemoryError()
```

## Parameters

无

## Returns

返回值会被系统忽略。

## Notes

- 实现是可选的。如果不定义，系统只会生成错误日志
- 可以使用 `GETCALLSTACK` 函数定位问题所在

## Compatibility

- YAYA：Tc567-2 及之后版本

## See Also

- [shiori.OnMemoryLimit](./shiori-OnMemoryLimit.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
