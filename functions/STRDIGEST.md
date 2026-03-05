# STRDIGEST
**Category:** 文字列操作
**Source:** マニュアル/関数/STRDIGEST

## Signature
```
STRDIGEST(string, type)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | ダイジェスト値を計算する対象の文字列 |
| type | ハッシュアルゴリズム。`CRC32`（32ビットCRC）、`MD5`、`SHA-1` または `SHA1` を指定 |

## Returns
- 成功時: 計算されたダイジェスト値の16進数文字列
- 失敗時: -1

## Description
指定した文字列のダイジェスト（ハッシュ）値を計算して返します。文字列の文字コードは内部表現（UTF-16）が使用されます。

## Compatibility
- YAYA: Tc568-1以降

## See Also
- FDIGEST（ファイルのダイジェスト計算）
