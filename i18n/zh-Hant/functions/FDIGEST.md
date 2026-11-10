# FDIGEST

**Category:** ファイル操作

## Signature

```
FDIGEST(path [, type])
```

## Parameters

| 引數 | 說明 |
|-----------|-------------|
| path | 要計算摘要值的檔案路徑。可指定完整路徑。相對路徑以 DLL 載入位置為基準 |
| type | 摘要種類。MD5、SHA-1、SHA-2、SHA-3、Adler-32、各種 CRC。清單請參閱 [STRDIGEST](STRDIGEST.md#ダイジェストの種類)。省略時為 `MD5` |

## Returns

- 成功時：以十六進位字串（英文字母大寫）傳回摘要值
- 失敗時（檔案不存在或無法產生值）：-1

## Description

取得指定檔案的摘要（雜湊）值。路徑可指定完整路徑。若為相對路徑，則以 DLL 載入時傳入的位置（通常是 DLL 所在位置）為基準。

`type` 的寫法，以及只有 `CRC-32` 會從值的低位元組開始排列的特性，都與 [STRDIGEST](STRDIGEST.md) 相同。計算時會直接使用檔案內容的位元組序列，而非字串的內部表示，因此可以與其他工具的結果比對。

### 確認用的值

僅含有 `123456789`（9 個位元組、不含換行）的檔案所產生的值。

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

- YAYA: Tc527-1 首次釋出。Tc530-1 新增 CRC32 支援
- Tc607-1: 新增 `SHA-224` / `SHA-256` / `SHA-384` / `SHA-512`、`SHA3-*`、`Adler-32` 及 `CRC-32B` 等各種 CRC。並改為忽略種類名稱中的大小寫，以及 `-` `_` `/`

## See Also

- STRDIGEST
