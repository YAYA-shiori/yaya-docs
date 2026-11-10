# PARSEJSON
**Category:** 型取得/変換

## Signature
```
PARSEJSON( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | JSON 字符串 |

## Returns
- 成功时：转换 JSON 后得到的值
- 失败时：空（VOID）

## Description
解析 JSON 字符串，并将其作为哈希、数组等值返回。值的对应关系以及注释的处理方式与 [FREADJSON](FREADJSON.md#値の対応) 相同。

处理从 SAORI 或外部接收的 JSON 字符串时使用。要从文件读取时，请使用 [FREADJSON](FREADJSON.md)。

### 错误
| 状况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| str 不是字符串 | W0009 | 9 |
| 无法作为 JSON 解析 | W0026 | 26 |

## Example
```
_j = PARSEJSON('{"result": [{"id": 1, "text": "こんにちは"}]}')
_j["result"][0]["text"]     // こんにちは
_j["result"][0]["id"]       // 1

PARSEJSON('[1, 2.5, "a"]')  // 整数 1、実数 2.5、文字列 a の汎用配列
PARSEJSON('{')              // 空（警告 W0026）
```

## Compatibility
- YAYA：Tc601-1 及以后
- Tc602-1：修复了在小数点为 `,` 的区域设置（例如德语）环境中，解析包含小数的 JSON 会失败的问题

## See Also
- [FREADJSON](FREADJSON.md)
- [DUMPJSON](DUMPJSON.md)
- [PARSEXML](PARSEXML.md)
