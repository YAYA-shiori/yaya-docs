# 更改人格切换消息（新）

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

随着添加切换反应的人格越来越多，代码会变得越来越难以查看。<br>
这种时候可以使用下面的方法。

**更新-20061023**：已反映 <http://acronotes.seesaa.net/article/25705192.html> 中的报告

### １）删除 OnGhostChanging 和 OnGhostChanged，并替换为以下内容。

通常它们位于 aya_bootend.dic 的后半部分。<br>
如果不放心直接删除，可以把已有的两个函数

| 原名 | 修改后 |
|---|---|
| OnGhostChanging | OnGhostChanging<span style="color:red">Other</span> |
| OnGhostChanged | OnGhostChanged<span style="color:red">Other</span> |

改成这样，然后将下面代码框中的全部内容粘贴到词典末尾。

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

### ２）新建人格专用函数

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

| 要写的名称 | 功能 |
|---|---|
| OnGhostChanging | 切换到其他人格 |
| OnGhostChanged | 从其他人格切换而来 |
| OnGhostCalling | 开始呼叫其他人格[SSP] |
| OnGhostCallComplete | 完成呼叫其他人格[SSP] |
| OnGhostCalled | 被其他人格呼叫[SSP] |
| OnOtherGhostClosed | 其他人格已结束[SSP] |

- 请创建类似 OnGhostChanged<span style="color:red">_(Sakura侧的名字)</span> 的函数。
  - 上表中的名称 ＋ "_"(下划线) ＋ Sakura 名称
  - 这里需要的是 Sakura 名称，而不是人格名称。请注意。

- 如果名称中包含空格或 +- 等字符，这些字符都会被替换为 _。
  - 示例：`+Emily+`  ==>  `OnGhostChanged__Emily_`
  - 示例：`○|￣|_`  ==>  `OnGhostChanged_○_￣__`

- 如果词典中没有对应的人格，就会执行名称末尾加上 Other 的函数，例如 OnGhostChangedOther；如果也没有该函数，则会执行通常的启动或结束处理。

```
OnGhostChangingOther
OnGhostChangedOther
OnGhostCallingOther
OnGhostCalledOther
OnGhostCallCompleteOther
OnOtherGhostClosedOther
```

### 示例

例如，将[更改人格切换消息](ghost-switch-message.md)中的示例改写后如下。

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
