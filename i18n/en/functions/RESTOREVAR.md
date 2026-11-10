# RESTOREVAR
**Category:** メタ操作・特殊関数

## Signature
```
RESTOREVAR( [ path ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | (Optional) Name of the file to restore from. If omitted, the default filename (DLL name + "_variable.cfg", e.g. yaya_variable.cfg) is used |

## Returns
VOID (no return value)

## Description
Loads (restores) variables from a file. The operation is the same as the one performed during loading. You can restore variables from the specified file.

For the file format, see [SAVEVAR](SAVEVAR.md#保存形式). From Tc600-3 onward, hashes and nested values can also be restored. Files saved in versions earlier than Tc600-3 can still be read as they are.

## Compatibility
- YAYA: Available since the initial release
- Tc600-3: Added support for restoring hashes and nested values

## See Also
- SAVEVAR
- SERIALIZEVAR
- DESERIALIZEVAR
