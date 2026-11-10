# Change Ghost-Switch Messages (New)

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

As the number of ghosts with switch reactions increases, the dictionary gets harder and harder to navigate.<br>
Use this method in that case.

**Updated-20061023**: Incorporates the report at <http://acronotes.seesaa.net/article/25705192.html>

### 1) Remove OnGhostChanging and OnGhostChanged and replace them with the following.

They are usually near the end of aya_bootend.dic.<br>
If you are not comfortable removing them outright, rename the two existing functions as follows:

| Before | After |
|---|---|
| OnGhostChanging | OnGhostChanging<span style="color:red">Other</span> |
| OnGhostChanged | OnGhostChanged<span style="color:red">Other</span> |

Then paste everything in the box below at the very end of the dictionary.

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

### 2) Create new functions for each ghost

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

| Name to write | Function |
|---|---|
| OnGhostChanging | Switching to another ghost |
| OnGhostChanged | Switching from another ghost |
| OnGhostCalling | Starting a call to another ghost [SSP] |
| OnGhostCallComplete | Call to another ghost completed [SSP] |
| OnGhostCalled | Called by another ghost [SSP] |
| OnOtherGhostClosed | Another ghost has closed [SSP] |

- Create a function such as OnGhostChanged<span style="color:red">_(Sakura-side name)</span>.
  - The name from the table above + "_" (underscore) + the Sakura name
  - This is the Sakura name, not the ghost name. Take care.

- In special cases where the name contains spaces, +, -, and similar characters, they are all replaced with _.
  - Example: `+Emily+`  ==>  `OnGhostChanged__Emily_`
  - Example: `○|￣|_`  ==>  `OnGhostChanged_○_￣__`

- If the dictionary has no function for the relevant ghost, it will call the function with Other appended, such as OnGhostChangedOther. If that function is also missing, the normal boot or shutdown processing is used.

```
OnGhostChangingOther
OnGhostChangedOther
OnGhostCallingOther
OnGhostCalledOther
OnGhostCallCompleteOther
OnOtherGhostClosedOther
```

### Example

For example, rewriting the example in [Change Ghost-Switch Messages](ghost-switch-message.md) gives the following:

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
