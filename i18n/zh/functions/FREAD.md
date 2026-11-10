# FREAD

**Category:** ファイル操作

## Signature

```
FREAD(path)
```

## Parameters

| 参数 | 说明 |
|-----------|-------------|
| path | 由 FOPEN 指定的文件相对路径（相对于 yaya.dll） |

## Returns

- 成功时：读取到的一行字符串（会移除 CR、LF 等行末字符）。从 FCHARSET 指定的字符编码转换为 YAYA 的内部编码
- 到达文件末尾时：-1
- 失败时：空字符串

必须预先用 FOPEN 打开文件。

## Description

从文件中读取一行。

- 调用 `FREAD` 之前，必须先用 `FOPEN` 打开文件
- 字符编码会从 `FCHARSET` 指定的字符编码转换为 YAYA 内部使用的字符编码
- 会移除行末的换行符（CR、LF）

### 注意

如果为了检测 EOF 而编写如下代码，当文件中存在「只写有 `-1` 的行」时，可能会将其误认为 EOF，导致读取提前结束。

```
_line = FREAD(_filename);
if(_line == -1) { break; }
```

可以按如下方式避免这种情况。

```
_line = FREAD(_filename);
if(GETTYPE(_line) == 1 && _line == -1) { break; }
```

EOF 的 `-1` 是整数值，而从文件读取的 `"-1"` 是字符串，因此可以用 [GETTYPE](GETTYPE.md) 检查值的类型，仅在其为「整数值 `-1`」时将其视为 EOF。

## Compatibility

- YAYA：从首次发布起即可使用
- AYA：5.8 及以上版本

## See Also

- FWRITE
- FREADBIN
- FOPEN
- FREADENCODE
- FWRITE2
- FCHARSET
