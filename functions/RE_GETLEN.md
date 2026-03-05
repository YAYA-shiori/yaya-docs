# RE_GETLEN
**Category:** 正規表現
**Source:** マニュアル/関数/RE_GETLEN

## Signature
```
RE_GETLEN
RE_GETLEN()
```

## Parameters
なし

## Returns
正規表現内の `( )` にマッチした部分の長さを列挙した汎用配列。

| 要素 | 内容 |
|------|------|
| 要素0 | 正規表現全体にマッチした部分の長さ |
| 要素n | n番目の括弧グループにマッチした部分の長さ |

- 長さは文字数で計測されます。
- 正規表現関数を実行していない場合、またはマッチした文字列がない場合は `IARRAY` を返します。
- `RE_REPLACE`・`RE_REPLACEEX`・`RE_SPLIT` の場合は、個々のグループではなく正規表現全体にマッチした部分の長さを返します。

## Description
正規表現系関数の実行結果を取得します。`RE_GETPOS`・`RE_GETSTR` と組み合わせて使用します。

## Compatibility
- YAYA: 初期リリースから使用可能
- AYA: バージョン5.8以降で使用可能

## See Also
- RE_GETPOS
- RE_GETSTR
