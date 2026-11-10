# FTELL

**Category:** ファイル操作

## Signature

```
FTELL(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | The file name specified with FOPEN |

## Returns

- On success: The byte offset from the beginning of the file (the current file position)
- On failure: -1

In non-binary mode, automatic line-ending conversion may prevent FSEEK/FTELL from working as expected. If you use these functions, it is recommended that you specify binary mode with FOPEN.

## Description

Gets the file position indicator used when reading from or writing to a file.

## See Also

- FSEEK
- FOPEN
