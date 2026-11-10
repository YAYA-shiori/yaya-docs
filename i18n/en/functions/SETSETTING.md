# SETSETTING
**Category:** メタ操作・特殊関数

## Signature
```
SETSETTING( name , string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | Name of the settings entry (string). Specify an entry from the basic settings file |
| string | Value to set (string) |

## Returns
- **1**: Success
- **0**: Failure

## Description
Changes the settings information for the running sentence. This function pairs with GETSETTING.

The following settings entries are effective only on the first load, so changing them at runtime has no effect:
- dic
- msglang
- charset.dic
- checkparser

## Compatibility
- YAYA: Supported since the initial version

## See Also
- GETSETTING
- [Basic Settings](../grammar/01-basic-settings.md)
