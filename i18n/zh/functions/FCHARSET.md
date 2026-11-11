# FCHARSET

**Category:** ファイル操作

## Signature

```
FCHARSET( code )
```

## Parameters

| 参数 | 说明 |
|-----------|-------------|
| code | 要设置的字符编码 ID，或字符编码名称（[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）。如果名称未知，则发出警告 W0012，不更改设置 |

## Returns

无返回值（VOID）。

## Description

指定读写文件时使用的字符编码。必须在调用 FOPEN 之前调用。可以为每个文件更改字符编码，字符编码在调用 FOPEN 时确定。设置在人格当前会话期间保持有效，但结束后会重置。如果未调用 FCHARSET，则默认字符编码遵循基础设置文件中的 charset.file 或 charset 设置。

使用 UTF-8 时，读取文件如果发现文件开头有 BOM（Byte Order Mark），会自动将其删除。使用 UTF-8 写入时不会写入 BOM。

## Compatibility

- YAYA：从初版开始支持
- AYA：5.8 及以上版本
- Tc574-8 / Tc603-1：传入未知字符编码名称时，改为发出警告 W0012 且不更改设置（此前不会发出警告，而是按操作系统默认值处理）

## See Also

- FOPEN
- FCLOSE
- FATTRIB
