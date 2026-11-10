# FWRITEBIN
**Category:** ファイル操作

## Signature
```
FWRITEBIN( path, string [, char] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | File name specified with FOPEN |
| string | String to write |
| char | Replacement character for the byte value 0x00 (defaults to a half-width space) |

## Returns
None

## Description
A function that writes data without performing character encoding conversion. The file must be opened with FOPEN beforehand.

Newline conversion occurs if the file was not opened in binary mode.

The character specified by `char` is converted to the byte value 0 because YAYA cannot store null bytes in strings.

## Compatibility
- YAYA: Tc516-901 and later

## See Also
- FWRITE
- FREADBIN
- FOPEN
