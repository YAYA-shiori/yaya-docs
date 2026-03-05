# TOREAL
**Category:** 型取得/変換
**Source:** マニュアル/関数/TOREAL

## Signature
```
TOREAL( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 変換したい文字列または整数 |

## Returns
- 成功: 変換後の実数値
- 失敗: 0.0

## Description
文字列または整数を実数（浮動小数点数）に変換する。

## Example
```
_s = '1.00005'
_d = TOREAL( _s )
_d // 1.000050 (実数)

_i = 1
_d = TOREAL( _i )
_d // 1.000000 (実数)
```

## Compatibility
- YAYA: 初期バージョンより
- AYA: 5.8以降

## See Also
- TOINT
- TOSTR
