# STRDIGEST
**Category:** 文字列操作

## Signature
```
STRDIGEST(string [, type])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | ダイジェスト値を計算する対象の文字列 |
| type | ダイジェストの種類（[下表](#ダイジェストの種類)）。省略すると `MD5` |

## Returns
- 成功時: 計算されたダイジェスト値の16進数文字列（英大文字）
- 失敗時: -1

## Description
指定した文字列のダイジェスト（ハッシュ）値を計算して返します。文字列の文字コードは内部表現（Windows 版は UTF-16、POSIX 版は UTF-32）のバイト列が使用されます。たとえば `"abc"` は Windows 版では `61 00 62 00 63 00` の6バイトです。

`type` は大文字小文字を区別せず、`-` `_` `/` も無視します（`SHA-256` `sha_256` `sha256` はどれも同じ）。知らない種類を指定すると `MD5` として計算します。

### ダイジェストの種類

| type | 内容 | 長さ |
|------|------|------|
| `MD5` | MD5 | 16バイト |
| `SHA-1` / `SHA1` | SHA-1 | 20バイト |
| `SHA-224` / `SHA-256` / `SHA-384` / `SHA-512` | SHA-2 | 28 / 32 / 48 / 64バイト |
| `SHA3-224` / `SHA3-256` / `SHA3-384` / `SHA3-512` | SHA-3 | 28 / 32 / 48 / 64バイト |
| `Adler-32` | Adler-32（zlib） | 4バイト |
| `CRC-32` | CRC-32（ZIP・PNG などと同じ多項式）。**下位バイトから先に並べる**（下の注意を参照） | 4バイト |
| `CRC-32B`（`CRC-32/ISO-HDLC`） | `CRC-32` と同じ値を、一般的な表記（上位バイトから）で出す | 4バイト |
| `CRC-32C`（`CRC-32/CASTAGNOLI`） | CRC-32C（iSCSI・SCTP・ext4 など） | 4バイト |
| `CRC-32/BZIP2` | CRC-32/BZIP2 | 4バイト |
| `CRC-32/MPEG-2` | CRC-32/MPEG-2 | 4バイト |
| `CRC-32/JAMCRC`（`JAMCRC`） | CRC-32/JAMCRC | 4バイト |
| `CRC-16`（`CRC-16/ARC`） | CRC-16/ARC | 2バイト |
| `CRC-16/CCITT-FALSE`（`CRC-16/IBM-3740`） | CRC-16/CCITT-FALSE | 2バイト |
| `CRC-16/XMODEM`（`CRC-16/ZMODEM`） | CRC-16/XMODEM | 2バイト |
| `CRC-16/KERMIT`（`CRC-16/CCITT-TRUE`） | CRC-16/KERMIT | 2バイト |
| `CRC-16/MODBUS` | CRC-16/MODBUS | 2バイト |
| `CRC-16/X-25`（`CRC-16/IBM-SDLC`） | CRC-16/X-25 | 2バイト |
| `CRC-8`（`CRC-8/SMBUS`） | CRC-8 | 1バイト |
| `CRC-8/MAXIM`（`CRC-8/DOW`） | CRC-8/MAXIM（Dallas 1-Wire） | 1バイト |
| `CRC-64`（`CRC-64/XZ`） | CRC-64/XZ（xz・Go の ECMA 表） | 8バイト |
| `CRC-64/ECMA-182` | CRC-64/ECMA-182 | 8バイト |

CRC の各種類の名前と定義は、CRC のカタログ（Rocksoft モデルによる一覧）に合わせています。`CRC-16` と `CRC-64` は、それぞれ `CRC-16/ARC` と `CRC-64/XZ` のことです。

!!! note "CRC の並び順"
    `CRC-32` だけは、従来の互換のため値の下位バイトから先に並べます（`123456789` の CRC-32 は一般には `CBF43926` ですが、`2639F4CB` になります）。一般的な表記で受け取りたいときは `CRC-32B` を使ってください。それ以外の CRC は、カタログと同じ一般的な表記（上位バイトから）です。

    実装の確認に使える値は [FDIGEST](FDIGEST.md) にあります。

## Example
```
_h = STRDIGEST("abc", "SHA-256")    // 13E228567E8249FCE53337F25D7970DE3BD68AB2653424C7B8F9FD05E33CAEDF (Windows 版)
```

## Compatibility
- YAYA: Tc568-1以降
- Tc607-1: `SHA-224` / `SHA-256` / `SHA-384` / `SHA-512`、`SHA3-*`、`Adler-32` と、`CRC-32B` ほかの各種 CRC を追加。種類名の大文字小文字と `-` `_` `/` を無視するようにした

## See Also
- FDIGEST（ファイルのダイジェスト計算）
