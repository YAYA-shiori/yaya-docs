# 變更人格切換訊息（新）

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

隨著新增切換反應的人格越來越多，內容也會變得越來越難以掌握。<br>
遇到這種情況時，請參考這裡。

**更新-20061023**：反映 <http://acronotes.seesaa.net/article/25705192.html> 中的回報

### １）刪除 OnGhostChanging 和 OnGhostChanged，並以以下內容取代。

這兩個事件通常位於 aya_bootend.dic 的後半部。<br>
如果擔心直接刪除，也可以將已存在的兩個名稱

| 前 | 後 |
|---|---|
| OnGhostChanging | OnGhostChanging<span style="color:red">Other</span> |
| OnGhostChanged | OnGhostChanged<span style="color:red">Other</span> |

改寫成如下形式，然後將下方框內的所有內容貼到辭典的最末尾。

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

### ２）新增人格專用函式

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

| 應使用的名稱 | 功能 |
|---|---|
| OnGhostChanging | 切換至其他人格 |
| OnGhostChanged | 從其他人格切換過來 |
| OnGhostCalling | 開始呼叫其他人格[SSP] |
| OnGhostCallComplete | 完成呼叫其他人格[SSP] |
| OnGhostCalled | 被其他人格呼叫[SSP] |
| OnOtherGhostClosed | 其他人格已結束[SSP] |

- 請建立類似 OnGhostChanged<span style="color:red">_(Sakura 側的名稱)</span> 的函式。
  - 表格中的名稱 ＋ "_"（底線）＋ Sakura 名稱
  - 這裡使用的不是人格名稱，而是 Sakura 名稱，請注意。

- 如果名稱中包含空格或 +- 等特殊字元，全部都會替換成 _。
  - 範例：`+Emily+`  ==>  `OnGhostChanged__Emily_`
  - 範例：`○|￣|_`  ==>  `OnGhostChanged_○_￣__`

- 如果辭典中沒有符合的人格，就會執行名稱後面加上 Other 的函式，例如 OnGhostChangedOther；如果也沒有這個函式，則會執行一般的啟動、結束處理。

```
OnGhostChangingOther
OnGhostChangedOther
OnGhostCallingOther
OnGhostCalledOther
OnGhostCallCompleteOther
OnOtherGhostClosedOther
```

### 範例

例如，將[變更人格切換訊息](ghost-switch-message.md)中的範例改寫如下。

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
