# 以里々風格處理畫面裁切與重疊反應

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

在里々中，即使進入畫面裁切或重疊狀態，似乎也會稍微等一會兒，才觸發畫面裁切或重疊事件。<br>
而且這樣的動作似乎比較自然，以下介紹如何用文句處理。

雖然大量使用旗標，寫法不太簡潔。

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

這裡也提供另一種寫法。<br>
如果上面的範例無法運作，請改用這個。<br>
（將reference\*寫成`reference[*]`）

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
