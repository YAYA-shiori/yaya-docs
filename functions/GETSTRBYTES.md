# GETSTRBYTES
**Category:** 文字列操作
**Source:** マニュアル/関数/GETSTRBYTES

## Signature
```
GETSTRBYTES( string [ , code ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | バイト数を計算する対象の文字列 |
| code | 文字コードID（省略時は0）。エンコードを指定してバイト数を計算する |

## Returns
- 成功時: 文字列を格納するのに必要なバイト数（整数）
- 失敗時: 0

## Description
「文字列を格納するのに必要なバイト数」を計算する関数。文字エンコードごとのメモリ使用量を調べることができる。

## Compatibility
- YAYA: 初期から利用可能
- AYA: 5.8以降

## See Also
- GETSETTING
- GETSYSTEMFUNCLIST
