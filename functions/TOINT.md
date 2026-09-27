# TOINT
**Category:** 型取得/変換

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
- Tc574-4 / Tc602-6: 数字の後に `a`（`A`）が続く文字列で、`a` を 10 という桁として読んでしまい `TOINT('1a')` が 20 になっていたのを修正（1 になる）

## See Also
- TOSTR
- TOREAL
