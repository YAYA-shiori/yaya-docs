# ゴースト切替えメッセージを変化させる(新)

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

切換反応をつけるゴーストの数が増えてくると、どんどん見通しが悪くなってきます。<br>
そんな時はこちら。

**更新-20061023**：<http://acronotes.seesaa.net/article/25705192.html> の報告反映

### １）OnGhostChangingとOnGhostChangedを消して、これに入れ換え。

通常、aya_bootend.dicの後ろのほうにあります。<br>
ばっさり消してしまうのは不安だという人は、すでに存在する2つを

| 前 | 後 |
|---|---|
| OnGhostChanging | OnGhostChanging<span style="color:red">Other</span> |
| OnGhostChanged | OnGhostChanged<span style="color:red">Other</span> |

のように書きかえて、辞書のいちばん最後に下の囲みのすべてを貼りつけてください。

```
TranslateSystemChar
{
  _text = TOSTR(_argv[0])
  _text = RE_REPLACE(_text,"[ !%(CHR(0x22))%(CHR(0x25))#$&()*+,\-/:;<=>?@\[\]`{|}~]","_")
  _text
}

ExecuteChangeCallTalk
{
  _ghostname = TranslateSystemChar(reference0)
  
  _funcname = "%(_argv[0])_%(_ghostname)"
  if ISFUNC(_funcname) {
    _script = EVAL(_funcname)
    if STRLEN(_script) != 0 {
      _script
      return
    }
  }

  _funcname = "%(_argv[0])Other"
  if ISFUNC(_funcname) {
    _script = EVAL(_funcname)
    if STRLEN(_script) != 0 {
      _script
      return
    }
  }

  if _argc >= 2 {
    _script = EVAL(_argv[1])
    if STRLEN(_script) != 0 {
      REPLACE(_script,"\-","")
      return
    }
  }
}
 
OnGhostChanging
{
  ExecuteChangeCallTalk("OnGhostChanging","OnClose")
}

OnGhostChanged
{
  ExecuteChangeCallTalk("OnGhostChanged","OnBoot")
}

OnGhostCalling
{
  ExecuteChangeCallTalk("OnGhostCalling")
}

OnGhostCalled
{
  ExecuteChangeCallTalk("OnGhostCalled","OnBoot")
}

OnGhostCallComplete
{
  ExecuteChangeCallTalk("OnGhostCallComplete")
}

OnOtherGhostClosed
{
  ExecuteChangeCallTalk("OnOtherGhostClosed")
}
```

### ２）新たにゴースト専用の関数をつくる

```
OnGhostChanging_和音
{
  "ごにょごにょ"
}

OnGhostChanged_和音
{
  "ごにょごにょ"
}
```

| 書くべき名前 | 機能 |
|---|---|
| OnGhostChanging | 他のゴーストに切り替え |
| OnGhostChanged | 他のゴーストから切り替え |
| OnGhostCalling | 他のゴーストを呼び出し開始[SSP] |
| OnGhostCallComplete | 他のゴーストを呼び出し完了[SSP] |
| OnGhostCalled | 他のゴーストから呼び出された[SSP] |
| OnOtherGhostClosed | 他のゴーストが終了した[SSP] |

- OnGhostChanged<span style="color:red">_(Sakura側の名前)</span>　のようなものをつくってください。
  - 上の表の名前 ＋ "_"(アンダースコア) ＋ Sakura名
  - ゴースト名ではなくSakura名です。気をつけてください。

- 名前にスペースや+-などが含まれる特殊な場合は、すべて _ に置換されます。
  - 例：`+Emily+`  ==>  `OnGhostChanged__Emily_`
  - 例：`○|￣|_`  ==>  `OnGhostChanged_○_￣__`

- 該当するゴーストが辞書にない時は、OnGhostChangedOtherなどというように、Otherが後ろについたものを喋り、それもない場合は通常の起動・終了処理となります。

```
OnGhostChangingOther
OnGhostChangedOther
OnGhostCallingOther
OnGhostCalledOther
OnGhostCallCompleteOther
OnOtherGhostClosedOther
```

### サンプル

たとえば、[ゴースト切替えメッセージを変化させる](ghost-switch-message.md)の例を書き直すとこうなります。

```
OnGhostChanged_ゴーストA
{
  if "お料理" _in_ reference1 // （ここでキーワード「お料理」を指定）
  {
    "(文章1)"
  }
  elseif "薬" _in_ reference1 // （ここでキーワード「薬」を指定）
  {
    "(文章2)"
  }
  else // （キーワード「お料理」がなかったときの反応）
  {
    "(文章3)"
  }
}
```
