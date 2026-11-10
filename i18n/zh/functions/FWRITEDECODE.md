# FWRITEDECODE
**Category:** ファイル操作

## Signature
```
FWRITEDECODE( path, string [, type] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 通过 FOPEN 指定的文件名 |
| string | 要写入的已编码字符串 |
| type | 解码方式：`"base64"`、`"url"` 或 `"form"`（省略时为 base64。详情请参阅 [STRDECODE](STRDECODE.md)）。Tc554-1 因实现错误而无法省略 |

## Returns
无

## Description
在将数据从 base64 或 URL 编码解码的同时写入的函数。执行与 FREADENCODE 相反的操作。

需要事先使用 FOPEN 打开文件。如果 FOPEN 未以二进制访问模式打开文件，则会进行换行符转换。即使解码结果中包含字节值 0（0x00），也能正常写入。

## Compatibility
- YAYA：Tc554-1 及之后
- Tc554-1 因实现错误而无法省略 `type`

## See Also
- FWRITE
- FREADENCODE
- STRDECODE
