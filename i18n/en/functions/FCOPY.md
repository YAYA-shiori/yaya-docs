# FCOPY

**Category:** ファイル操作

## Signature

```
FCOPY( path, dir )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | Name of the source file. A full or relative path can be specified (relative to the DLL load location). |
| dir | Name of the destination directory |

## Returns

- `1`: Success
- `0`: Failure

## Description

Copies a file. A full path can be specified. Relative paths are based on the location passed to DLL load (in most cases, the location of the DLL).

## Compatibility

- YAYA: Supported since the initial release
- AYA: 5.8 and later

## See Also

- FMOVE
- FRENAME
- FDEL
