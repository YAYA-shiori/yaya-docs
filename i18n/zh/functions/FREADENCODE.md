# FREADENCODE

**Category:** ファイル操作

## Signature

```
FREADENCODE(path, size [, type])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 由 FOPEN 指定的文件名 |
| size | 读取的字节数。指定 0 时读取整个文件 |
| type | 编码类型。为 "base64"、"url"、"form" 之一。省略时为 "base64"（详情参见 STRENCODE） |

## Returns

- 成功时：编码后的字符串
- 到达文件末尾时：-1
- 失败时：空字符串

读取文件时将其编码为 Base64 或 URL 编码。如果未以二进制模式打开文件，则会进行换行符转换。需要事先使用 FOPEN 打开文件。

## Compatibility

- YAYA: Tc535-1 及更高版本

## See Also

- FREAD
- FREADBIN
- FOPEN
- STRENCODE
