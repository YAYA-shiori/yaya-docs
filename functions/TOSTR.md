# TOSTR
**Category:** 型取得/変換

## Signature
```
TOSTR( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 変換する整数、実数、または汎用配列 |

## Returns
- 成功: 変換後の文字列
- 失敗: VOID

## Description
整数・実数・汎用配列を文字列に変換する。汎用配列を渡した場合は、要素をカンマで結合した文字列を返す。

## Example
```
_i = 100
_result = TOSTR( _i )
// "100"

_array = ('さくら','ねここ','まゆら')
_result = TOSTR( _array )
// "さくら,ねここ,まゆら"
```

## Compatibility
- YAYA: 初期バージョンより
- AYA: 5.8以降
- Tc574-4 / Tc602-5: 整数の最小値（-9223372036854775808）が `-` だけになっていたのを修正
- Tc574-4 / Tc601-1: 1e57 以上の実数を文字列にすると、末尾にゴミが混ざることがあったのを修正

## See Also
- TOINT
- TOREAL
