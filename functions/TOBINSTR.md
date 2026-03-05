# TOBINSTR
**Category:** 文字列操作
**Source:** マニュアル/関数/TOBINSTR

## Signature
```
TOBINSTR( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 変換する整数値 |

## Returns
- 成功: 2進数値文字列
- 失敗: VOID

## Description
整数を2進数値文字列へ変換する。

## Example
```
_i = 30
_bin = TOBINSTR( _i )
_bin // "11110" (10進数30 = 2進数11110)
```

## Compatibility
- YAYA: 初期バージョンより
- AYA: 5.8以降

## See Also
- TOHEXSTR
- BINSTRTOI
