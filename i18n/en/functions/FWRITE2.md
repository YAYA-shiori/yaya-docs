# FWRITE2
**Category:** ファイル操作

## Signature
```
FWRITE2( path, string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path to a file opened with FOPEN (relative to yaya.dll) |
| string | String to write |

## Returns
None (VOID)

## Description
A function that writes one line to a file. The file must be opened with FOPEN beforehand.

The character encoding is converted from YAYA's internal format to the format specified with FCHARSET before writing. Unlike FWRITE, **no newline character is appended at the end of the line**.

To automatically append a newline character, use FWRITE.

## Compatibility
- YAYA: Available since the initial versions
- AYA: Version 5.8 and later

## See Also
- FWRITE
- FREAD
- FWRITEBIN
- FOPEN
