# RE_SPLIT
**Category:** 正規表現
**Source:** マニュアル/関数/RE_SPLIT

## Signature
```
RE_SPLIT( string , regexp [, max] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 分割対象の文字列 |
| regexp | 分割に使用する正規表現パターン |
| max | 最大分割数（省略または0で全分割） |

## Returns
- 成功: 分割された文字列を格納した汎用配列
- 失敗: 空の汎用配列

## Description
処理対象文字列を正規表現パターンで分割し、結果を汎用配列として返します。

分割結果の詳細は RE_GETSTR、RE_GETPOS、RE_GETLEN で取得できます。

## Compatibility
- YAYA: 初期バージョンより対応（max パラメータは Tc536-1 以降）

## See Also
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
