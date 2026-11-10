# STRDIGEST
**Category:** 文字列操作

## Signature
```
STRDIGEST(string [, type])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要計算摘要值的字串 |
| type | 摘要類型（[下表](#ダイジェストの種類)）。省略時為 `MD5` |

## Returns
- 成功時：計算所得摘要值的十六進位字串（英文字母為大寫）
- 失敗時：-1

## Description
計算並傳回指定字串的摘要（雜湊）值。字串會使用內部表示法的字元編碼位元組序列（Windows 版為 UTF-16，POSIX 版為 UTF-32）。例如，`"abc"` 在 Windows 版中是 6 個位元組：`61 00 62 00 63 00`。

`type` 不區分大小寫，且會忽略 `-`、`_`、`/`（`SHA-256`、`sha_256`、`sha256` 都相同）。指定不明的類型時，會以 `MD5` 計算。

### 摘要類型

| type | 內容 | 長度 |
|------|------|------|
| `MD5` | MD5 | 16 位元組 |
| `SHA-1` / `SHA1` | SHA-1 | 20 位元組 |
| `SHA-224` / `SHA-256` / `SHA-384` / `SHA-512` | SHA-2 | 28 / 32 / 48 / 64 位元組 |
| `SHA3-224` / `SHA3-256` / `SHA3-384` / `SHA3-512` | SHA-3 | 28 / 32 / 48 / 64 位元組 |
| `Adler-32` | Adler-32（zlib） | 4 位元組 |
| `CRC-32` | CRC-32（與 ZIP、PNG 等相同的多項式）。**從低位元組開始排列**（請參閱下方注意事項） | 4 位元組 |
| `CRC-32B`（`CRC-32/ISO-HDLC`） | 與 `CRC-32` 相同的值，以一般表示法（從高位元組開始）輸出 | 4 位元組 |
| `CRC-32C`（`CRC-32/CASTAGNOLI`） | CRC-32C（iSCSI、SCTP、ext4 等） | 4 位元組 |
| `CRC-32/BZIP2` | CRC-32/BZIP2 | 4 位元組 |
| `CRC-32/MPEG-2` | CRC-32/MPEG-2 | 4 位元組 |
| `CRC-32/JAMCRC`（`JAMCRC`） | CRC-32/JAMCRC | 4 位元組 |
| `CRC-16`（`CRC-16/ARC`） | CRC-16/ARC | 2 位元組 |
| `CRC-16/CCITT-FALSE`（`CRC-16/IBM-3740`） | CRC-16/CCITT-FALSE | 2 位元組 |
| `CRC-16/XMODEM`（`CRC-16/ZMODEM`） | CRC-16/XMODEM | 2 位元組 |
| `CRC-16/KERMIT`（`CRC-16/CCITT-TRUE`） | CRC-16/KERMIT | 2 位元組 |
| `CRC-16/MODBUS` | CRC-16/MODBUS | 2 位元組 |
| `CRC-16/X-25`（`CRC-16/IBM-SDLC`） | CRC-16/X-25 | 2 位元組 |
| `CRC-8`（`CRC-8/SMBUS`） | CRC-8 | 1 位元組 |
| `CRC-8/MAXIM`（`CRC-8/DOW`） | CRC-8/MAXIM（Dallas 1-Wire） | 1 位元組 |
| `CRC-64`（`CRC-64/XZ`） | CRC-64/XZ（xz、Go 的 ECMA 表） | 8 位元組 |
| `CRC-64/ECMA-182` | CRC-64/ECMA-182 | 8 位元組 |

CRC 各類型的名稱和定義依據 CRC 型錄（以 Rocksoft 模型整理的列表）。`CRC-16` 和 `CRC-64` 分別指 `CRC-16/ARC` 和 `CRC-64/XZ`。

!!! note "CRC 的排列順序"
    為了維持舊版相容性，只有 `CRC-32` 會從值的低位元組開始排列（`123456789` 的 CRC-32 一般表示為 `CBF43926`，此處則會是 `2639F4CB`）。若要使用一般表示法，請使用 `CRC-32B`。其他 CRC 都採用與型錄相同的一般表示法（從高位元組開始）。

    可用於確認實作的值列於 [FDIGEST](FDIGEST.md)。

## Example
```
_h = STRDIGEST("abc", "SHA-256")    // 13E228567E8249FCE53337F25D7970DE3BD68AB2653424C7B8F9FD05E33CAEDF (Windows 版)
```

## Compatibility
- YAYA：Tc568-1 之後
- Tc607-1：新增 `SHA-224` / `SHA-256` / `SHA-384` / `SHA-512`、`SHA3-*`、`Adler-32` 及 `CRC-32B` 等各種 CRC。類型名稱不區分大小寫，且會忽略 `-`、`_`、`/`

## See Also
- FDIGEST（計算檔案摘要）
