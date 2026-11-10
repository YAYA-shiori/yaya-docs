# FWRITEXML
**Category:** ファイル操作

## Signature
```
FWRITEXML( path, element [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path of the file to write (relative to yaya.dll or an absolute path) |
| element | Hash representing the root element (in the same form returned by [FREADXML](FREADXML.md#要素の形)) |
| charset | Character encoding of the file (optional). Specify a string (such as `"UTF-8"` or `"Shift_JIS"`; [character encoding names](../grammar/11-character-encoding.md#文字コードの名前)) or a number. If omitted or an empty string, UTF-8 (without a BOM) is used |
| pretty | If 1, format the output with line breaks and indentation. Defaults to 1 (format the output) |

## Returns
- On success: 1
- On failure: 0

## Description
Converts the element hash to XML and writes it to a file. If the file already exists, it is overwritten. You do not need to open it with [FOPEN](FOPEN.md).

The hash format for elements, escaping, and formatting are the same as for [DUMPXML](DUMPXML.md). An XML declaration matching the charset is added at the beginning.

| charset | XML declaration encoding |
|---------|------|
| UTF-8 (default) | `UTF-8` |
| Shift_JIS | `Shift_JIS` |
| EUC-JP | `EUC-JP` |
| ISO-2022-JP | `ISO-2022-JP` |
| BIG5 | `Big5` |
| GB2312 | `GB2312` |
| EUC-KR | `EUC-KR` |
| default (OS character encoding) | Determined from the OS code page (932 gives `Shift_JIS`) |

Because the written file's XML declaration specifies the encoding, you can read it back with [FREADXML](FREADXML.md) without specifying a charset.

Characters that cannot be represented in the specified charset (such as emoji in Shift_JIS) are written as character references like `&#x1F600;` in text and attribute values. They are restored to the original characters when read back. Characters in element names and attribute names cannot be written as character references, so the operation fails with W0027.

Directories are not created. You cannot write to a directory that does not exist.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| Too few arguments | W0008 | 8 |
| path is not a string | W0009 | 9 |
| Invalid charset | W0012 / W0009 | 12 / 9 |
| Invalid element hash (see [DUMPXML](DUMPXML.md#エラー)) | W0027 | 27 |
| Element or attribute name contains characters that cannot be represented in the charset | W0027 | 27 |
| Could not open the file | W0025 | 25 |
| Write failed | W0013 | 13 |

## Example
```
_x = FREADXML("shop.xml")
_x["children"][0]["text"] = "みかん"

FWRITEXML("shop.xml", _x, "Shift_JIS")
// shop.xml:
// <?xml version="1.0" encoding="Shift_JIS"?>
// <shop name="A">
//     <item id="1">みかん</item>
//     <item id="2">バナナ</item>
// </shop>
```

## Compatibility
- YAYA: Tc602-1 and later
- Tc603-1: Characters that cannot be represented in the specified charset are now written using format-specific escapes instead of being silently replaced with `?`. Passing an unknown character encoding name now causes the operation to fail with warning W0012 (previously, it was treated as the OS default without a warning)

## See Also
- [DUMPXML](DUMPXML.md)
- [FREADXML](FREADXML.md)
- [FWRITEJSON](FWRITEJSON.md)
