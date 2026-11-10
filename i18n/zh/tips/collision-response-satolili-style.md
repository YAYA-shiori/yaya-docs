# 以里々风格处理被遮挡・重叠

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

在里々中，即使进入被遮挡或重叠状态，似乎也会经过一段时间后才触发被遮挡或重叠事件。<br>
而且，这样的行为看起来更自然一些，下面介绍一种用句子实现的方法。

虽然大量使用了标志，不太简洁。

```
OnSecondChange
{
    if mikireenable && reference1 && !mikireflag {
       mikiretimer--;
       if mikiretimer < 1 {
          mikireflag   = 1
          "" //見切れ反応時のトーク
       }
    } else {
       mikiretimer = 5
    }
 
    if mikireflag && !reference1 {
       //5秒以内に復帰した場合は、見切れ後トークを行わない
       endmikire = 1
    }
 
    if endmikire {
       "" //見切れ終了時のトーク
    }
 
    if kasanarienable && reference2 {
       kasanaritimer--;
       if kasanaritimer < 1 {
          kasanarienable = 0;
          "" //重なり反応時のトーク
          kasanarienable = 1;
       }
    } else {
       kasanaritimer = 5
    }
}
```

--せきやひろし

我试着写了另一种方法。<br>
如果上面的示例无法运行，请使用这个。<br>
（将reference\*写作`reference[*]`）

```
OnSecondChange
{
　　//見切れ反応（メインキャラ見切れ5秒後）
　　if reference[1] && !mikireflag {
　　　　mikiretimer--
　　　　if mikiretimer < 1 {
　　　　　　mikireflag = 1
　　　　　　"" //見切れ反応時のトーク
　　　　}
　　}
　　else {
　　　　mikiretimer = 5
　　}

　　//見切れ終了反応（見切れ終了直後）
　　if mikireflag && !reference[1] {
　　　　mikireflag = 0
　　　　"" //見切れ終了時のトーク
　　}

　　//重なり反応（メインとサブキャラの重なり5秒後）
　　elseif !kasanariflag && reference[2] {

　　　　if ISVAR('kasanaritimer') == 0 {
　　　　　　kasanaritimer = 5
　　　　}

　　　　kasanaritimer--
　　　　if kasanaritimer < 1 {
　　　　　　kasanariflag = 1
　　　　　　"" //重なり反応時のトーク
　　　　}
　　}
　　//重なり終了反応（重なり終了直後）
　　elseif kasanariflag && !reference[2] {
　　　　kasanariflag = 0
　　　　kasanaritimer = 5
　　　　"" //重なり反応終了時のトーク
　　}
　　else {
　　　　kasanaritimer = 5
　　}
}
```
