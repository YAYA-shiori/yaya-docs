# RE_GREP
**Category:** 正規表現
**Source:** マニュアル/関数/RE_GREP

## Signature
```
RE_GREP( string , regexp )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 処理対象の文字列 |
| regexp | マッチさせる正規表現パターン |

## Returns
- 1以上: マッチした部分の数（マッチした場合）
- 0: マッチする部分がなかった場合

## Description
対象文字列の中から正規表現にマッチするすべての部分を検索します。詳細な結果は `RE_GETSTR`・`RE_GETPOS`・`RE_GETLEN` を使って取得できます。

## Compatibility
- YAYA: 初期リリースから使用可能
- AYA: バージョン5.8以降で使用可能

## See Also
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
