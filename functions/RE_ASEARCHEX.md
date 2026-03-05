# RE_ASEARCHEX
**Category:** 正規表現
**Source:** マニュアル/関数/RE_ASEARCHEX

## Signature
```
RE_ASEARCHEX( key , array )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key | 検索する正規表現パターン |
| array | 検索対象の汎用配列（単純配列はサポートされない） |

## Returns
マッチした要素の序数を列挙した汎用配列（0始まり）。マッチする要素がない場合は空の配列を返す。

**注意:** `RE_GETSTR`・`RE_GETPOS`・`RE_GETLEN` は使用不可です。

## Description
汎用配列から、指定した正規表現に「一部でも」合致する値を**すべて**検索します。

## Example
```
_tea = ("鉄観音", "烏龍", "やぶきた", "烏龍", "ジャスミン")
ipod = RE_ASEARCHEX("^烏", _tea)
// ipod は (1,3) になる（"烏"で始まる要素のインデックス）
```

## Compatibility
- YAYA: 初期リリースから使用可能
- AYA: バージョン5.8以降で使用可能

## See Also
- ASEARCHEX
- RE_ASEARCH
