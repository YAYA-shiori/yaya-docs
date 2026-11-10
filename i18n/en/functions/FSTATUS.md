# FSTATUS

**Category:** ファイル操作

## Signature

```
FSTATUS(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | The file name specified with FOPEN |

## Returns

Returns the result status of the most recent file I/O operation (such as FOPEN, FREAD, FWRITE, FSEEK, or FTELL).

| Return value | Meaning |
|--------|------|
| 0 | Completed normally (no error) |
| -1 | An error occurred |
| 1 | Reached the end of the file (EOF) |

## Description

Gets the status of the most recent operation by a file read/write function (FOPEN, the FREAD family, the FWRITE family, FSEEK, or FTELL).

## Compatibility

- YAYA: Tc573-3 or later

## See Also

- FOPEN
- FSEEK
- FTELL
