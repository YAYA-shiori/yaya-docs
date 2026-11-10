# FREADXML
**Category:** ファイル操作

## Signature
```
FREADXML( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path of the XML file to read (a path relative to yaya.dll or an absolute path) |
| charset | Character encoding of the file (optional). Specify as a string (such as `"UTF-8"` or `"Shift_JIS"`. [Character encoding names](../grammar/11-character-encoding.md#文字コードの名前)) or a number. If omitted, it is determined automatically as described below |

## Returns
- On success: A hash representing the root element (see [Element structure](#要素の形) below)
- On failure: Empty (VOID)

## Description
Reads and parses the entire XML file, then returns the root element as a hash. It does not need to be opened with [FOPEN](FOPEN.md).

XML parsing uses [TinyXML-2](https://github.com/ponapalt/tinyxml2).

When charset is omitted, the character encoding is determined in the following order:

1. UTF-8 if the file starts with a UTF-8 BOM
2. The encoding specified by the XML declaration (for example, `<?xml version="1.0" encoding="Shift_JIS"?>`). `Windows-31J` and `CP932` are also treated as Shift_JIS
3. UTF-8 if neither is present, or if the encoding is not recognized by YAYA

If charset is specified, the encoding in the XML declaration is ignored.

### Element structure

An element becomes a hash with the following four keys. All keys are present, even if their contents are empty.

| Key | Value |
|------|----|
| `name` | Tag name (kept as `ns:tag` if it has a namespace prefix) |
| `attr` | A hash mapping attribute names to attribute values. All values are strings |
| `children` | A generic array of child element hashes (in order of appearance) |
| `text` | A string formed by concatenating the direct text (including CDATA) in order |

- Entity references (such as `&amp;` and `&#x3042;`) are expanded
- Whitespace and line breaks before and after text are preserved. Whitespace-only content between elements is not included in `text`
- If child elements and text are mixed, their relative order is lost (`text` for `<p>a<b>x</b>c</p>` is `ac`)
- Comments, processing instructions, DOCTYPE, and the XML declaration are ignored. Content outside the root element is also not returned
- The order of attributes is not preserved. They are ordered as hash keys are

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| path is not a string | W0009 | 9 |
| charset is invalid | W0012 / W0009 | 12 / 9 |
| Cannot open the file | W0025 | 25 |
| Cannot parse as XML | W0026 (also outputs the error and line number) | 26 |

## Example
shop.xml:
```xml
<?xml version="1.0" encoding="Shift_JIS"?>
<shop name="A">
  <item id="1">りんご</item>
  <item id="2">バナナ</item>
</shop>
```

```
_x = FREADXML("shop.xml")
_x["name"]                          // shop
_x["attr"]["name"]                  // A
_x["children"][1]["name"]           // item
_x["children"][1]["attr"]["id"]     // 2
_x["children"][1]["text"]           // バナナ

foreach _x["children"]; _item {
    // _item["attr"]["id"] と _item["text"] を順に扱える
}
```

## Compatibility
- YAYA: Since Tc601-1
- Tc603-1: Passing an unknown character encoding name now causes a failure with warning W0012 (previously, no warning was issued and the OS default was used)

## See Also
- [PARSEXML](PARSEXML.md)
- [FWRITEXML](FWRITEXML.md)
- [FREADHTML](FREADHTML.md)
- [FREADJSON](FREADJSON.md)
- [Nested values and multidimensional assignment](../grammar/13-nesting.md)
