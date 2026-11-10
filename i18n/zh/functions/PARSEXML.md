# PARSEXML
**Category:** 型取得/変換

## Signature
```
PARSEXML( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | XML 字符串 |

## Returns
- 成功时：表示根元素的哈希
- 失败时：空（VOID）

## Description
解析 XML 字符串，并将根元素转换为哈希后返回。元素的形式与 [FREADXML](FREADXML.md#要素の形) 相同。

字符串已经是 YAYA 字符串，因此会忽略 XML 声明中的 encoding。从文件读取时，请使用 [FREADXML](FREADXML.md)。

### 错误
| 状况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| str 不是字符串 | W0009 | 9 |
| 无法作为 XML 解析 | W0026（同时输出错误内容和行号） | 26 |

## Example
```
_x = PARSEXML('<res code="0"><msg>OK</msg></res>')
_x["attr"]["code"]              // 0（文字列）
_x["children"][0]["text"]       // OK

PARSEXML('<a><b></a>')          // 空（警告 W0026）
```

## Compatibility
- YAYA：Tc601-1 及之后

## See Also
- [FREADXML](FREADXML.md)
- [DUMPXML](DUMPXML.md)
- [PARSEHTML](PARSEHTML.md)
- [PARSEJSON](PARSEJSON.md)
