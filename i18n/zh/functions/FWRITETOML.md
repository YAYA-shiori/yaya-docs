# FWRITETOML
**Category:** ファイル操作

## Signature
```
FWRITETOML( path, value [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要写入的文件路径（相对于 yaya.dll 的路径，或绝对路径） |
| value | 转换为 TOML 的哈希（包括嵌套结构） |
| charset | 文件的字符编码（可省略）。可指定为字符串（如 `"UTF-8"`、`"Shift_JIS"`。[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）或数值。省略时或为空字符串时，使用 UTF-8（无 BOM）。TOML 规范规定使用 UTF-8，因此通常省略此参数 |
| pretty | 为 1 时使用 `[表]` 标题进行格式化，为 0 时每个最顶层的键占一行。省略时为 1 |

## Returns
- 成功时：1
- 失败时：0

## Description
将哈希转换为 TOML 并写入文件。如果文件已存在，则覆盖。[FOPEN](FOPEN.md) 无需事先打开文件。

值的对应方式和格式化形式与 [DUMPTOML](DUMPTOML.md#値の対応) 相同。

写入的文件可以通过 [FREADTOML](FREADTOML.md) 读回。

包含无法用 charset 表示的字符（例如 Shift_JIS 中的表情符号）的字符串，不会用 `'...'` 括起，而是用 `"..."` 括起（包含换行时用 `"""..."""`），并将该字符写成 `\uXXXX`（BMP 以外的字符写成 `\U0001F600` 这样的 8 位形式）。键也一样。读回时会还原为原字符。

不会创建目录。无法写入不存在的目录。

### 错误
| 情况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 参数不足 | W0008 | 8 |
| path 不是字符串 | W0009 | 9 |
| charset 无效 | W0012 / W0009 | 12 / 9 |
| value 不是哈希，或数组元素中包含空值（VOID） | W0027（也会输出原因） | 27 |
| 无法打开文件 | W0025 | 25 |
| 字符编码转换本身失败 | W0027 | 27 |
| 写入失败 | W0013 | 13 |

## Example
```
_conf = IHASH()
_conf["volume"] = 80
_conf["friends"] = ("うにゅう", "まゆら")
_conf["memo"] = "1行目" + CHR(10) + "2行目"

FWRITETOML("config.toml", _conf)
// config.toml:
// friends = ["うにゅう", "まゆら"]
// memo = """
// 1行目
// 2行目"""
// volume = 80
```

## Compatibility
- YAYA：Tc602-5 及以后
- Tc603-1：对于无法用 charset 表示的字符，不再静默写成 `?`，而是使用格式规定的转义序列写入。传入未知的字符编码名称时，会发出警告 W0012 并失败（此前不会发出警告，而是按 OS 默认编码处理）

## See Also
- [DUMPTOML](DUMPTOML.md)
- [FREADTOML](FREADTOML.md)
- [FWRITEJSON](FWRITEJSON.md)
- [FWRITEYAML](FWRITEYAML.md)
