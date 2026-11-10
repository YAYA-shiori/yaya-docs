# UNDEFFUNC
**Category:** メタ操作・特殊関数

## Signature
```
UNDEFFUNC( funcname )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| funcname | Name of the function to unload |

## Returns
- 0: Success
- 1: Failure

## Description
Unloads the specified function.

If unloading would cause a problem with a dictionary file, an error occurs and nothing happens. A function that is already referenced elsewhere cannot be unloaded.

While a thread started with [THREADSTART](THREADSTART.md) is running, warning W0032 is issued, no action is taken, and 1 is returned.

## Compatibility
- YAYA: Tc561-1 and later
- Tc608-1: Functions can no longer be unloaded while a worker thread is running

## See Also
- DICUNLOAD
- UNDEFGLOBALDEFINE
