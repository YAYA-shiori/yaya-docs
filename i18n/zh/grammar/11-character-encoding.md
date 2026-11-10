# 字符编码相关

## 内部字符编码

YAYA 使用 **UCS-2** 作为内部字符编码。在进行词典操作、文件 I/O 以及与外部库交互时，所有字符串都会自动转换为 UCS-2，或从 UCS-2 转换为相应编码。

## 字符编码 ID 系统

部分函数使用数值 ID 来指定字符编码。对于可以通过名称指定的函数，请使用文本形式的名称（[字符编码名称](#文字コードの名前)）：

| 编码 | 文本形式 | ID |
|----------------|------------|-----|
| Shift JIS | Shift_JIS | 0 |
| UTF-8 | UTF-8 | 1 |
| EUC-JP | EUC-JP | 2 |
| Big5 | Big5 | 3 |
| GB2312 | GB2312 | 4 |
| EUC-KR | EUC-KR | 5 |
| ISO-2022-JP (JIS) | ISO-2022-JP | 6 |
| 二进制 | binary | 126 |
| OS 默认 | default（OSNative 也相同） | 127 |

## 字符编码名称

通过名称指定字符编码时，请使用上表中的文本形式。名称不区分大小写。

将无法使用的名称（如 `UTF-16`、`ISO-8859-1`）传递给系统函数时，会发出警告 W0012 并执行失败（GETLASTERROR 为 12）。具体的失败方式请参阅各函数对应的页面。在 Tc574-8 / Tc603-1 之前，遇到这种情况不会发出警告，而是按 OS 默认编码处理。

在配置文件（如 `charset`）中填写无法使用的名称时，仍会像以往一样不发出警告，并使用 OS 默认编码。

## 二进制编码的特殊情况

二进制格式是一种特殊的字符编码，它会「将 UCS-2 字符串的低位字节直接转换为字节序列」。这种格式是为 `FWRITEBIN`、`FREADBIN` 等函数设计的，用于在不进行转换的情况下交换数据。

**重要限制：** 即使在二进制模式下，YAYA 也无法处理字符串中的空字节（0x00）。此外，`FUNCTIONEX` 等现有系统词典并未考虑二进制字符串值。

## 相关内容

- [CHARSETLIB](../functions/CHARSETLIB.md)
- [CHARSETLIBEX](../functions/CHARSETLIBEX.md)
- [CHARSETIDTOTEXT](../functions/CHARSETIDTOTEXT.md)
- [CHARSETTEXTTOID](../functions/CHARSETTEXTTOID.md)
- [FCHARSET](../functions/FCHARSET.md)
- [STRENCODE](../functions/STRENCODE.md)
- [STRDECODE](../functions/STRDECODE.md)
