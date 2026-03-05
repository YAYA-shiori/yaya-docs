# HEXSTRTOI
**Category:** 文字列操作
**Source:** マニュアル/関数/HEXSTRTOI

## Signature
```
HEXSTRTOI( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 変換対象の16進数値文字列 |

## Returns
- 成功時: 変換後の数値（整数）
- 失敗時: 0

## Description
16進数値文字列を整数へ変換する。先頭に `0x` プレフィックスがある場合は無視する。

## Example
```
_hex = '1E'
_i = HEXSTRTOI( _hex )
// _i は 30（16進数 1E = 10進数 30）
```

## Compatibility
- YAYA: 初期から利用可能
  - Tc547-1以降: 先頭の `0x` プレフィックスを処理可能
- AYA: 5.8以降

## See Also
- BINSTRTOI
- TOHEXSTR
