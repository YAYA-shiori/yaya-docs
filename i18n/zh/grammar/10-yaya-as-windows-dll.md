# 作为 Windows DLL 的 YAYA

## 概要

YAYA（读音：Yaya）是用于处理字符串的 DLL。它使用类似 C 语言的语法，可以

- 处理给定的字符串
- 根据编写的规则生成字符串

执行此类处理。YAYA 是 Windows DLL，因此要直接使用它，需要具备一定的编程知识。

## 运行环境

适用于 Windows。它是在与 SSP 相同的开发环境中构建的，也就是说，使用了据称可在 Windows 95 上运行的设置。

## 导出函数

YAYA 提供以下公开函数。使用 YAYA 的程序在对 YAYA 执行 `LoadLibrary` 后，调用这些函数即可执行所需的处理。

### load

```c
extern "C" __declspec(dllexport) BOOL __cdecl load(HGLOBAL h, long len)
```

指示 YAYA 进行初始化。开始使用 YAYA 之前，也就是对 YAYA 执行 `LoadLibrary` 后，必须且仅调用此函数一次。向 `h` 传入“YAYA 识别为当前目录的绝对路径”，向 `len` 传入 `h` 的长度。`h` 所占用的内存由 YAYA 负责释放，因此调用方可以不再使用它。

### unload

```c
extern "C" __declspec(dllexport) BOOL __cdecl unload()
```

指示 YAYA 结束运行。在对 YAYA 执行 `FreeLibrary` 之前调用一次。

### request

```c
extern "C" __declspec(dllexport) HGLOBAL __cdecl request(HGLOBAL h, long *len)
```

指示 YAYA 执行处理并获取结果。向 `h` 传入待处理的字符串，向 `*len` 传入 `h` 的长度。传入的 `h` 所占用的内存由 YAYA 负责释放，因此调用方可以不再使用它。

处理结果通过返回值获取。处理结果的长度会存入 `*len`（也就是说，此值会被改写）。获取返回值后，请按照 `*len` 指定的大小释放内存区域（`GlobalFree`）。

## 技术说明

这是与桌面吉祥物软件“伺か”中使用的伪 AI 用 DLL“SHIORI”的接口规范完全相同的接口。

## 使用规定

- 请遵守随附文档中的规定
- 使用系统函数 [LICENSE](../functions/LICENSE.md)，可以显示 YAYA 使用的库的许可证条款
