# OnTranslateイベント

**Source:** Tips/OnTranslateイベント

## 概要

`OnTranslate` イベントを使用すると、ゴーストが出力するすべての文字列を事後的に書き換えることができる。特に敬称の重複（「さん様」「さま様」など）を回避するのに役立つ。

## コード例

```
OnTranslate
{
　reference0 = REPLACE(reference0, "ちゃんさん", "ちゃん")
　reference0 = REPLACE(reference0, "くんさん", "くん")
　reference0 = REPLACE(reference0, "さんさん", "さん")
　reference0
}
```

## 説明

`reference0` にはゴーストが出力しようとしているスクリプトテキストが格納されている。`REPLACE` 関数を使って置換処理を順次実行し、最終的な文字列を出力する。

複数の `REPLACE` 呼び出しを連続して記述することで、複数のパターンを順番に処理できる。

## 関連項目

- Tips/OnTranslateの使い方
- マニュアル/関数/REPLACE
- マニュアル/関数/RE_REPLACE
