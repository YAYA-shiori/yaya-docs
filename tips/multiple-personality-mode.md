# 多重人格モード

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

モードは変数 mode で持ち、0 と 1 のモードがあるとします。<br>
ランダムトークイベント OnAiTalk は以下のように記述します。

Version5

```
OnAiTalk
{
　EVAL("OnAiTalk%mode")
}
```

Version4

```
OnAiTalk
{
　CALLBYNAME("OnAiTalk%mode")
}
```

これで以下のようにモード毎にイベントを分けられます。<br>
他の各種イベントも同様に記述し、モード別に辞書ファイルをまとめれば出来上がりです。<br>

```
OnAiTalk0
{
　// モード 0
　"\0ユーザーさん大好きっ。\e"
}

OnAiTalk1
{
　// モード 1
　"\0くたばれ腐れユーザーさん。\e"
}
```

(et cetera. の雑記内より)
