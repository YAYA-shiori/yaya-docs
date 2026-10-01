# 直前の会話をもう一度再生する

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

『文』には直前の会話を再生する機能がありません。これをスクリプト側で実現するのが本稿の趣旨です。会話の再生時には、ベースウェアからAIの『OnAiTalk』が呼ばれますが、主にこのOnAiTalk関数に細工します。

### OnAiTalkを改造する

初期状態のOnAiTalk関数は、だいたい以下のような構造をしています。

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

『文』では、ランダムトークを実現するためにOnAiTalk関数からRandomTalk関数を呼び出していますので、**RandomTalk関数の戻り値を取得して、その戻り値を会話として再生するように**すれば、直前の会話を記憶しておくことが出来ます。改造したOnAiTalk関数は以下のようになります。

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

「//ここ！」が変更した場所です。

### メニュー周りの改造

変数を保存するだけでは再生機能が実現できないので、次にメニューを改造します。

『文』でのメニュー表示を行う『OpenMenu』関数は、基本的に以下のようになっています。

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

まず、これを以下のように変更します。

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

### 『OnLastTalk』関数を作る

新たに作るOnLastTalk関数は以下のようにします。

```
OnLastTalk {
  "\0\s[0]えっと\w2‥\w2‥\w2‥\w9\w9\w9\c/
  %lastTalk"
}
```

これで、メニュー『さっきなんて言ったの？』を選択すると、OnLastTalk関数が呼ばれ、直前の会話が再生されるようになります。

これを応用して、lastTalkを簡易配列にするなどの変更を行えば、N個前の会話を再生するようなスクリプトも組めると思います。
