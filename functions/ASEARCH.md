# ASEARCH

**Category:** 配列操作

## Signature

```
ASEARCH(key, array)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| key | 検索するキー値（文字列） |
| array | 汎用配列（簡易配列は使用不可） |

## Returns

成功時：最初に見つかった要素の順序番号（0始まり）
見つからない場合：-1

## Description

`key` と各要素を `==` と同じ規則で比べ、最初に一致した要素の位置を返す。

Tc600-3以降では、次の点が変わった。

- 要素がハッシュのときは内容で比べる（`key` にハッシュを渡すと、同じ内容のハッシュの要素が見つかる）
- `key` と要素が両方とも VOID のときも一致とみなす（それまでは -1 だった）

## Example

```
_array = ('さくら','まゆら','ねここ')
ASEARCH('まゆら', _array)  // 1 を出力
```

## Compatibility

- YAYA: 初期リリースから利用可能
- AYA: バージョン 5.8 以降
- Tc600-3: ハッシュの要素を内容で比べるようにした。VOID 同士を一致とみなすようにした

## See Also

- ASEARCHEX
- RE_ASEARCH
