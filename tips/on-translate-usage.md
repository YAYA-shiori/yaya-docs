# OnTranslateの使い方

**Source:** Tips/OnTranslateの使い方

## 概要

`OnTranslate` は、ゴーストがしゃべるスクリプトをまとめて後処理で置き換える際に使うイベント。語尾の変更や敬称の重複回避に有用。

## 基本実装例

```
OnTranslate
{
   _text = reference0

   _text = REPLACE(_text, "、", "、\w5")
   _text = REPLACE(_text, "。", "。\w5")
   _text = REPLACE(_text, "…", "…\w5")

   _text = REPLACE(_text, "たん殿", "たん")
   _text = RE_REPLACE(_text,"(ちゃん|くん|さん|殿)殿","殿")

   _text
}
```

## 説明

### 置換の仕組み

`REPLACE(_text, "置換前", "置換後")` でテキストを変換する。上記例では句読点の後に自動ウエイト `\w5` を挿入している。

### 正規表現の活用

`RE_REPLACE` を使えば複数パターンを一括処理できる。括弧と `|` で複数の選択肢を指定できる：

```
RE_REPLACE(_text, "(ちゃん|くん|さん|殿)殿", "殿")
```

これにより「ちゃん殿」「くん殿」「さん殿」「殿殿」をまとめて「殿」に変換する。

### TextOnlyTranslator

タグ内部を誤って置換しないよう、テキスト部分のみを処理する `TextOnlyTranslator` 関数の実装も紹介されている。

## 関連項目

- Tips/OnTranslateイベント
- マニュアル/関数/REPLACE
- マニュアル/関数/RE_REPLACE
