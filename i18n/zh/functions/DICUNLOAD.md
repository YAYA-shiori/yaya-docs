# DICUNLOAD

**Category:** メタ操作・特殊関数

## Signature

```
DICUNLOAD( filename )
```

## Parameters

| 参数 | 说明 |
|-----------|-------------|
| filename | 要卸载的词典文件名 |

## Returns

- `0`：成功
- `1`：失败

## Description

卸载指定词典文件中包含的函数以及 globaldefine 组。如果词典文件存在问题，则会发生错误且不执行任何操作。包含被其他词典使用的函数的词典无法卸载。

通过 [THREADSTART](THREADSTART.md) 启动的线程运行期间，会发出警告 W0032，不执行任何操作并返回 1。

## Compatibility

- YAYA: Tc561-1 及以上版本
- Tc608-1：改为在工作线程运行期间无法卸载

## See Also

- DICLOAD
- UNDEFFUNC
- UNDEFGLOBALDEFINE
