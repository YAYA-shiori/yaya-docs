# 错误处理函数

## 概要

错误处理函数是在脚本执行期间发生错误时自动调用的用户自定义函数。

这些函数可以选择是否实现。不在词典中定义也不会影响脚本正常运行，但它们有助于调试和分析用户环境中的错误。

## 共通特性

所有错误处理函数都有以下特性：

- **可以选择是否实现** — 不需要错误处理时，可以不在词典中编写
- **返回值会被忽略** — 系统会忽略返回值
- 使用 **`GETCALLSTACK`** 函数可以定位问题所在

## 错误处理函数一览

| 函数 | 说明 |
|------|------|
| [shiori.OnCallLimit](./shiori-OnCallLimit.md) | 调用深度达到上限时 |
| [shiori.OnLoopLimit](./shiori-OnLoopLimit.md) | 循环迭代次数达到上限时 |
| [shiori.OnMemoryError](./shiori-OnMemoryError.md) | 发生内存错误时 |
| [shiori.OnMemoryLimit](./shiori-OnMemoryLimit.md) | 达到内存上限时 |

## 相关内容

- [GETCALLSTACK](../functions/GETCALLSTACK.md)
