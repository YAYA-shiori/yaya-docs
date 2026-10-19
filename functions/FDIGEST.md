# FDIGEST

**Category:** ファイル操作

## Signature

```
FDIGEST(path [, type])
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | ダイジェスト値を計算するファイルのパス。フルパス指定可。相対パスはDLLのロード位置を基準とする |
| type | ダイジェストの種類。MD5・SHA-1・SHA-2・SHA-3・Adler-32・各種 CRC。一覧は [STRDIGEST](STRDIGEST.md#ダイジェストの種類) を参照。省略すると `MD5` |

## Returns

- 成功時: ダイジェスト値を16進数文字列（英大文字）で返す
- 失敗時（ファイルが存在しない・値の生成に失敗した場合）: -1

## Description

指定したファイルのダイジェスト（ハッシュ）値を得る。パスはフルパスで指定できる。相対パスの場合は DLL load で渡された位置（多くの場合、DLL のある位置）が基準になる。

`type` の書き方と、`CRC-32` だけ値の下位バイトから先に並ぶ点は [STRDIGEST](STRDIGEST.md) と同じ。文字列の内部表現ではなくファイルの中身のバイト列をそのまま計算するので、他のツールの結果と照らし合わせられる。

### 確認用の値

`123456789`（9バイト、改行なし）だけを書いたファイルの値。

| type | 値 |
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

- YAYA: Tc527-1 で初回リリース。Tc530-1 で CRC32 サポートを追加
- Tc607-1: `SHA-224` / `SHA-256` / `SHA-384` / `SHA-512`、`SHA3-*`、`Adler-32` と、`CRC-32B` ほかの各種 CRC を追加。種類名の大文字小文字と `-` `_` `/` を無視するようにした

## See Also

- STRDIGEST
