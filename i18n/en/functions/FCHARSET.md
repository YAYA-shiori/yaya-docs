# FCHARSET

**Category:** ファイル操作

## Signature

```
FCHARSET( code )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| code | Character encoding ID to set, or character encoding name ([character encoding names](../grammar/11-character-encoding.md#文字コードの名前)). If the name is unknown, warning W0012 is issued and the setting is not changed |

## Returns

No return value (VOID).

## Description

Specifies the character encoding used for reading and writing files. You must call this before FOPEN. You can change the character encoding for each file; the encoding is determined when FOPEN is called. The setting is maintained for the current ghost session, but is reset after the session ends. If FCHARSET is not called, the default character encoding follows the charset.file or charset setting in the basic settings file.

When reading UTF-8 files, a BOM (Byte Order Mark) at the beginning of the file is automatically removed if present. When writing in UTF-8, no BOM is written.

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later
- Tc574-8 / Tc603-1: Passing an unknown character encoding name now issues warning W0012 and leaves the setting unchanged (previously, no warning was issued and the OS default was used)

## See Also

- FOPEN
- FCLOSE
- FATTRIB
