# FRENAME

**Category:** ファイル操作

## Signature

```
FRENAME( from , to )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| from | The original file name. Can be specified as a full path. Relative paths are based on the DLL load location |
| to | The new file name |

## Returns

- On success: 1
- On failure: 0

## Description

Renames a file. The path can be specified as a full path. Relative paths are based on the location passed to DLL load (usually the location of the DLL).

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 or later

## See Also

- FCOPY
- FMOVE
- FDEL
