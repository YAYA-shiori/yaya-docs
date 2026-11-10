# FWRITEBIN
**Category:** ファイル操作

## Signature
```
FWRITEBIN( path, string [, char] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 通过 FOPEN 指定的文件名 |
| string | 要写入的字符串 |
| char | 替代字节值 0x00 的字符（省略时为半角空格） |

## Returns
无

## Description
不进行字符编码转换而写入数据的函数。需要事先使用 FOPEN 打开文件。

如果未以二进制模式打开文件，则会进行换行符转换。

由于 YAYA 的字符串无法包含 null 字节，`char` 指定的字符会被转换为字节值 0。

## Compatibility
- YAYA：Tc516-901 及之后

## See Also
- FWRITE
- FREADBIN
- FOPEN
