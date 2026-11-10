# CHARSETLIB

**Category:** 外部ライブラリ

## Signature

```
CHARSETLIB(code)
CHARSETLIB()
CHARSETLIB
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| code | （可省略）通过字符编码 ID 或表示字符编码的文本指定字符编码（[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)）。如果名称无法识别，则发出警告 W0012，且不更改设置 |

## Returns

无参数时：以字符串形式返回当前 DLL 字符编码设置
有参数时：VOID（不返回任何内容）

设置与外部库交互时使用的字符编码。必须在 LOADLIB 之前调用。默认编码从设置文件的 charset.extension 项获取（未指定时则从 charset 获取）。

CHARSETLIB 全局应用于所有外部库，而 CHARSETLIBEX 可以按库单独设置。

## Compatibility

- YAYA: 从初版起可用。省略参数的用法从Tc531起支持
- AYA: 5.8版及之后
- Tc574-8 / Tc603-1: 传入无法识别的字符编码名称时，会发出警告 W0012 且不更改设置（此前不会发出警告，而是按 OS 默认值处理）

## See Also

- CHARSETLIBEX
- CHARSETIDTOTEXT
