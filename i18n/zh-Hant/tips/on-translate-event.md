# OnTranslate 事件

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## OnTranslate 的用法

使用OnTranslate可以改寫特定字串。<br>
這可以避免敬稱重複（例如「さん様」、「さま様」等）。<br>

（撰寫範例）

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
