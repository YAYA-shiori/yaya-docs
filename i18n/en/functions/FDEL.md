# FDEL

**Category:** ファイル操作

## Signature

```
FDEL( path )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | Path of the file to delete. A full or relative path can be specified (relative to the DLL load location). |

## Returns

- `1`: Success
- `0`: Failure

## Description

Deletes a file. A full path can be specified. Relative paths are based on the location passed to DLL load (in most cases, the location of the DLL).

## Compatibility

- YAYA: Supported since the initial release
- AYA: 5.8 and later

## See Also

- FCOPY
- FMOVE
- FRENAME
