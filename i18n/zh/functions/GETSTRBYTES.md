# GETSTRBYTES
**Category:** 文字列操作

## Signature
```
GETSTRBYTES( string [ , code ] )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| string | 要计算字节数的字符串 |
| code | 字符编码 ID（省略时为 0），或字符编码名称（[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）。按指定的编码计算字节数。名称无法识别时会发出警告 W0012 并返回 0 |

## Returns
- 成功时：存储字符串所需的字节数（整数）
- 失败时：0

## Description
计算“存储字符串所需的字节数”的函数。可用于查看不同字符编码下的内存用量。

## Compatibility
- YAYA：从初始版本开始即可使用
- AYA：5.8 及以后版本
- Tc574-8 / Tc603-1：传入无法识别的字符编码名称时，改为发出警告 W0012 并返回 0（此前不会发出警告，而是按 OS 默认值处理）

## See Also
- GETSETTING
- GETSYSTEMFUNCLIST
