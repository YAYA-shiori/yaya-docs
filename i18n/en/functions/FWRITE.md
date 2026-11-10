# FWRITE
**Category:** ファイル操作

## Signature
```
FWRITE( path, string )
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

The character encoding is converted from YAYA's internal format to the format specified with FCHARSET before writing. A newline character is automatically appended at the end of the line.

To write without appending a newline character, use FWRITE2.

## Compatibility
- YAYA: Available since the initial versions
- AYA: Version 5.8 and later

## See Also
- FWRITE2
- FREAD
- FOPEN
- FCHARSET
