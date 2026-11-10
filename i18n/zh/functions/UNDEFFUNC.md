# UNDEFFUNC
**Category:** メタ操作・特殊関数

## Signature
```
UNDEFFUNC( funcname )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| funcname | 要取消加载的函数名 |

## Returns
- 0：成功
- 1：失败

## Description
取消加载指定的函数。

如果卸载会导致词典文件出现问题，则会报错且不执行任何操作。此外，已被其他位置引用的函数无法卸载。

通过 [THREADSTART](THREADSTART.md) 启动的线程运行期间，会发出警告 W0032，不执行任何操作并返回 1。

## Compatibility
- YAYA：Tc561-1 及以后
- Tc608-1：更改为工作线程运行期间无法取消加载

## See Also
- DICUNLOAD
- UNDEFGLOBALDEFINE
