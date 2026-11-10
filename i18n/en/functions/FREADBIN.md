# FREADBIN

**Category:** ファイル操作

## Signature

```
FREADBIN( path , size [ , char ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | Name of the file opened with FOPEN |
| size | Number of bytes to read. Specify 0 to read the entire file |
| char | Character used to replace null bytes (0x00) (defaults to a space) |

## Returns

- On success: String containing the data read
- On reaching the end of the file: -1
- On failure: Empty string

Reads binary data as-is without converting the character encoding. To avoid line-ending conversion, it is recommended to specify binary mode in advance with FOPEN. Null bytes (0x00) are replaced with the specified character (due to YAYA's limitation that strings cannot contain a byte with the value 0). If the file is not opened for binary access with FOPEN, newline conversion is performed.

## Compatibility

- YAYA: Tc516-901 and later
- Note: Until Tc540-3, a bug caused bytes 0x80 and above to be incorrectly converted to the 0xFF80 range due to a cast error

## See Also

- FREAD
- FWRITEBIN
