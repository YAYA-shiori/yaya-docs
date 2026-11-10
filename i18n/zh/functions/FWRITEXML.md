# FWRITEXML
**Category:** ファイル操作

## Signature
```
FWRITEXML( path, element [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要写入的文件路径（相对于 yaya.dll 的路径，或绝对路径） |
| element | 表示根元素的哈希（与 [FREADXML](FREADXML.md#要素の形) 返回的形式相同） |
| charset | 文件的字符编码（可省略）。可指定为字符串（如 `"UTF-8"`、`"Shift_JIS"`。[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）或数值。省略时或为空字符串时，使用 UTF-8（无 BOM） |
| pretty | 为 1 时插入换行和缩进进行格式化。省略时为 1（格式化） |

## Returns
- 成功时：1
- 失败时：0

## Description
将元素的哈希转换为 XML 并写入文件。如果文件已存在，则覆盖。[FOPEN](FOPEN.md) 无需事先打开文件。

元素哈希的形式、转义和格式化形式与 [DUMPXML](DUMPXML.md) 相同。开头会添加与 charset 对应的 XML 声明。

| charset | XML 声明中的 encoding |
|---------|------|
| UTF-8（省略时） | `UTF-8` |
| Shift_JIS | `Shift_JIS` |
| EUC-JP | `EUC-JP` |
| ISO-2022-JP | `ISO-2022-JP` |
| BIG5 | `Big5` |
| GB2312 | `GB2312` |
| EUC-KR | `EUC-KR` |
| default（OS 的字符编码） | 根据 OS 的代码页确定（代码页为 932 时使用 `Shift_JIS`） |

写入的文件会根据 XML 声明中的 encoding 确定编码，因此可以不指定 charset，直接通过 [FREADXML](FREADXML.md) 读回。

无法用 charset 表示的字符（例如 Shift_JIS 中的表情符号），在文本和属性值中会以字符引用 `&#x1F600;` 写入。读回时会还原为原字符。元素名和属性名中的字符无法使用字符引用，因此会因 W0027 而失败。

不会创建目录。无法写入不存在的目录。

### 错误
| 情况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 参数不足 | W0008 | 8 |
| path 不是字符串 | W0009 | 9 |
| charset 无效 | W0012 / W0009 | 12 / 9 |
| 元素哈希无效（参见 [DUMPXML](DUMPXML.md#エラー)） | W0027 | 27 |
| 元素名或属性名中包含无法用 charset 表示的字符 | W0027 | 27 |
| 无法打开文件 | W0025 | 25 |
| 写入失败 | W0013 | 13 |

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
- YAYA：Tc602-1 及以后
- Tc603-1：对于无法用 charset 表示的字符，不再静默写成 `?`，而是使用格式规定的转义序列写入。传入未知的字符编码名称时，会发出警告 W0012 并失败（此前不会发出警告，而是按 OS 默认编码处理）

## See Also
- [DUMPXML](DUMPXML.md)
- [FREADXML](FREADXML.md)
- [FWRITEJSON](FWRITEJSON.md)
