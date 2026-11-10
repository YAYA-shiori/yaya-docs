# STRDECODE
**Category:** 文字列操作

## Signature
```
STRDECODE(string [, code] [, type])
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| string | 要解码的字符串 |
| code | 用于转换的字符编码 ID（省略时为 0），或字符编码名称（[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）。如果名称未知，会发出警告 W0012 并返回 0 |
| type | 解码格式。指定 `url`（URL 编码）或 `base64`（Base64）。省略时为 `url` |

## Returns
- 成功时：解码后的字符串
- 失败时：0

## Description
使用指定的字符编码和编码格式解码字符串。字符编码 ID 请参阅[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)。

## Compatibility
- YAYA：Tc521-1 及之后（Tc532-1 中从 `GETSTRURLDECODE` 更名）
- Tc574-8 / Tc603-1：传入未知的字符编码名称时，会发出警告 W0012 并返回 0（此前不会发出警告，而是按操作系统默认值处理）

## See Also
- STRENCODE（编码函数）
