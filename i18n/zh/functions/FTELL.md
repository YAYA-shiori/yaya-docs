# FTELL

**Category:** ファイル操作

## Signature

```
FTELL(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 通过 FOPEN 指定的文件名 |

## Returns

- 成功时：从文件开头算起的字节偏移量（当前文件位置）
- 失败时：-1

在非二进制模式下，由于换行符会自动转换，FSEEK/FTELL 可能无法按预期工作。使用这些函数时，建议在 FOPEN 中指定二进制模式。

## Description

获取文件读写位置（文件位置指示器）。

## See Also

- FSEEK
- FOPEN
