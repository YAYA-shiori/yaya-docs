# RE_ASEARCH
**Category:** 正規表現
**Source:** マニュアル/関数/RE_ASEARCH

## Signature
```
RE_ASEARCH(key, array)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key | 検索する正規表現パターン |
| array | 検索対象の汎用配列（単純配列はサポートされない） |

## Returns
- 最初にマッチした要素のインデックス（0始まり）
- マッチする要素がない場合: -1

## Description
汎用配列から、指定した正規表現に「一部でも」合致する値を検索し、最初に見つかったもののみを返します。

**注意:** `RE_GETSTR`・`RE_GETPOS`・`RE_GETLEN` は使用不可です。すべてのマッチを取得したい場合は `RE_ASEARCHEX` を使用してください。

## Example
```
_array = ('さくら','まゆら','ねここ')
RE_ASEARCH('^ま', _array) // Returns: 1
```
"ま"で始まる要素を検索し、インデックス1（2番目の要素）が見つかります。

## Compatibility
- YAYA: バージョンTc539-1から使用可能

## See Also
- ASEARCH
- RE_ASEARCHEX
