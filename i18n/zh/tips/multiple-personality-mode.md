# 多重人格模式

> 转引自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

假设模式由变量 mode 保存，且有 0 和 1 两种模式。<br>
随机对话事件 OnAiTalk 按以下方式编写。

版本5

```
OnAiTalk
{
　EVAL("OnAiTalk%mode")
}
```

版本4

```
OnAiTalk
{
　CALLBYNAME("OnAiTalk%mode")
}
```

这样就可以像下面这样按模式拆分事件。<br>
其他各种事件也以同样方式编写，再按模式整理词典文件即可。<br>

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

（摘自(et cetera. 的杂记）
