# RE_REPLACE
**Category:** 正規表現
**Source:** マニュアル/関数/RE_REPLACE

## Signature
```
RE_REPLACE( string , regexp , replace [, count] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 処理対象の文字列（数値型変数は TOSTR で文字列型に変換することを推奨） |
| regexp | 正規表現パターン |
| replace | 置換後の文字列（メタ文字は使用不可） |
| count | 置換回数（省略またはマイナス値で全置換） |

## Returns
- 成功: 置換後の文字列
- マッチなし: 元の文字列（変更なし）

## Description
処理対象文字列内で正規表現にマッチした部分を置換します。置換文字列にメタ文字は利用できません。メタ文字を使用したい場合は RE_REPLACEEX を使用してください。

マッチした詳細は RE_GETSTR、RE_GETPOS、RE_GETLEN で取得できます。

## Compatibility
- YAYA: 初期バージョンより対応（count パラメータは Tc548-1 以降）
- AYA: 5.8以降

## See Also
- REPLACE
- RE_REPLACEEX
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
