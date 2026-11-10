# RMDIR
**Category:** ファイル操作

## Signature
```
RMDIR( path )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path of the directory to delete (full or relative path; relative paths are based on the DLL's load location) |

## Returns
- **1**: Deletion succeeded
- **0**: Failed

## Description
Deletes a directory. Only empty directories can be deleted. An error occurs if you try to delete a directory that contains files.

## Compatibility
- YAYA: Supported since the initial version
- AYA: 5.8 and later

## See Also
- MKDIR
