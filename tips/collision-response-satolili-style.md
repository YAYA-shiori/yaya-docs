# 見切れ・重なり反応を里々風に

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

里々では、見切れ・重なり状態になっても多少の間を空けてから見切れ・重なりイベントが発生するようです。<br>
で、その方が動作としては自然っぽいので、文でやる方法を。

フラグ使いまくりなのであまり綺麗じゃありませんが。

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

別解書いてみました。<br>
上のサンプルが動作しない場合はこちらを。<br>
（reference\*を`reference[*]`と書いています）

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
