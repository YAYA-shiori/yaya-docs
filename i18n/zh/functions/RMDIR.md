# RMDIR
**Category:** ファイル操作

## Signature
```
RMDIR( path )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要删除的目录路径（绝对路径或相对路径。相对路径以 DLL 的加载位置为基准） |

## Returns
- **1**: 删除成功
- **0**: 失败

## Description
删除目录。只能删除空目录。尝试删除包含文件的目录时会出错。

## Compatibility
- YAYA: 初始版本起支持
- AYA: 5.8 及以上版本

## See Also
- MKDIR
