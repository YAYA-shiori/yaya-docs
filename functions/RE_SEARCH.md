# RE_SEARCH
**Category:** 正規表現
**Source:** マニュアル/関数/RE_SEARCH

## Signature
```
RE_SEARCH( string , regexp )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 検索対象の文字列 |
| regexp | 正規表現パターン |

## Returns
- **1**: マッチする部分が見つかった場合
- **0**: マッチしなかった場合

## Description
処理対象文字列内に正規表現とマッチする部分があるかどうかを調べます。文字列全体の完全マッチを調べる場合は RE_MATCH を使用してください。

マッチした詳細は RE_GETSTR、RE_GETPOS、RE_GETLEN で取得できます。

## Example
```
if (RE_SEARCH(reference[0], 'こんに?ち[はわ]|今日[はわ]')){
  "こんにちは、%(username)"
}
```

ユーザー入力に「こんにちは」や「こんにちわ」等が含まれていればあいさつを返す例。

## Compatibility
- YAYA: 初期バージョンより対応

## See Also
- RE_MATCH
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
