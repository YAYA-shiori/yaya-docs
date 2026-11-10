# PARSETOML
**Category:** 型取得/変換

## Signature
```
PARSETOML( str )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | TOML 字符串 |

## Returns
- 成功时：转换 TOML 后得到的哈希
- 失败时：空（VOID）

## Description
解析 TOML 字符串，并将其转换为哈希后返回。值的对应关系与 [FREADTOML](FREADTOML.md#値の対応) 相同。

从文件读取时，请使用 [FREADTOML](FREADTOML.md)。

### 错误
| 状况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 没有参数 | W0008 | 8 |
| str 不是字符串 | W0009 | 9 |
| 无法作为 TOML 解析 | W0026（也会输出行号和原因） | 26 |

## Example
```
_t = PARSETOML("a = 1" + CHR(10) + "b.c = 'x'")
_t["a"]                     // 1
_t["b"]["c"]                // x

PARSETOML("a = 1" + CHR(10) + "a = 2")
// 空（警告 W0026 : line 2 : duplicate key : a）
```

## Compatibility
- YAYA：Tc602-5 及更高版本

## See Also
- [FREADTOML](FREADTOML.md)
- [DUMPTOML](DUMPTOML.md)
- [PARSEJSON](PARSEJSON.md)
- [PARSEYAML](PARSEYAML.md)
