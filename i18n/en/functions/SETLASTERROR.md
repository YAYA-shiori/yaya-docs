# SETLASTERROR
**Category:** デバッグ

## Signature
```
SETLASTERROR( code )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| code | Error code to set (integer value) |

## Returns
None

## Description
Sets the error code for system functions. You can manually set the error state while a YAYA script is running.

Use this with GETLASTERROR to manage the system-level error state.

## Compatibility
- YAYA: Supported since the initial version
- AYA: 5.8 and later

## See Also
- GETLASTERROR
