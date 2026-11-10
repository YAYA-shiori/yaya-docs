# 再次播放刚才的对话

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

『文』没有再次播放刚才对话的功能。本文旨在通过脚本实现这一功能。播放对话时，baseware 会调用 AI 的『OnAiTalk』，本文主要对 OnAiTalk 函数进行改造。

### 改造 OnAiTalk

初始状态下的 OnAiTalk 函数大致具有以下结构。

**aya_aitalk.dic**

```
//---- OnAiTalkイベント --------------------------------
OnAiTalk
{
  if RAND(100) < communicateratio
  {
    //---- communicateratio % の率で他ゴーストへ話しかけ
    StartCommunicate
  }
  else
  {
    if mikireflag == 0
    {
      //---- 通常のランダムトーク、ただしチェイン中はチェイントーク
      if CHAIN.IDName == "" {
        RandomTalk
      }
      else {
        ChainTalk
      }
    }
    else
    {
      //---- 見切れ中なので見切れ中のトークを行う
      MikireTalk
    }
  }
}
```

『文』通过 OnAiTalk 函数调用 RandomTalk 函数来实现随机对话，因此，只要**获取 RandomTalk 函数的返回值，并将其作为对话播放**，就可以记住刚才的对话。改造后的 OnAiTalk 函数如下所示。

```
//---- OnAiTalkイベント --------------------------------
OnAiTalk
{
  if RAND(100) < communicateratio
  {
    //---- communicateratio % の率で他ゴーストへ話しかけ
    StartCommunicate
  }
  else
  {
    if mikireflag == 0
    {
      //---- 通常のランダムトーク、ただしチェイン中はチェイントーク
      if CHAIN.IDName == "" {
        lastTalk = RandomTalk //ここ！
      }
      else {
        lastTalk = ChainTalk //ここ！
      }
      lastTalk //ここ！
    }
    else
    {
      //---- 見切れ中なので見切れ中のトークを行う
      MikireTalk
    }
  }
}
```

「//ここ！」是修改过的地方。

### 改造菜单相关内容

仅保存变量还无法实现再次播放功能，因此接下来要改造菜单。

『文』中用于显示菜单的 OpenMenu 函数，基本上如下所示。

**aya_menu.dic**

```
//---- メインメニュー展開 ------------------------
OpenMenu
{
   "\0\s[0]"
   --
   "はい、なんでしょうか？"
   "%username、なんですか？"
   "ん‥‥どうしたの？"
   --
   "\n\n/
   \q[なんか話して,AITALK]\n/
   \q[しゃべり頻度を変えて,TALKINTERVAL]\n/
   \q[コミュニケート,COMMUNICATEOPEN]\n/
   \q[AIについて,ABOUTAYA]\n/
   \q[なんでもない,CANCEL]\e"
}
```

首先，将其修改如下。

```
//---- メインメニュー展開 ------------------------
OpenMenu
{
   "\0\s[0]"
   --
   "はい、なんでしょうか？"
   "%username、なんですか？"
   "ん‥‥どうしたの？"
   --
   "\n\n" //ここから
   --
   if lastTalk != "" {
     "\q[さっきなんて言ったの？,OnLastTalk]\n"
   }
   --  //ここまで
   "\q[なんか話して,AITALK]\n/
   \q[しゃべり頻度を変えて,TALKINTERVAL]\n/
   \q[コミュニケート,COMMUNICATEOPEN]\n/
   \q[AIについて,ABOUTAYA]\n/
   \q[なんでもない,CANCEL]\e"
}
```

### 创建『OnLastTalk』函数

新建的 OnLastTalk 函数如下所示。

```
OnLastTalk {
  "\0\s[0]えっと\w2‥\w2‥\w2‥\w9\w9\w9\c/
  %lastTalk"
}
```

这样，选择菜单中的『刚才你说了什么？』后，就会调用 OnLastTalk 函数并再次播放刚才的对话。

以此为基础，例如将 lastTalk 改为简单数组等，还可以编写出再次播放前 N 次对话的脚本。
