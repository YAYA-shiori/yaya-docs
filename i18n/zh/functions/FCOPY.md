# FCOPY

**Category:** ファイル操作

## Signature

```
FCOPY( path, dir )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 源文件名。可以是完整路径或相对路径（以 DLL 加载位置为基准）。 |
| dir | 目标目录名 |

## Returns

- `1`: 成功
- `0`: 失败

## Description

复制文件。路径可以指定为完整路径。对于相对路径，以 DLL load 所传入的位置（通常是 DLL 所在位置）为基准。

## Compatibility

- YAYA: 从初版起支持
- AYA: 5.8 及以上版本

## See Also

- FMOVE
- FRENAME
- FDEL
