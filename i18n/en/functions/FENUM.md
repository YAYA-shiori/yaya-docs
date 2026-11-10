# FENUM

**Category:** ファイル操作

## Signature

```
FENUM( path [ , delim ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | Path of the directory to enumerate. A full path can be specified. Relative paths are based on the DLL load location |
| delim | Delimiter string (defaults to a comma) |

## Returns

- On success: A string of file and directory names joined by the delimiter. Directory names have a backslash prefix
- On failure: VOID (empty)

## Description

Enumerates the file and directory names at the specified location and returns them as a string joined by the delimiter. A full path can be specified. Relative paths are based on the location passed to DLL load (in most cases, the location of the DLL). Directory names are prefixed with `\`.

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later
