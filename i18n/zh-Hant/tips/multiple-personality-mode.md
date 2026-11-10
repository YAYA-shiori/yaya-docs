# 多重人格模式

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

假設以變數 mode 儲存模式，並有 0 和 1 兩種模式。<br>
隨機對話事件 OnAiTalk 可如下撰寫。

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

如此一來，就能像下面這樣依模式區分事件。<br>
其他各種事件也以同樣方式撰寫，再依模式整理辭典檔案即可。<br>

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

（摘自 et cetera. 的雜記）
