# RE_GETSTR
**Category:** 正規表現
**Source:** マニュアル/関数/RE_GETSTR

## Signature
```
RE_GETSTR
RE_GETSTR()
```

## Parameters
なし

## Returns
マッチした部分文字列を格納した汎用配列。

| 要素 | 内容 |
|------|------|
| 要素0 | 正規表現全体にマッチした文字列 |
| 要素n | n番目の括弧グループにマッチした部分文字列 |

- 正規表現関数を実行していない場合やマッチした文字列がない場合は `IARRAY` を返します。
- `RE_REPLACE`・`RE_REPLACEEX`・`RE_SPLIT` の場合は、個々のグループではなく正規表現全体にマッチした文字列を格納した配列を返します。

## Description
正規表現系関数の実行結果を取得します。

## Example
```
RE_MATCH("x > 15.7", "x *> *([\\d\\.]+)")
_array = RE_GETSTR
// _array は ("x > 15.7", "15.7") になる
```

## Compatibility
- YAYA: 初期リリースから使用可能
- AYA: バージョン5.8から使用可能

## See Also
- RE_GETPOS
- RE_GETLEN
