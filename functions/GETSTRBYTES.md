# GETSTRBYTES
**Category:** 文字列操作

## Signature
```
GETSTRBYTES( string [ , code ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | バイト数を計算する対象の文字列 |
| code | 文字コードID（省略時は0）、または文字コードの名前（[文字コードの名前](../grammar/11-character-encoding.md#文字コードの名前)）。エンコードを指定してバイト数を計算する。知らない名前なら警告 W0012 を出して 0 を返す |

## Returns
- 成功時: 文字列を格納するのに必要なバイト数（整数）
- 失敗時: 0

## Description
「文字列を格納するのに必要なバイト数」を計算する関数。文字エンコードごとのメモリ使用量を調べることができる。

## Compatibility
- YAYA: 初期から利用可能
- AYA: 5.8以降
- Tc574-8 / Tc603-1: 知らない文字コードの名前を渡すと、警告 W0012 を出して0 を返すようにした（それまでは警告を出さずに OS デフォルトとして扱っていた）

## See Also
- GETSETTING
- GETSYSTEMFUNCLIST
