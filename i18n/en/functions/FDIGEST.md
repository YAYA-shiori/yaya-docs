# FDIGEST

**Category:** ファイル操作

## Signature

```
FDIGEST(path [, type])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | Path to the file whose digest value is to be calculated. A full path can be specified. Relative paths are based on the DLL load location |
| type | Digest type: MD5, SHA-1, SHA-2, SHA-3, Adler-32, or various CRC types. See [STRDIGEST](STRDIGEST.md#ダイジェストの種類) for the list. Defaults to `MD5` if omitted |

## Returns

- On success: Returns the digest value as a hexadecimal string (uppercase letters)
- On failure (if the file does not exist or value generation fails): -1

## Description

Gets the digest (hash) value of the specified file. A full path can be specified. Relative paths are based on the location passed to DLL load (in most cases, the location of the DLL).

The syntax for `type` and the fact that only `CRC-32` lists the least significant byte first are the same as for [STRDIGEST](STRDIGEST.md). Since the calculation uses the file's contents as-is, as a byte sequence, rather than the internal representation of a string, the result can be checked against those from other tools.

### Test Values

The value for a file containing only `123456789` (9 bytes, no newline).

| type | Value |
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

- YAYA: First released in Tc527-1. CRC32 support added in Tc530-1
- Tc607-1: Added `SHA-224` / `SHA-256` / `SHA-384` / `SHA-512`, `SHA3-*`, `Adler-32`, and various CRC types such as `CRC-32B`. Type names are now case-insensitive, and `-`, `_`, and `/` are ignored

## See Also

- STRDIGEST
