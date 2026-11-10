# DUMPXML
**Category:** 型取得/変換

## Signature
```
DUMPXML( element [, pretty] )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| element | 表示根元素的哈希（与 [FREADXML](FREADXML.md#要素の形) 返回的形状相同） |
| pretty | 为 1 时添加换行和缩进进行格式化。省略时为 0（输出为一行） |

## Returns
- 成功时：带有 XML 声明（`<?xml version="1.0" encoding="UTF-8"?>`）的 XML 字符串
- 失败时：空字符串

## Description
将元素的哈希转换为 XML 字符串并返回。这是 [PARSEXML](PARSEXML.md) 的逆向转换。

元素哈希的键如下。除 `name` 外，其他键可以省略（也可以为空）。

| 键 | 值 |
|------|----|
| `name` | 标签名（必需）。字符串 |
| `attr` | 属性名 → 属性值的哈希。值可以是整数、实数或字符串（会转换为字符串后写入） |
| `children` | 子元素哈希组成的通用数组 |
| `text` | 元素的文本。整数、实数或字符串 |

- 文本会写在子元素之前。如果通过 [FREADXML](FREADXML.md) 读取的元素同时包含文本和子元素（`<p>a<b>x</b>c</p>`），则无法还原为原来的顺序（会变成 `<p>ac<b>x</b></p>`）
- `&` `<` `>` 以及属性值中的 `"` 会进行转义
- 标签名和属性名只对 ASCII 范围内的字符检查 XML 名称规则（首字符为字母、`_`、`:`，从第二个字符起也可以是数字、`-`、`.`）。日文等非 ASCII 字符也可以使用

格式化时使用4个空格缩进，换行符为 LF。即使在含有文本的元素中，从第二个子元素开始，子元素前也会添加换行和缩进。[FREADXML](FREADXML.md) / [PARSEXML](PARSEXML.md) 会忽略元素之间仅由空白字符组成的文本，因此不会影响读回时的 `text`。

### 错误
| 情况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| 元素不是哈希、没有 `name` 或其值无效、`attr` 不是哈希、属性名无效、属性值或 `text` 是数组或哈希、`children` 不是数组、子元素不是哈希 | W0027（也会输出具体无效的位置） | 27 |

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
- YAYA：Tc602-1及之后

## See Also
- [FWRITEXML](FWRITEXML.md)
- [PARSEXML](PARSEXML.md)
- [DUMPJSON](DUMPJSON.md)
