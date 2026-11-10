# FREADXML
**Category:** ファイル操作

## Signature
```
FREADXML( path [, charset] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要读取的 XML 文件路径（相对于 yaya.dll 的路径，或绝对路径） |
| charset | 文件的字符编码（可省略）。可指定为字符串（`"UTF-8"` `"Shift_JIS"` 等。[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）或数值。省略时按下述方式自动确定 |

## Returns
- 成功时：表示根元素的哈希（参见下方的[元素结构](#要素の形)）
- 失败时：空值（VOID）

## Description
读取并解析整个 XML 文件，将根元素转换为哈希后返回。无需使用 [FOPEN](FOPEN.md) 打开文件。

XML 解析使用 [TinyXML-2](https://github.com/ponapalt/tinyxml2)。

省略 charset 时，按以下顺序确定字符编码。

1. 如果文件开头有 UTF-8 BOM，则使用 UTF-8
2. 使用 XML 声明（`<?xml version="1.0" encoding="Shift_JIS"?>`）中的 encoding。`Windows-31J` `CP932` 也按 Shift_JIS 处理
3. 如果两者都没有，或者 encoding 是 YAYA 不认识的字符编码，则使用 UTF-8

指定 charset 时，会忽略 XML 声明中的 encoding。

### 元素结构

元素会变成一个包含以下4个键的哈希。即使内容为空，这些键也始终存在。

| 键 | 值 |
|------|----|
| `name` | 标签名（如果有命名空间前缀，则保留为 `ns:tag`） |
| `attr` | 属性名 → 属性值的哈希。所有值均为字符串 |
| `children` | 子元素哈希组成的通用数组（按出现顺序排列） |
| `text` | 按顺序拼接直属文本（包括 CDATA）后得到的字符串 |

- 实体引用（如 `&amp;` `&#x3042;`）会被展开
- 文本前后的空格和换行会原样保留。元素之间仅包含空白的部分不会放入 `text`
- 子元素和文本混合时，文本与子元素的先后关系会丢失（`<p>a<b>x</b>c</p>` 的 `text` 为 `ac`）
- 注释、处理指令、DOCTYPE、XML 声明都会被忽略。根元素之外的内容也不会返回
- 属性顺序不会保留，而是按哈希键的顺序排列

### 错误
| 情况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| path 不是字符串 | W0009 | 9 |
| charset 无效 | W0012 / W0009 | 12 / 9 |
| 无法打开文件 | W0025 | 25 |
| 无法作为 XML 解析 | W0026（也会输出错误内容和行号） | 26 |

## Example
shop.xml：
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
- YAYA：Tc601-1及以后
- Tc603-1：传入未知字符编码名称时，会发出警告 W0012 并失败（此前不会发出警告，而是按 OS 默认编码处理）

## See Also
- [PARSEXML](PARSEXML.md)
- [FWRITEXML](FWRITEXML.md)
- [FREADHTML](FREADHTML.md)
- [FREADJSON](FREADJSON.md)
- [嵌套值与多维赋值](../grammar/13-nesting.md)
