# shiori.OnMemoryLimit

## 概述

达到内存上限时调用的用户自定义函数。

## Signature

```
shiori.OnMemoryLimit()
```

## Parameters

无

## Returns

返回值会被系统忽略。

## Notes

- 实现是可选的。如果不需要错误处理，可以不在词典中编写此函数
- 可以使用 `GETCALLSTACK` 函数定位问题所在
- 执行期间内存耗尽时会调用此函数。但无法捕获堆栈溢出

## Compatibility

- YAYA：Tc567-2 及之后版本

## See Also

- [shiori.OnMemoryError](./shiori-OnMemoryError.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
