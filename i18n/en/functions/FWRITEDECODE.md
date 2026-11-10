# FWRITEDECODE
**Category:** ファイル操作

## Signature
```
FWRITEDECODE( path, string [, type] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | File name specified with FOPEN |
| string | Encoded string to write |
| type | Decoding method: one of `"base64"`, `"url"`, or `"form"` (defaults to base64; see [STRDECODE](STRDECODE.md) for details). In Tc554-1, this parameter could not be omitted due to an implementation error |

## Returns
None

## Description
A function that writes data while decoding it from base64 or URL encoding. It performs the reverse operation of FREADENCODE.

The file must be opened with FOPEN beforehand. If FOPEN does not open the file for binary access, newline conversion is performed. The data can be written correctly even if the decoded result contains the byte value 0 (0x00).

## Compatibility
- YAYA: Tc554-1 and later
- In Tc554-1, `type` could not be omitted due to an implementation error

## See Also
- FWRITE
- FREADENCODE
- STRDECODE
