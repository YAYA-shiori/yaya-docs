# STRDIGEST
**Category:** 文字列操作

## Signature
```
STRDIGEST(string [, type])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String to calculate the digest value for |
| type | Digest type ([see table below](#ダイジェストの種類)). Defaults to `MD5` |

## Returns
- On success: Calculated digest value as a hexadecimal string (uppercase letters)
- On failure: -1

## Description
Calculates and returns the digest (hash) value of the specified string. The string's character encoding is the byte sequence of its internal representation (UTF-16 on Windows and UTF-32 on POSIX). For example, `"abc"` is 6 bytes on Windows: `61 00 62 00 63 00`.

`type` is case-insensitive, and `-`, `_`, and `/` are ignored (`SHA-256`, `sha_256`, and `sha256` are all equivalent). If an unknown type is specified, the value is calculated as `MD5`.

### Digest Types

| type | Description | Length |
|------|------|------|
| `MD5` | MD5 | 16 bytes |
| `SHA-1` / `SHA1` | SHA-1 | 20 bytes |
| `SHA-224` / `SHA-256` / `SHA-384` / `SHA-512` | SHA-2 | 28 / 32 / 48 / 64 bytes |
| `SHA3-224` / `SHA3-256` / `SHA3-384` / `SHA3-512` | SHA-3 | 28 / 32 / 48 / 64 bytes |
| `Adler-32` | Adler-32 (zlib) | 4 bytes |
| `CRC-32` | CRC-32 (same polynomial as ZIP, PNG, etc.). **Bytes are ordered least significant first** (see note below) | 4 bytes |
| `CRC-32B` (`CRC-32/ISO-HDLC`) | Same value as `CRC-32`, in the conventional representation (most significant byte first) | 4 bytes |
| `CRC-32C` (`CRC-32/CASTAGNOLI`) | CRC-32C (iSCSI, SCTP, ext4, etc.) | 4 bytes |
| `CRC-32/BZIP2` | CRC-32/BZIP2 | 4 bytes |
| `CRC-32/MPEG-2` | CRC-32/MPEG-2 | 4 bytes |
| `CRC-32/JAMCRC` (`JAMCRC`) | CRC-32/JAMCRC | 4 bytes |
| `CRC-16` (`CRC-16/ARC`) | CRC-16/ARC | 2 bytes |
| `CRC-16/CCITT-FALSE` (`CRC-16/IBM-3740`) | CRC-16/CCITT-FALSE | 2 bytes |
| `CRC-16/XMODEM` (`CRC-16/ZMODEM`) | CRC-16/XMODEM | 2 bytes |
| `CRC-16/KERMIT` (`CRC-16/CCITT-TRUE`) | CRC-16/KERMIT | 2 bytes |
| `CRC-16/MODBUS` | CRC-16/MODBUS | 2 bytes |
| `CRC-16/X-25` (`CRC-16/IBM-SDLC`) | CRC-16/X-25 | 2 bytes |
| `CRC-8` (`CRC-8/SMBUS`) | CRC-8 | 1 byte |
| `CRC-8/MAXIM` (`CRC-8/DOW`) | CRC-8/MAXIM (Dallas 1-Wire) | 1 byte |
| `CRC-64` (`CRC-64/XZ`) | CRC-64/XZ (xz and Go's ECMA table) | 8 bytes |
| `CRC-64/ECMA-182` | CRC-64/ECMA-182 | 8 bytes |

The names and definitions of the CRC types follow the CRC catalogue (the list based on the Rocksoft model). `CRC-16` and `CRC-64` refer to `CRC-16/ARC` and `CRC-64/XZ`, respectively.

!!! note "CRC byte order"
    For compatibility with previous behavior, `CRC-32` is the only type whose value is ordered with the least significant byte first (the CRC-32 of `123456789` is generally written as `CBF43926`, but here it is `2639F4CB`). Use `CRC-32B` to get the conventional representation. All other CRC types use the conventional representation in the catalogue (most significant byte first).

    Values for verifying the implementation are available in [FDIGEST](FDIGEST.md).

## Example
```
_h = STRDIGEST("abc", "SHA-256")    // 13E228567E8249FCE53337F25D7970DE3BD68AB2653424C7B8F9FD05E33CAEDF (Windows 版)
```

## Compatibility
- YAYA: Tc568-1 or later
- Tc607-1: Added `SHA-224` / `SHA-256` / `SHA-384` / `SHA-512`, `SHA3-*`, `Adler-32`, and various CRC types such as `CRC-32B`. Type names are now case-insensitive, and `-`, `_`, and `/` are ignored

## See Also
- FDIGEST (calculate a file digest)
