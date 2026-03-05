# TOINT
**Category:** 型取得/変換
**Source:** マニュアル/関数/TOINT

## Signature
```
TOINT( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 変換したい文字列または実数 |

## Returns
- 成功: 変換後の整数値
- 失敗: 0

## Description
文字列・実数を整数に変換する。小数点以下は単純に切り捨てられる。

Tc542-4以前のバージョンではFLOOR()相当の動作（バグ）があったが、Tc542-4以降では他言語と同様に小数点以下を単純に切り捨てる動作となった。

## Example
```
_i = '100'
_j = TOINT( _i ) + 1
// 101 (文字列連結ではなく整数加算)

_i = 1.1
_j = TOINT( _i )
// 1

_i = -1.1
_j = TOINT( _i )
// -1 (Tc542-4以降の動作)
```

## Compatibility
- YAYA: 初期バージョンより
- AYA: 5.8以降
- Tc542-4以降: 負の小数の切り捨て動作変更

## See Also
- TOSTR
- TOREAL
