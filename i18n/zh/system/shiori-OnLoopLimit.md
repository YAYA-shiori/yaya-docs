# shiori.OnLoopLimit

## 概述

循环迭代次数达到上限时调用的用户自定义函数。

## Signature

```
shiori.OnLoopLimit(_filename_, _linenum_)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| *filename* | 发生错误的词典文件名 |
| *linenum* | 发生错误的行号 |

## Returns

返回值会被系统忽略。

## Notes

- 实现是可选的。如果不需要错误处理，可以不在词典中编写此函数
- 可以使用 `GETCALLSTACK` 函数定位问题所在
- 循环上限可在基础设置的 [`looplimit`](../grammar/01-basic-settings.md#looplimit-count) 中更改（默认值：1000000）。`foreach` 不受此限制
- 只有达到上限并被中止时才会调用。如果 `for` / `while` 恰好在上限次数时自然结束，则不会调用

## Compatibility

- YAYA：Tc564-2 及之后版本
- Tc574-10 / Tc606-4 将循环上限的默认值从 10000 提高到 1000000
- 在 Tc574-10 / Tc606-4 之前，即使 `for` / `while` 在达到上限前的某次迭代到上限次数之间自然结束（或执行 `break` / `return`），也可能会调用此函数

## See Also

- [shiori.OnCallLimit](./shiori-OnCallLimit.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
