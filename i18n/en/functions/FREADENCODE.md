# FREADENCODE

**Category:** ファイル操作

## Signature

```
FREADENCODE(path, size [, type])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | File name specified with FOPEN |
| size | Number of bytes to read. Specify 0 to read the entire file |
| type | Encoding type: one of "base64", "url", or "form". Defaults to "base64" (see STRENCODE for details) |

## Returns

- On success: encoded string
- If the end of the file is reached: -1
- On failure: empty string

Reads a file while encoding it as Base64 or URL encoding. Line-ending conversion is applied if the file was not opened in binary mode. You must open the file with FOPEN beforehand.

## Compatibility

- YAYA: Tc535-1 and later

## See Also

- FREAD
- FREADBIN
- FOPEN
- STRENCODE
