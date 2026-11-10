# PARSEHTML
**Category:** 型取得/変換

## Signature
```
PARSEHTML( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | HTML string |

## Returns
- On success: a hash representing the `<html>` element
- On failure: empty (VOID)

## Description
Parses an HTML string and returns the `<html>` element as a hash. The element structure and parsing rules are the same as [FREADHTML](FREADHTML.md#要素の形).

Because the string is already a YAYA string, `<meta charset>` is ignored. Use [FREADHTML](FREADHTML.md) to read from a file.

Even if you pass only part of an HTML document (such as `<p>a</p>`), the result is a tree with `<html>`, `<head>`, and `<body>` added. Get the fragment from `children` of `<body>`.

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| str is not a string | W0009 | 9 |
| Nesting is too deep (more than 128 levels) | W0026 (also outputs the cause) | 26 |

## Example
```
_h = PARSEHTML('<p class=a>x<b>y</b>z<br><img src="a.png" alt="&amp;"></p>')
_h["name"]                                   // html
_body = _h["children"][1]
_p = _body["children"][0]
_p["attr"]["class"]                          // a
_p["text"]                                   // xz
_p["children"][0]["text"]                    // y
_p["children"][2]["attr"]["alt"]             // &
```

## Compatibility
- YAYA: Tc605-1 and later

## See Also
- [FREADHTML](FREADHTML.md)
- [PARSEXML](PARSEXML.md)
- [PARSEJSON](PARSEJSON.md)
