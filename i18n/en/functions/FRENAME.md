# FRENAME

**Category:** ファイル操作

## Signature

```
FRENAME( from , to )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| from | Original file name. A full path can be specified. Relative paths are resolved from the DLL load location |
| to | New file name |

## Returns

- On success: 1
- On failure: 0

## Description

Renames a file. A full path can be specified. Relative paths are resolved from the location passed to DLL load (usually the location of the DLL).

A file that is still open with `FOPEN` cannot be renamed, and 0 is returned. Close it with `FCLOSE` before renaming it.

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later

## See Also

- FCOPY
- FMOVE
- FDEL
