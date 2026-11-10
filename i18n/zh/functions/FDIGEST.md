# FDIGEST

**Category:** ファイル操作

## Signature

```
FDIGEST(path [, type])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 要计算摘要值的文件路径。可以指定完整路径。相对路径以 DLL 的加载位置为基准 |
| type | 摘要类型。MD5、SHA-1、SHA-2、SHA-3、Adler-32、各种 CRC。类型列表请参见 [STRDIGEST](STRDIGEST.md#ダイジェストの種類)。省略时为 `MD5` |

## Returns

- 成功时：以十六进制字符串（大写字母）返回摘要值
- 失败时（文件不存在或无法生成值）：-1

## Description

获取指定文件的摘要（哈希）值。路径可以指定为完整路径。对于相对路径，以 DLL load 所传入的位置（通常是 DLL 所在位置）为基准。

`type` 的写法，以及只有 `CRC-32` 会从值的低位字节开始排列这一点，均与 [STRDIGEST](STRDIGEST.md) 相同。本函数直接根据文件内容的字节序列计算，而不是根据字符串的内部表示计算，因此可以与其他工具的结果进行比较。

### 用于确认的值

仅包含 `123456789`（9 字节，不含换行符）的文件的值。

| type | 值 |
|------|----|
| `Adler-32` | `091E01DE` |
| `CRC-32` | `2639F4CB` |
| `CRC-32B` | `CBF43926` |
| `CRC-32C` | `E3069283` |
| `CRC-32/BZIP2` | `FC891918` |
| `CRC-32/MPEG-2` | `0376E6E7` |
| `CRC-32/JAMCRC` | `340BC6D9` |
| `CRC-16/ARC` | `BB3D` |
| `CRC-16/CCITT-FALSE` | `29B1` |
| `CRC-16/XMODEM` | `31C3` |
| `CRC-16/KERMIT` | `2189` |
| `CRC-16/MODBUS` | `4B37` |
| `CRC-16/X-25` | `906E` |
| `CRC-8` | `F4` |
| `CRC-8/MAXIM` | `A1` |
| `CRC-64/XZ` | `995DC9BBDF1939FA` |
| `CRC-64/ECMA-182` | `6C40DF5F0B497347` |

## Compatibility

- YAYA: 在 Tc527-1 中首次发布。在 Tc530-1 中添加了 CRC32 支持
- Tc607-1: 添加了 `SHA-224` / `SHA-256` / `SHA-384` / `SHA-512`、`SHA3-*`、`Adler-32` 以及 `CRC-32B` 等各种 CRC。类型名称不再区分大小写，并且会忽略 `-` `_` `/`

## See Also

- STRDIGEST
