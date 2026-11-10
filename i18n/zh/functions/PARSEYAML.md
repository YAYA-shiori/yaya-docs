# PARSEYAML
**Category:** 型取得/変換

## Signature
```
PARSEYAML( str )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| str | YAML 字符串 |

## Returns
- 成功时：转换后的 YAML 值
- 失败时：空（VOID）

## Description
解析 YAML 字符串，并将其作为哈希、数组等值返回。支持的写法及其对应的值与 [FREADYAML](FREADYAML.md#対応している書き方) 相同。

从文件读取时，请使用 [FREADYAML](FREADYAML.md)。

### 错误
| 情况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| str 不是字符串 | W0009 | 9 |
| 无法作为 YAML 解析，或使用了不支持的写法 | W0026（同时输出行号和原因） | 26 |

## Example
```
_y = PARSEYAML("{name: さくら, tags: [ghost, shell]}")
_y["name"]                  // さくら
_y["tags"][1]               // shell

PARSEYAML("- 1" + CHR(10) + "- 0x10" + CHR(10) + "- yes" + CHR(10) + "- '007'")
// 整数 1、整数 16、文字列 yes、文字列 007 の汎用配列

PARSEYAML("a: [1")          // 空（警告 W0026）
```

## Compatibility
- YAYA：Tc602-5 及以后

## See Also
- [FREADYAML](FREADYAML.md)
- [DUMPYAML](DUMPYAML.md)
- [PARSEJSON](PARSEJSON.md)
- [PARSETOML](PARSETOML.md)
