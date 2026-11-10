# SETGLOBALDEFINE
**Category:** メタ操作・特殊関数

## Signature
```
SETGLOBALDEFINE( define_name , define_value )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| define_name | Name to define with #globaldefine |
| define_value | Value to assign with #globaldefine |

## Returns
- **1**: Success
- **0**: Failure

## Description
Has the same effect as writing `#globaldefine` in a dictionary named `_RUNTIME_DIC_` in memory.

## Compatibility
- YAYA: Tc562-1 and later

## See Also
- ISGLOBALDEFINE
- UNDEFGLOBALDEFINE
- PROCESSGLOBALDEFINE
