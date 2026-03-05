# ASEARCH

**Category:** 配列操作
**Source:** マニュアル/関数/ASEARCH

## Signature

```
ASEARCH(key, array)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| key | 検索するキー値（文字列） |
| array | 汎用配列（単純配列は使用不可） |

## Returns

成功時：最初に見つかった要素の順序番号（0始まり）
見つからない場合：-1

## Example

```
_array = ('さくら','まゆら','ねここ')
ASEARCH('まゆら', _array)  // 1 を出力
```

## Compatibility

- YAYA: 初期リリースから利用可能
- AYA: バージョン 5.8 以降

## See Also

- ASEARCHEX
- RE_ASEARCH
