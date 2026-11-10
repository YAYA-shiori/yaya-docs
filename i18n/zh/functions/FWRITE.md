# FWRITE
**Category:** ファイル操作

## Signature
```
FWRITE( path, string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 通过 FOPEN 打开的文件路径（相对于 yaya.dll） |
| string | 要写入的字符串 |

## Returns
无（VOID）

## Description
向文件写入一行的函数。需要事先使用 FOPEN 打开文件。

写入时会将字符编码从 YAYA 内部格式转换为 FCHARSET 指定的格式。行末会自动添加换行符。

若要写入时不添加换行符，请使用 FWRITE2。

## Compatibility
- YAYA：从早期版本起即可使用
- AYA：5.8 及之后版本

## See Also
- FWRITE2
- FREAD
- FOPEN
- FCHARSET
