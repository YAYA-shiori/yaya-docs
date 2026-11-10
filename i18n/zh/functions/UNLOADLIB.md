# UNLOADLIB
**Category:** 外部ライブラリ

## Signature
```
UNLOADLIB( path )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | DLL 的路径。相对于 YAYA 目录的相对路径或绝对路径 |

## Returns
VOID（无返回值）

## Description
卸载外部库（DLL）。首次调用时执行卸载操作，随后调用 FreeLibrary。

外部库 DLL 必须拥有与 YAYA 本身相同的接口（导出 load/unload/request 函数）。

如果另一个线程（[THREADSTART](THREADSTART.md)）正在通过 [REQUESTLIB](REQUESTLIB.md) 调用该库，则不会卸载该库，而是发出警告 W0013。调用结束后，再次执行 UNLOADLIB 即可。

## Compatibility
- YAYA: 从初始版本起
- AYA: 5.8 及以上版本
- Tc608-1: 改为不卸载正在被其他线程调用的库

## See Also
- LOADLIB
- REQUESTLIB
