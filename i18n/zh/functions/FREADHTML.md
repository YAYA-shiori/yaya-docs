# FREADHTML
**Category:** ファイル操作

## Signature
```
FREADHTML( path [, charset] )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| path | 要读取的 HTML 文件路径（相对于 yaya.dll 的路径，或绝对路径） |
| charset | 文件的字符编码（可省略）。可以指定字符串（如 `"UTF-8"`、`"Shift_JIS"`。[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）或数值。省略时按下文自动确定 |

## Returns
- 成功时：表示 `<html>` 元素的哈希（见下方[元素的形态](#要素の形)）
- 失败时：空（VOID）

## Description
读取并解析整个 HTML 文件，将 `<html>` 元素转换为哈希后返回。无需先通过 [FOPEN](FOPEN.md) 打开文件。

解析 HTML 时使用 [Gumbo](https://github.com/ponapalt/gumbo-parser-mirror)（遵循 HTML5 语法分析规则的解析器）。即使缺少闭合标签或标签嵌套错误，也会按照与浏览器相同的规则补全并构建树，因此解析本身不会失败。如果没有 `<html>`、`<head>`、`<body>`，也会自动补全。

省略 charset 时，按以下顺序确定字符编码。

1. 如果文件开头有 UTF-8 BOM，则使用 UTF-8
2. 文件开头 1024 字节以内的 `<meta charset="Shift_JIS">`，或 `<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">` 中指定的字符编码。不会读取注释中的内容。`Windows-31J` 和 `CP932` 也会按 Shift_JIS 处理
3. 如果以上内容都没有，或字符编码是 YAYA 不认识的编码（包括 `UTF-16`），则使用 UTF-8

指定 charset 时会忽略 `<meta>`。

### 元素的形态

与 [FREADXML](FREADXML.md#要素の形) 相同，元素会成为包含以下 4 个键的哈希。即使键对应的内容为空，也始终会包含这些键。

| 键 | 值 |
|------|----|
| `name` | 标签名（HTML 元素名为小写，如 `div`、`custom-tag`） |
| `attr` | 属性名 → 属性值的哈希。值全部为字符串。属性名会转换为小写 |
| `children` | 子元素哈希组成的通用数组（按出现顺序排列） |
| `text` | 按顺序连接的直接子文本字符串 |

- 字符引用（如 `&amp;`、`&#x3042;`、`&nbsp;`）会被展开
- `<br>`、`<img>` 等没有内容的元素也会成为 `children` 和 `text` 为空的元素
- 子元素和文本混合存在时，文本与子元素之间的顺序关系会丢失（`<p>a<b>x</b>c</p>` 的 `text` 为 `ac`）
- 对于包含子元素的元素，只包含空白的文本（元素之间的换行或缩进）不会放入 `text`。没有子元素的元素即使只包含空白，也会保留（`<pre> </pre>` 的 `text` 为半角空格）
- `<script>`、`<style>`、`<textarea>` 中的内容也会放入 `text`
- 注释、DOCTYPE、处理指令会被忽略
- SVG、MathML 中的 `xlink:href`、`xml:lang` 等属性会使用带前缀的名称
- 嵌套层数超过 128 层的 HTML 会导致失败（将 `<html>` 计为第 1 层）
- 属性的顺序不会保留，而是按哈希键的顺序排列

### 错误
| 情况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| path 不是字符串 | W0009 | 9 |
| charset 无效 | W0012 / W0009 | 12 / 9 |
| 无法打开文件 | W0025 | 25 |
| 嵌套过深 | W0026（也会输出原因） | 26 |

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
- YAYA：Tc605-1 及び以降の版本

## See Also
- [PARSEHTML](PARSEHTML.md)
- [FREADXML](FREADXML.md)
- [FREADJSON](FREADJSON.md)
- [嵌套值与多维赋值](../grammar/13-nesting.md)
