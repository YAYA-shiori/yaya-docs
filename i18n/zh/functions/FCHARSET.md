# FCHARSET

**Category:** ファイル操作

## Signature

```
FCHARSET( code )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| code | 要设置的字符编码 ID，或字符编码名称（[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）。若名称不受识别，则发出警告 W0012，并且不更改设置 |

## Returns

无返回值（VOID）。

## Description

指定文件读写所用的字符编码。必须在 FOPEN 之前调用。可以按文件更改字符编码；字符编码在调用 FOPEN 时确定。设置会在人格当前会话期间保持，但会在会话结束后重置。不调用 FCHARSET 时，默认字符编码遵循基本设置文件中 charset.file 或 charset 的设置。

## Compatibility

- YAYA: 从初版起支持
- AYA: 5.8 及以上版本
- Tc574-8 / Tc603-1: 传入不受识别的字符编码名称时，会发出警告 W0012，且不更改设置（在此之前不会发出警告，而是按 OS 默认值处理）

## See Also

- FOPEN
- FCLOSE
- FATTRIB
