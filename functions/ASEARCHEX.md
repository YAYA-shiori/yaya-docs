# ASEARCHEX

**Category:** 配列操作

## Signature

```
ASEARCHEX(key, array)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| key | 検索対象の文字列値 |
| array | 汎用配列（簡易配列は使用不可） |

## Returns

一致するすべての要素の順序番号（0始まり）を格納した汎用配列を返す。一致する要素がない場合は空の配列を返す。

## Description

汎用配列から、値が一致する要素をすべて検索する。

## Example

```
_tea = ("鉄観音", "烏龍", "やぶきた", "烏龍", "ジャスミン")
ipod = ASEARCHEX("烏龍", _tea)
// ipod には (1,3) という汎用配列が格納される
```

## Compatibility

- YAYA: 初期リリースから利用可能
- AYA: バージョン 5.8 以降

## See Also

- ASEARCH
- RE_ASEARCHEX
