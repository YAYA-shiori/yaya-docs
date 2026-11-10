# FMOVE

**Category:** ファイル操作

## Signature

```
FMOVE( path , dir )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | Name of the source file. A full path can be specified. Relative paths are based on the DLL load location |
| dir | Name of the destination directory |

## Returns

- On success: 1
- On failure: 0

## Description

Moves a file. A full path can be specified. Relative paths are based on the location passed to DLL load (in most cases, the location of the DLL).

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later

## See Also

- FCOPY
- FRENAME
- FDEL
