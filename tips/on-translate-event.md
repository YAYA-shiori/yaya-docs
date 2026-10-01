# OnTranslateイベント

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

## OnTranslateの使い方

OnTranslateを使うと、特定の文字列を書き換えることができます。<br>
敬称の重なり（さん様、さま様etc.）などを回避することが出来ます。<br>

(記述例)

```
OnTranslate
{
　// 順次変換して、結果を次へ渡していく
　reference0 = REPLACE(reference0, "ちゃんさん", "ちゃん")
　reference0 = REPLACE(reference0, "くんさん", "くん")
　reference0 = REPLACE(reference0, "さんさん", "さん")
　// 最終結果のみ出力
　reference0
}
```
