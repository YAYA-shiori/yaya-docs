# shiori.OnCallLimit

## 概述

调用深度达到上限时调用的用户自定义函数。

## Signature

```
shiori.OnCallLimit(_filename_, _linenum_)
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
- 调用深度上限可在基础设置的 [`fncdepth`](../grammar/01-basic-settings.md#fncdepth-depth) 中更改（默认值：32 层）
- 即使尚未达到深度上限，剩余堆栈较少时也会调用此函数（Tc607-4 及之后版本）。如果在执行此函数期间堆栈进一步不足，则不会再次调用此函数，而是只输出错误日志（E0097）并停止调用

## Compatibility

- YAYA：Tc564-2 及之后版本
- Tc607-4：调整为剩余堆栈较少时也会调用（此前将 `fncdepth` 设为 0 会导致 baseware 崩溃）

## See Also

- [shiori.OnLoopLimit](./shiori-OnLoopLimit.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
