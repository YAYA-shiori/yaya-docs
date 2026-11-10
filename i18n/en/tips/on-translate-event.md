# OnTranslate Event

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## How to Use OnTranslate

You can use OnTranslate to replace specific strings.<br>
This can be used to avoid duplicate honorifics (such as "さん様" or "さま様").<br>

(Example)

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
