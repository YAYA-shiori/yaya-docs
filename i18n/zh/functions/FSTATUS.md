# FSTATUS

**Category:** ファイル操作

## Signature

```
FSTATUS(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 通过 FOPEN 指定的文件名 |

## Returns

返回最近一次文件 I/O 操作（如 FOPEN、FREAD、FWRITE、FSEEK、FTELL）的结果状态。

| 返回值 | 含义 |
|--------|------|
| 0 | 正常结束（无错误） |
| -1 | 发生错误 |
| 1 | 已到达文件末尾（EOF） |

## Description

获取文件读写函数（FOPEN、FREAD 系列、FWRITE 系列、FSEEK、FTELL）最近一次操作的状态。

## Compatibility

- YAYA：Tc573-3 及以后

## See Also

- FOPEN
- FSEEK
- FTELL
