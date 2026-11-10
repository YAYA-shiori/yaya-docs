# PARSEXML
**Category:** 型取得/変換

## Signature
```
PARSEXML( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | XML string |

## Returns
- On success: a hash representing the root element
- On failure: empty (VOID)

## Description
Parses an XML string and returns the root element as a hash. The element structure is the same as for [FREADXML](FREADXML.md#要素の形).

Because the string is already a YAYA string, the encoding in the XML declaration is ignored. Use [FREADXML](FREADXML.md) to read from a file.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| str is not a string | W0009 | 9 |
| Cannot parse as XML | W0026 (also outputs the error details and line number) | 26 |

## Example
```
_x = PARSEXML('<res code="0"><msg>OK</msg></res>')
_x["attr"]["code"]              // 0（文字列）
_x["children"][0]["text"]       // OK

PARSEXML('<a><b></a>')          // 空（警告 W0026）
```

## Compatibility
- YAYA: Tc601-1 and later

## See Also
- [FREADXML](FREADXML.md)
- [DUMPXML](DUMPXML.md)
- [PARSEHTML](PARSEHTML.md)
- [PARSEJSON](PARSEJSON.md)
