# REQUESTLIB
**Category:** 外部ライブラリ

## Signature
```
REQUESTLIB( path , string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | DLL 的位置。相对于 YAYA 所在位置的相对路径，或绝对路径。 |
| string | 要传递给 request 函数的字符串 |

## Returns
- 成功：request 函数生成的字符串
- 失败：VOID（不返回任何内容）

## Description
调用预先加载的外部库的 request 函数，并获取其结果。外部库的 DLL 必须具有与 YAYA 相同的接口（导出 load/unload/request 函数）。

从 Tc604-1 起，指定通过 [LOADLIB](LOADLIB.md) 加载的 SAORI-basic 可执行文件时，YAYA 会启动该可执行文件并返回 SAORI/1.0 响应（[详情](LOADLIB.md#saori-basic)）。

### 与线程的关系
等待响应缓慢的外部库时，如果从通过 [THREADSTART](THREADSTART.md) 启动的线程中调用，那么在等待期间，来自 SSP 的 `request` 和其他线程都不会停止运行。

- 外部库只能由一个线程同时调用，因此对同一个库的调用会按顺序执行。如果其他线程正在调用同一个库，就要等它结束后再调用。不同的库可以同时调用
- 即使其他线程对正在调用的库执行 [UNLOADLIB](UNLOADLIB.md)，该库也不会被释放（警告 W0013）
- 外部库会从 `THREADSTART` 线程中调用。COM 或窗口等要求由特定线程调用的 SAORI，从工作线程调用时可能无法正常工作
- 调用过程中无法中断。[THREADSTOP](THREADSTOP.md) 要等该调用返回后才会生效

## Compatibility
- YAYA：从初始版本起即可使用
- AYA：从 5.8 版起可使用
- Tc604-1：支持 SAORI-basic 可执行文件
- Tc608-1：等待期间允许其他线程运行（存在 `THREADSTART` 线程时）。对同一个库的调用改为按顺序执行

## See Also
- LOADLIB
- UNLOADLIB
- THREADSTART
