# OnTranslate事件

> 转引自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## OnTranslate的用法

使用OnTranslate可以替换特定字符串。<br>
可以避免敬称重复（さん様、さま様等）的情况。<br>

（编写示例）

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
