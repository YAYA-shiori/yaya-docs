# RE_GETPOS
**Category:** 正規表現
**Source:** マニュアル/関数/RE_GETPOS

## Signature
```
RE_GETPOS
RE_GETPOS()
```

## Parameters
なし

## Returns
正規表現内の `( )` にマッチした位置を列挙した汎用配列。

| 要素 | 内容 |
|------|------|
| 要素0 | 正規表現パターン全体がマッチした位置 |
| 要素n | n番目の括弧グループがマッチした位置 |

- 位置は先頭からの文字数（0始まり）で表されます。
- 正規表現関数を実行していない場合、またはマッチする文字列がない場合は `IARRAY` を返します。
- `RE_REPLACE`・`RE_REPLACEEX`・`RE_SPLIT` の場合は、個々のグループではなく正規表現全体のマッチ位置を返します。

## Description
正規表現系関数の実行結果（マッチ位置情報）を取得します。

## Compatibility
- YAYA: 初期リリースから使用可能
- AYA: バージョン5.8以降で使用可能

## See Also
- RE_GETSTR
- RE_GETLEN
