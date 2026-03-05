# TOSTR
**Category:** 型取得/変換
**Source:** マニュアル/関数/TOSTR

## Signature
```
TOSTR( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 変換する整数、実数、または一般配列 |

## Returns
- 成功: 変換後の文字列
- 失敗: VOID

## Description
整数・実数・一般配列を文字列に変換する。一般配列を渡した場合は、要素をカンマで結合した文字列を返す。

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

## See Also
- TOINT
- TOREAL
