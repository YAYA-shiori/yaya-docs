# MKDIR
**Category:** ファイル操作

## Signature
```
MKDIR(path)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path of the directory to create |

## Returns
- Success: 1
- Failure: 0

## Description
Creates a directory. Full paths are supported. For relative paths, the base location is the DLL's directory.

**Limitations:** Only one directory level can be created at a time. Specifying multiple nonexistent nested levels at once causes an error.

## Compatibility
- YAYA: Available since the initial release
- AYA: Available since version 5.8

## See Also
- RMDIR
