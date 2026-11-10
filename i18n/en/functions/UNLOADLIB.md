# UNLOADLIB
**Category:** 外部ライブラリ

## Signature
```
UNLOADLIB( path )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | DLL path. A relative path from the YAYA directory or an absolute path |

## Returns
VOID (no return value)

## Description
Unloads an external library (DLL). The first call performs the unload operation, followed by a call to FreeLibrary.

The external library DLL must have the same interface as YAYA itself (exports the load/unload/request functions).

If another thread ([THREADSTART](THREADSTART.md)) is calling the library with [REQUESTLIB](REQUESTLIB.md), the library is not unloaded and warning W0013 is issued. Call UNLOADLIB again after the call has finished.

## Compatibility
- YAYA: Since the initial version
- AYA: 5.8 and later
- Tc608-1: Changed so that libraries are not unloaded while another thread is calling them

## See Also
- LOADLIB
- REQUESTLIB
