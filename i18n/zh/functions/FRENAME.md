# FRENAME

**Category:** ファイル操作

## Signature

```
FRENAME( from , to )
```

## Parameters

| 参数 | 说明 |
|-----------|-------------|
| from | 更改前的文件名。可以指定完整路径。相对路径以 DLL 的加载位置为基准 |
| to | 更改后的文件名 |

## Returns

- 成功时：1
- 失败时：0

## Description

更改文件名。路径可以使用完整路径指定。对于相对路径，以 DLL load 传入的位置（通常是 DLL 所在的位置）为基准。

无法更改仍由 `FOPEN` 打开的文件名，此时返回 0。重命名前请先使用 `FCLOSE` 将文件关闭。

## Compatibility

- YAYA：从首次发布起可用
- AYA：5.8 及以上版本

## See Also

- FCOPY
- FMOVE
- FDEL
