# FSIZE

**Category:** ファイル操作

## Signature

```
FSIZE(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | Path to the file whose size is to be retrieved. Can be specified as a full path. Relative paths are based on the DLL load location |

## Returns

- On success: A non-negative integer representing the file size in bytes
- On failure: -1

## Description

Retrieves the file size. The path can be specified as a full path. Relative paths are based on the location passed to DLL load (usually the location of the DLL).

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 or later

## See Also

- FATTRIB
- FSEEK
- FTELL
