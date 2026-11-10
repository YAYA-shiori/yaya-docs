# DICUNLOAD

**Category:** メタ操作・特殊関数

## Signature

```
DICUNLOAD( filename )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| filename | The name of the dictionary file to unload |

## Returns

- `0`: Success
- `1`: Failure

## Description

Unloads the functions and globaldefine groups contained in the specified dictionary file. If there is a problem with the dictionary file, an error occurs and nothing happens. A dictionary containing functions used by other dictionaries cannot be unloaded.

While a thread started with [THREADSTART](THREADSTART.md) is running, warning W0032 is issued and 1 is returned without doing anything.

## Compatibility

- YAYA: Tc561-1 and later
- Tc608-1: Unloading is no longer possible while a worker thread is running

## See Also

- DICLOAD
- UNDEFFUNC
- UNDEFGLOBALDEFINE
