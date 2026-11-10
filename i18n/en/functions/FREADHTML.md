# FREADHTML
**Category:** ファイル操作

## Signature
```
FREADHTML( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | Path to the HTML file to read (relative to yaya.dll, or an absolute path) |
| charset | Character encoding of the file (optional). Specify a string (such as `"UTF-8"` or `"Shift_JIS"`. [Character encoding names](../grammar/11-character-encoding.md#文字コードの名前)) or a number. If omitted, it is determined automatically as described below |

## Returns
- On success: A hash representing the `<html>` element (see [Element structure](#要素の形) below)
- On failure: Empty (VOID)

## Description
Reads and parses the entire HTML file, then returns the `<html>` element as a hash. You do not need to open it with [FOPEN](FOPEN.md).

HTML parsing uses [Gumbo](https://github.com/ponapalt/gumbo-parser-mirror), a parser that follows the HTML5 parsing rules. Even if closing tags are missing or elements are incorrectly nested, it repairs the markup and builds a tree using the same rules as a browser, so parsing itself does not fail. `<html>`, `<head>`, and `<body>` are also added if missing.

When charset is omitted, the character encoding is determined in the following order.

1. UTF-8 if a UTF-8 BOM is present at the beginning
2. The character encoding specified by `<meta charset="Shift_JIS">` or `<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">` within the first 1024 bytes. Content inside comments is ignored. `Windows-31J` and `CP932` are also treated as Shift_JIS
3. UTF-8 if neither is present, or if the character encoding is unknown to YAYA (including `UTF-16`)

If charset is specified, `<meta>` elements are ignored.

### Element structure

As with [FREADXML](FREADXML.md#要素の形), an element is represented as a hash with the following four keys. The keys are always present, even if their contents are empty.

| Key | Value |
|------|----|
| `name` | Tag name (HTML elements are lowercase, such as `div` and `custom-tag`) |
| `attr` | A hash mapping attribute names to attribute values. All values are strings. Attribute names are lowercase |
| `children` | Generic array of child element hashes (in order of appearance) |
| `text` | String formed by concatenating the direct text in order |

- Character references (such as `&amp;`, `&#x3042;`, and `&nbsp;`) are expanded
- Elements with no content, such as `<br>` and `<img>`, are also represented as elements with empty `children` and `text`
- If child elements and text are mixed, their relative order is lost (`text` for `<p>a<b>x</b>c</p>` is `ac`)
- For elements with child elements, whitespace-only text (line breaks or indentation between elements) is not included in `text`. For elements without child elements, whitespace-only text is retained (`text` for `<pre> </pre>` is a half-width space)
- Content inside `<script>`, `<style>`, and `<textarea>` is also included in `text`
- Comments, DOCTYPE, and processing instructions are ignored
- Attributes such as `xlink:href` and `xml:lang` inside SVG and MathML elements have prefixed names
- HTML with nesting deeper than 128 levels fails (the `<html>` element counts as level 1)
- The order of attributes is not preserved. They are ordered by hash key

### Errors
| Situation | Warning | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| No arguments | W0008 | 8 |
| path is not a string | W0009 | 9 |
| Invalid charset | W0012 / W0009 | 12 / 9 |
| Cannot open the file | W0025 | 25 |
| Nesting is too deep | W0026 (also outputs the cause) | 26 |

## Example
page.html:
```html
<!DOCTYPE html>
<html>
<head><meta charset="Shift_JIS"><title>お知らせ</title></head>
<body>
<h1>お知らせ</h1>
<ul>
  <li><a href="a.html">その1</a></li>
  <li><a href="b.html">その2</a></li>
</ul>
</body>
</html>
```

```
_h = FREADHTML("page.html")
_h["children"][0]["children"][1]["text"]     // お知らせ（<title>。[0] は <meta>）
_body = _h["children"][1]
_body["children"][0]["text"]                 // お知らせ（<h1>）
_ul = _body["children"][1]
foreach _ul["children"]; _li {
    _a = _li["children"][0]
    // _a["attr"]["href"] と _a["text"] を順に扱える
}
```

## Compatibility
- YAYA: Tc605-1 and later

## See Also
- [PARSEHTML](PARSEHTML.md)
- [FREADXML](FREADXML.md)
- [FREADJSON](FREADJSON.md)
- [Nested values and multidimensional assignment](../grammar/13-nesting.md)
