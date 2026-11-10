# FSIZE

**Category:** ファイル操作

## Signature

```
FSIZE(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 要获取大小的文件路径。可以指定完整路径。相对路径以 DLL 的加载位置为基准 |

## Returns

- 成功时：表示文件大小（字节数）的非负整数
- 失败时：-1

## Description

获取文件大小。可以使用完整路径指定路径。如果使用相对路径，则以 DLL load 传入的位置（通常是 DLL 所在位置）为基准。

## Compatibility

- YAYA：从首次发布起即可使用
- AYA：5.8 版及以后

## See Also

- FATTRIB
- FSEEK
- FTELL
