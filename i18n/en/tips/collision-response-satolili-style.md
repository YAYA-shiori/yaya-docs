# Responding to Clipping and Overlap in the Satori Style

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) Reposted from AYAYA Wiki

In Satori, it seems that clipping and overlap events occur after a short delay, even when the ghost enters a clipped or overlapped state.<br>
So, since that seems more natural behavior, here is how to do it in a talk.

It uses a lot of flags, so it is not very clean.

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

Here is another approach.<br>
Use this if the sample above does not work.<br>
(Note that `reference[*]` is used instead of reference\*.)

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
