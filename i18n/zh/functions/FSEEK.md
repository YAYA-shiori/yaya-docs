# FSEEK

**Category:** ファイル操作

## Signature

```
FSEEK(path, offset, origin)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 通过 FOPEN 指定的文件名 |
| offset | 移动的字节数 |
| origin | 表示移动起点的字符串。`SEEK_CUR` 或 `current`（当前位置）、`SEEK_END` 或 `end`（文件末尾）、`SEEK_SET` 或 `start`（文件开头） |

## Returns

- 成功时：1
- 失败时：0

在非二进制模式下，由于换行符会自动转换，FSEEK/FTELL 可能无法按预期工作。使用这些函数时，建议在 FOPEN 中指定二进制模式。

## Description

移动文件读写位置（文件位置指示器）。

## See Also

- FTELL
- FOPEN
