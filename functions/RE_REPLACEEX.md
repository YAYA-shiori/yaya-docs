# RE_REPLACEEX
**Category:** 正規表現
**Source:** マニュアル/関数/RE_REPLACEEX

## Signature
```
RE_REPLACEEX( string , regexp , replace_ex [, count] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 処理対象の文字列（数値型変数は TOSTR で文字列型に変換することを推奨） |
| regexp | 正規表現パターン |
| replace_ex | 置換後の文字列（`$0`、`$1` 等のPerlスタイルメタ文字使用可能） |
| count | 置換回数（省略またはマイナス値で全置換） |

## Returns
- 成功: 置換後の文字列
- 失敗: 元の string（変更なし）

## Description
処理対象文字列内で正規表現にマッチした部分を置換します。RE_REPLACE との違いは、置換文字列に `$0`、`$1` などのPerlスタイルのメタ文字が使用できる点です。

RE_REPLACEEX を使用した場合、RE_GETSTR、RE_GETPOS、RE_GETLEN は、nグループのキャプチャではなく、正規表現パターン全体のn番目のマッチに関する情報を返します。

## Compatibility
- YAYA: 初期バージョンより対応（count パラメータは Tc548-1 以降）

## See Also
- REPLACE
- RE_REPLACE
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
