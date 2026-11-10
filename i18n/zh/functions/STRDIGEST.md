# STRDIGEST
**Category:** 文字列操作

## Signature
```
STRDIGEST(string [, type])
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| string | 要计算摘要值的字符串 |
| type | 摘要类型（见[下表](#ダイジェストの種類)）。省略时为 `MD5` |

## Returns
- 成功时：计算出的摘要值的十六进制字符串（英文字母大写）
- 失败时：-1

## Description
计算并返回指定字符串的摘要（哈希）值。字符串的字符编码使用内部表示（Windows 版本为 UTF-16，POSIX 版本为 UTF-32）的字节序列。例如，`"abc"` 在 Windows 版本中是 6 个字节：`61 00 62 00 63 00`。

`type` 不区分大小写，并且会忽略 `-` `_` `/`（`SHA-256`、`sha_256` 和 `sha256` 均相同）。指定未知类型时，会按 `MD5` 计算。

### 摘要类型

| type | 内容 | 长度 |
|------|------|------|
| `MD5` | MD5 | 16 字节 |
| `SHA-1` / `SHA1` | SHA-1 | 20 字节 |
| `SHA-224` / `SHA-256` / `SHA-384` / `SHA-512` | SHA-2 | 28 / 32 / 48 / 64 字节 |
| `SHA3-224` / `SHA3-256` / `SHA3-384` / `SHA3-512` | SHA-3 | 28 / 32 / 48 / 64 字节 |
| `Adler-32` | Adler-32（zlib） | 4 字节 |
| `CRC-32` | CRC-32（与 ZIP、PNG 等相同的多项式）。**按低位字节在前排列**（参见下方注意事项） | 4 字节 |
| `CRC-32B`（`CRC-32/ISO-HDLC`） | 与 `CRC-32` 相同的值，采用常见表示方式（高位字节在前） | 4 字节 |
| `CRC-32C`（`CRC-32/CASTAGNOLI`） | CRC-32C（iSCSI、SCTP、ext4 等） | 4 字节 |
| `CRC-32/BZIP2` | CRC-32/BZIP2 | 4 字节 |
| `CRC-32/MPEG-2` | CRC-32/MPEG-2 | 4 字节 |
| `CRC-32/JAMCRC`（`JAMCRC`） | CRC-32/JAMCRC | 4 字节 |
| `CRC-16`（`CRC-16/ARC`） | CRC-16/ARC | 2 字节 |
| `CRC-16/CCITT-FALSE`（`CRC-16/IBM-3740`） | CRC-16/CCITT-FALSE | 2 字节 |
| `CRC-16/XMODEM`（`CRC-16/ZMODEM`） | CRC-16/XMODEM | 2 字节 |
| `CRC-16/KERMIT`（`CRC-16/CCITT-TRUE`） | CRC-16/KERMIT | 2 字节 |
| `CRC-16/MODBUS` | CRC-16/MODBUS | 2 字节 |
| `CRC-16/X-25`（`CRC-16/IBM-SDLC`） | CRC-16/X-25 | 2 字节 |
| `CRC-8`（`CRC-8/SMBUS`） | CRC-8 | 1 字节 |
| `CRC-8/MAXIM`（`CRC-8/DOW`） | CRC-8/MAXIM（Dallas 1-Wire） | 1 字节 |
| `CRC-64`（`CRC-64/XZ`） | CRC-64/XZ（xz、Go 的 ECMA 表） | 8 字节 |
| `CRC-64/ECMA-182` | CRC-64/ECMA-182 | 8 字节 |

CRC 各类型的名称和定义遵循 CRC 目录（基于 Rocksoft 模型的列表）。`CRC-16` 和 `CRC-64` 分别指 `CRC-16/ARC` 和 `CRC-64/XZ`。

!!! note "CRC 的排列顺序"
    仅 `CRC-32` 为保持既有兼容性，会按低位字节在前排列（`123456789` 的 CRC-32 通常表示为 `CBF43926`，但这里会得到 `2639F4CB`）。要以常见表示方式获取结果时，请使用 `CRC-32B`。其他 CRC 均采用与目录相同的常见表示方式（高位字节在前）。

    可用于验证实现的值见 [FDIGEST](FDIGEST.md)。

## Example
```
_h = STRDIGEST("abc", "SHA-256")    // 13E228567E8249FCE53337F25D7970DE3BD68AB2653424C7B8F9FD05E33CAEDF (Windows 版)
```

## Compatibility
- YAYA：Tc568-1 及之后
- Tc607-1：新增 `SHA-224` / `SHA-256` / `SHA-384` / `SHA-512`、`SHA3-*`、`Adler-32` 和 `CRC-32B` 等各种 CRC；类型名称不再区分大小写，并会忽略 `-` `_` `/`

## See Also
- FDIGEST（计算文件摘要）
