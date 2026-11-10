# DUMPXML
**Category:** 型取得/変換

## Signature
```
DUMPXML( element [, pretty] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| element | A hash representing the root element (in the same format returned by [FREADXML](FREADXML.md#要素の形)) |
| pretty | If 1, format the output with newlines and indentation. Defaults to 0 (output on one line) |

## Returns
- On success: an XML string with an XML declaration (`<?xml version="1.0" encoding="UTF-8"?>`)
- On failure: an empty string

## Description
Converts an element hash to an XML string and returns it. This is the reverse conversion of [PARSEXML](PARSEXML.md).

The keys in an element hash are as follows. All keys except `name` are optional (and may be empty).

| Key | Value |
|------|----|
| `name` | Tag name (required). String |
| `attr` | A hash mapping attribute names to attribute values. Values can be integers, real numbers, or strings (written as strings) |
| `children` | A generic array of child element hashes |
| `text` | The element's text. Integer, real number, or string |

- Text is written before child elements. If an element read by [FREADXML](FREADXML.md) contains interleaved text and child elements (such as `<p>a<b>x</b>c</p>`), the original order is not restored (`<p>ac<b>x</b></p>` is produced)
- Escapes `&` `<` `>`, and `"` in attribute values
- Tag names and attribute names are checked against XML name rules for ASCII characters only (the first character must be a letter, `_`, or `:`; subsequent characters may also be digits, `-`, or `.`). Non-ASCII characters such as Japanese characters can be used

When formatting, use four spaces for indentation and LF for newlines. Even inside elements that contain text, newlines and indentation are inserted before the second and subsequent child elements. [FREADXML](FREADXML.md) / [PARSEXML](PARSEXML.md) ignore text consisting only of whitespace between elements, so it does not affect `text` when the result is read back.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No argument | W0008 | 8 |
| element is not a hash, `name` is missing or invalid, `attr` is not a hash, an attribute name is invalid, an attribute value or `text` is an array or hash, `children` is not an array, or a child element is not a hash | W0027 (also outputs what is invalid) | 27 |

## Example
```
_item = IHASH("name", "item", "text", "りんご")
_item["attr"] = IHASH("id", 1)
_shop = IHASH("name", "shop")
_shop["children"] = IARRAY()
_shop["children"] ,= _item

DUMPXML(_shop)
// <?xml version="1.0" encoding="UTF-8"?><shop><item id="1">りんご</item></shop>

DUMPXML(_shop, 1)
// <?xml version="1.0" encoding="UTF-8"?>
// <shop>
//     <item id="1">りんご</item>
// </shop>

DUMPXML(PARSEXML('<a x="1"><b/></a>'))
// <?xml version="1.0" encoding="UTF-8"?><a x="1"><b/></a>
```

## Compatibility
- YAYA: Tc602-1 and later

## See Also
- [FWRITEXML](FWRITEXML.md)
- [PARSEXML](PARSEXML.md)
- [DUMPJSON](DUMPJSON.md)
