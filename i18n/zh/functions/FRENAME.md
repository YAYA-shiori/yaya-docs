# FRENAME

**Category:** ファイル操作

## Signature

```
FRENAME( from , to )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| from | 更改前的文件名。可以指定完整路径。相对路径以 DLL 的加载位置为基准 |
| to | 更改后的文件名 |

## Returns

- 成功时：1
- 失败时：0

## Description

更改文件名。可以使用完整路径指定路径。如果使用相对路径，则以 DLL load 传入的位置（通常是 DLL 所在位置）为基准。

## Compatibility

- YAYA：从首次发布起即可使用
- AYA：5.8 版及以后

## See Also

- FCOPY
- FMOVE
- FDEL
