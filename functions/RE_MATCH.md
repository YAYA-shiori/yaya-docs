# RE_MATCH
**Category:** 正規表現
**Source:** マニュアル/関数/RE_MATCH

## Signature
```
RE_MATCH( string , regexp )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | マッチ対象の文字列 |
| regexp | 正規表現パターン |

## Returns
- **1**: 文字列全体がパターンに完全マッチした場合
- **0**: マッチしなかった場合

## Description
処理対象文字列が正規表現に完全にマッチするかどうかを調べます。部分一致を調べる場合は RE_SEARCH を使用してください。

マッチした詳細は RE_GETSTR、RE_GETPOS、RE_GETLEN で取得できます。

## Example
```
RE_MATCH("50kg", "(\d+) *kg")
// → 1

RE_MATCH("50cm", "(\d+) *kg")
// → 0
```

## Compatibility
- YAYA: 初期バージョンより対応
- AYA: 5.8以降

## See Also
- RE_SEARCH
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
