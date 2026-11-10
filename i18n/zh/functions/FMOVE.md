# FMOVE

**Category:** ファイル操作

## Signature

```
FMOVE( path , dir )
```

## Parameters

| 参数 | 说明 |
|-----------|-------------|
| path | 源文件名。可以指定完整路径。相对路径以 DLL 的加载位置为基准 |
| dir | 目标目录名 |

## Returns

- 成功时：1
- 失败时：0

## Description

移动文件。可以指定完整路径。对于相对路径，以 DLL load 传入的位置（通常是 DLL 所在位置）为基准。

## Compatibility

- YAYA：从首次发布起即可使用
- AYA：5.8 及更高版本

## See Also

- FCOPY
- FRENAME
- FDEL
