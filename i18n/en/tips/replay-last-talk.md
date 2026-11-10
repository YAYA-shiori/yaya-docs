# Replay the Previous Conversation

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

The Fumi ghost does not have a feature for replaying the previous conversation. This article explains how to implement one in a script. When a conversation is replayed, the baseware calls the AI event OnAiTalk. This article mainly modifies the OnAiTalk function.

### Modifying OnAiTalk

The OnAiTalk function in its initial state has roughly the following structure.

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

In Fumi, the OnAiTalk function calls the RandomTalk function to produce random talk. Therefore, you can remember the previous conversation by **getting the return value of the RandomTalk function and playing that return value as the conversation**. The modified OnAiTalk function looks like this.

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

The lines marked “//ここ！” are the changes.

### Modifying the Menu

Saving a variable alone is not enough to implement replay, so next, modify the menu.

The OpenMenu function, which displays the menu in Fumi, basically looks like this.

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

First, change it as follows.

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

### Creating the OnLastTalk Function

Create the new OnLastTalk function as follows.

```
OnLastTalk {
  "\0\s[0]えっと\w2‥\w2‥\w2‥\w9\w9\w9\c/
  %lastTalk"
}
```

Now, when you select “What did you just say?” from the menu, the OnLastTalk function is called and the previous conversation is replayed.

You can also adapt this approach to create a script that replays one of the previous N conversations, for example by changing lastTalk into a simple array.
