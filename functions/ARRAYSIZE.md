# ARRAYSIZE

**Category:** 配列操作

## Signature

```
ARRAYSIZE(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 簡易配列（文字列）または汎用配列 |

## Returns

成功時：要素数
失敗時：0

## Description

簡易配列、もしくは汎用配列の要素数を返す。

## Example

```
_array = ('さくら','まゆら','ねここ') // 汎用配列を代入
ARRAYSIZE( _array ) // 要素数「3」を出力
```

## Compatibility

- YAYA: 初期リリースから利用可能
- AYA: バージョン 5.8 以降

## See Also

- ARRAYDEDUP
- ASEARCH
