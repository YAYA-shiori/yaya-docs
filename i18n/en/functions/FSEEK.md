# FSEEK

**Category:** ファイル操作

## Signature

```
FSEEK(path, offset, origin)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | The file name specified with FOPEN |
| offset | The number of bytes to move |
| origin | A string specifying the starting point: `SEEK_CUR` or `current` (current position), `SEEK_END` or `end` (end of file), `SEEK_SET` or `start` (beginning of file) |

## Returns

- On success: 1
- On failure: 0

In non-binary mode, automatic line-ending conversion may prevent FSEEK/FTELL from working as expected. If you use these functions, it is recommended that you specify binary mode with FOPEN.

## Description

Moves the file position indicator used when reading from or writing to a file.

## See Also

- FTELL
- FOPEN
