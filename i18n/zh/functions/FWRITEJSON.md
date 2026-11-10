# FWRITEJSON
**Category:** ファイル操作

## Signature
```
FWRITEJSON( path, value [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要写入文件的路径（相对于 yaya.dll 的路径，或绝对路径） |
| value | 转换为 JSON 的值。哈希或数组（包括嵌套结构）也可以作为一个参数传入 |
| charset | 文件的字符编码（可省略）。可以指定字符串（如 `"UTF-8"`、`"Shift_JIS"`。[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）或数值。省略时或为空字符串时，使用 UTF-8（无 BOM） |
| pretty | 为 1 时，添加换行和缩进进行格式化。省略时为 1（格式化） |

## Returns
- 成功时：1
- 失败时：0

## Description
将值转换为 JSON 并写入文件。若文件已存在，则覆盖。无需使用 [FOPEN](FOPEN.md) 预先打开文件。

值的支持范围和格式化方式与 [DUMPJSON](DUMPJSON.md#値の対応) 相同。格式化时，会在文件末尾添加换行符（LF）。

写入的文件可以通过 [FREADJSON](FREADJSON.md) 读回（以 UTF-8 以外的编码写入时，请指定相同的 charset）。

无法用 charset 表示的字符（例如 Shift_JIS 中的表情符号）会以 JSON 转义序列 `\uXXXX` 写入（BMP 范围之外的字符会以代理对形式写成两个转义序列，例如 `\uD83D\uDE00`）。读回时会还原为原字符。

不会创建目录。无法写入不存在的目录。

### 错误
| 情况 | 警告 | [GETLASTERROR](GETLASTERROR.md) |
|------|------|------|
| 参数不足 | W0008 | 8 |
| path 不是字符串 | W0009 | 9 |
| charset 无效 | W0012 / W0009 | 12 / 9 |
| 无法打开文件 | W0025 | 25 |
| 字符编码转换本身失败 | W0027 | 27 |
| 写入失败 | W0013 | 13 |

## Example
```
_conf = IHASH()
_conf["volume"] = 80
_conf["friends"] = ("うにゅう", "まゆら")

FWRITEJSON("config.json", _conf)
// config.json:
// {
//     "friends": [
//         "うにゅう",
//         "まゆら"
//     ],
//     "volume": 80
// }

FWRITEJSON("config.min.json", _conf, "", 0)   // UTF-8 で1行に
```

## Compatibility
- YAYA：Tc602-1 及之后
- Tc603-1：对于无法用 charset 表示的字符，改为使用格式规定的转义序列写入，而不是默默替换为 `?`。传入未知字符编码名称时，会发出警告 W0012 并失败（此前不会发出警告，而是按操作系统默认编码处理）

## See Also
- [DUMPJSON](DUMPJSON.md)
- [FREADJSON](FREADJSON.md)
- [FWRITEXML](FWRITEXML.md)
