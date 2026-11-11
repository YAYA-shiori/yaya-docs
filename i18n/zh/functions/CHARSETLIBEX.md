# CHARSETLIBEX

**Category:** 外部ライブラリ

## Signature

```
CHARSETLIBEX(path, code)
CHARSETLIBEX(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | DLL 文件的位置。指定相对于 YAYA 目录的路径，或绝对路径 |
| code | （可省略）字符编码 ID 或表示字符编码的文本标识符（[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）。如果是未知名称，则发出警告 W0012，且不更改设置 |

## Returns

省略 code 时：以字符串形式返回指定 DLL 当前的字符编码设置
指定 code 时：VOID（不返回任何内容）

单独指定与外部库交互时使用的字符编码。从 Tc530-2 起，在调用 LOADLIB 之前调用即可生效，并且可以在“初始化中”设置。建议在初始化时预先使用此函数指定字符编码。默认编码从设置文件的 charset.extension 项（未指定时为 charset）中获取。不过，POSIX 环境下 SAORI-basic（Tc604-1 及更高版本）的默认值为 UTF-8。

## Compatibility

- YAYA：从初始版本起可用。省略参数的功能从 Tc531 起可用
- Tc574-8 / Tc603-1：传入未知的字符编码名称时，将发出警告 W0012，且不更改设置（此前不会发出警告，而是作为 OS 默认值处理）

## See Also

- CHARSETLIB
- CHARSETTEXTTOID
