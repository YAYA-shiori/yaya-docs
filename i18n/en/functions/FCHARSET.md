# FCHARSET

**Category:** ファイル操作

## Signature

```
FCHARSET( code )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| code | The character encoding ID or character encoding name to set ([character encoding names](../grammar/11-character-encoding.md#文字コードの名前)). If the name is unknown, warning W0012 is issued and the setting is not changed |

## Returns

No return value (VOID).

## Description

Specifies the character encoding to use for reading and writing files. It must be called before FOPEN. The character encoding can be changed for each file, and is determined when FOPEN is called. The setting is maintained for the ghost's current session, but is reset when the session ends. If FCHARSET is not called, the default character encoding follows the charset.file or charset setting in the basic configuration file.

## Compatibility

- YAYA: Supported since the initial release
- AYA: 5.8 and later
- Tc574-8 / Tc603-1: Passing an unknown character encoding name now issues warning W0012 and leaves the setting unchanged (previously, no warning was issued and the OS default was used)

## See Also

- FOPEN
- FCLOSE
- FATTRIB
