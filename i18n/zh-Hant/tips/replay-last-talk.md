# 再次播放上一段對話

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

『文』沒有再次播放上一段對話的功能。本文旨在透過指令碼實現這項功能。播放對話時，baseware 會呼叫 AI 的『OnAiTalk』，而我們主要會修改這個 OnAiTalk 函式。

### 修改 OnAiTalk

初始狀態的 OnAiTalk 函式大致如下。

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

『文』會從 OnAiTalk 函式呼叫 RandomTalk 函式來實現隨機對話，因此，只要**取得 RandomTalk 函式的傳回值，並將該傳回值作為對話播放**，就能記住上一段對話。修改後的 OnAiTalk 函式如下。

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

「//ここ！」是修改的地方。

### 修改選單相關部分

只儲存變數還無法實現播放功能，因此接著要修改選單。

『文』負責顯示選單的『OpenMenu』函式，基本上如下所示。

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

首先，將它修改如下。

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

### 建立『OnLastTalk』函式

新建的 OnLastTalk 函式如下。

```
OnLastTalk {
  "\0\s[0]えっと\w2‥\w2‥\w2‥\w9\w9\w9\c/
  %lastTalk"
}
```

如此一來，選取選單中的『さっきなんて言ったの？』時，就會呼叫 OnLastTalk 函式，並再次播放上一段對話。

將這個做法延伸應用，例如把 lastTalk 改成簡易陣列，就能編寫出再次播放前 N 段對話的指令碼。
