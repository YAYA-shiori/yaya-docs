# TOHEXSTR
**Category:** 文字列操作

## Signature
```
TOHEXSTR( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 変換する整数値 |

## Returns
- 成功: 16進数値文字列
- 失敗: VOID

## Description
整数を16進数値文字列へ変換する。

## Example
```
_i = 30
_hex = TOHEXSTR( _i )
_hex // "1E" (10進数30 = 16進数1E)
```

## Compatibility
- YAYA: 初期バージョンより
- AYA: 5.8以降
- Tc602-5: 整数の最小値（-9223372036854775808）が `-` だけになっていたのを修正

## See Also
- TOBINSTR
- HEXSTRTOI
