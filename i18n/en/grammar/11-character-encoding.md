# Character Encoding

## Internal Character Encoding

YAYA uses **UCS-2** as its internal character encoding. When performing dictionary operations, file I/O, or interactions with external libraries, it automatically converts all strings to and from UCS-2.

## Character Encoding ID System

Some functions refer to character encodings by numeric ID. For functions that accept names, use the name in its text representation ([Character Encoding Names](#文字コードの名前)):

| Encoding | Text representation | ID |
|----------------|------------|-----|
| Shift JIS | Shift_JIS | 0 |
| UTF-8 | UTF-8 | 1 |
| EUC-JP | EUC-JP | 2 |
| Big5 | Big5 | 3 |
| GB2312 | GB2312 | 4 |
| EUC-KR | EUC-KR | 5 |
| ISO-2022-JP (JIS) | ISO-2022-JP | 6 |
| Binary | binary | 126 |
| OS default | default (OSNative is also the same) | 127 |

## Character Encoding Names

When specifying a character encoding by name, use the text representation in the table above. Names are case-insensitive.

If you pass an unsupported name (such as `UTF-16` or `ISO-8859-1`) to a system function, it emits warning W0012 and fails (GETLASTERROR is 12). See the function's page for details on how it fails. Before Tc574-8 / Tc603-1, unsupported names were treated as the OS default without a warning.

When you specify an unsupported name in a configuration file (such as `charset`), it continues to use the OS default without a warning, as before.

## Special Case: Binary Encoding

The binary format is “a special character encoding that uses the low-order bytes of a UCS-2 string as-is to form a byte sequence.” It is designed for functions such as `FWRITEBIN` and `FREADBIN`, which exchange data without conversion.

**Important limitation:** Even in binary mode, YAYA cannot process null bytes (0x00) in strings. Existing system dictionaries such as `FUNCTIONEX` also do not expect binary string values.

## See Also

- [CHARSETLIB](../functions/CHARSETLIB.md)
- [CHARSETLIBEX](../functions/CHARSETLIBEX.md)
- [CHARSETIDTOTEXT](../functions/CHARSETIDTOTEXT.md)
- [CHARSETTEXTTOID](../functions/CHARSETTEXTTOID.md)
- [FCHARSET](../functions/FCHARSET.md)
- [STRENCODE](../functions/STRENCODE.md)
- [STRDECODE](../functions/STRDECODE.md)
