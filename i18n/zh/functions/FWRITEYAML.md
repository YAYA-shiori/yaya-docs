# FWRITEYAML
**Category:** ファイル操作

## Signature
```
FWRITEYAML( path, value [, charset [, pretty]] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要写入的文件路径（相对于 yaya.dll 的路径，或绝对路径） |
| value | 要转换为 YAML 的值。哈希和数组（包括嵌套结构）也可以作为一个参数传入 |
| charset | 文件的字符编码（可省略）。可以指定字符串（如 `"UTF-8"`、`"Shift_JIS"`。[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）或数值。省略时或为空字符串时，使用 UTF-8（无 BOM） |
| pretty | 为 1 时使用块格式，为 0 时使用流格式并写为一行。省略时为 1 |

## Returns
- 成功时：1
- 失败时：0

## Description
将值转换为 YAML 并写入文件。如果文件已存在，则覆盖该文件。无需使用 [FOPEN](FOPEN.md) 预先打开文件。

值的对应关系和格式化方式与 [DUMPYAML](DUMPYAML.md#値の対応) 相同。使用块格式时，会在文件末尾添加换行符（LF）。

写入的文件可以通过 [FREADYAML](FREADYAML.md) 读回（使用 UTF-8 以外的编码写入时，请指定相同的 charset）。

字符串中包含 charset 无法表示的字符（例如 Shift_JIS 中的表情符号）时，不会使用不带引号的形式或块标量（`|`），而是用 `"..."` 括起，并将该字符写为 `\uXXXX`（BMP 范围以外的字符写为类似 `\U0001F600` 的 8 位形式）。键也一样。读回时会还原为原字符。

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
_conf["memo"] = "1行目" + CHR(10) + "2行目"

FWRITEYAML("config.yaml", _conf)
// config.yaml:
// friends:
//   - うにゅう
//   - まゆら
// memo: |-
//   1行目
//   2行目
// volume: 80

FWRITEYAML("config.flow.yaml", _conf, "", 0)
// {friends: [うにゅう, まゆら], memo: "1行目\n2行目", volume: 80}
```

## Compatibility
- YAYA：Tc602-5 及以后
- Tc603-1：修改为遇到 charset 无法表示的字符时，不再静默转换成 `?`，而是使用格式对应的转义形式写入。传入未知字符编码名称时，会发出警告 W0012 并失败（此前不会发出警告，而是按 OS 默认编码处理）

## See Also
- [DUMPYAML](DUMPYAML.md)
- [FREADYAML](FREADYAML.md)
- [FWRITEJSON](FWRITEJSON.md)
- [FWRITETOML](FWRITETOML.md)
