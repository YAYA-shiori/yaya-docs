# FENUM

**Category:** ファイル操作

## Signature

```
FENUM( path [ , delim ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 要枚举的目录路径。可以指定完整路径。相对路径以 DLL 的加载位置为基准 |
| delim | 分隔字符串（省略时为逗号） |

## Returns

- 成功时：以分隔符连接文件名和目录名后组成的字符串。目录名前会添加反斜杠前缀
- 失败时：VOID（空）

## Description

枚举指定位置的文件名和目录名，并以分隔符连接成字符串后返回。路径可以指定为完整路径。对于相对路径，以 DLL load 所传入的位置（通常是 DLL 所在位置）为基准。目录名前会添加 `\`。

## Compatibility

- YAYA: 从首次发布起即可使用
- AYA: 5.8 及以上版本
