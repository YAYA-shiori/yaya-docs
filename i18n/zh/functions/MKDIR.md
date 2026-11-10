# MKDIR
**Category:** ファイル操作

## Signature
```
MKDIR(path)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要创建的目录的路径 |

## Returns
- 成功：1
- 失败：0

## Description
创建目录。支持指定完整路径。对于相对路径，基准位置是 DLL 所在的位置。

**限制事项：** 一次只能创建一层目录。若一次指定多个尚不存在的嵌套目录层级，则会出错。

## Compatibility
- YAYA：从初始版本起可用
- AYA：从版本 5.8 起可用

## See Also
- RMDIR
