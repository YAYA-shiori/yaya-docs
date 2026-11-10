# 日期事件

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

使用範本人格「紺野あやめ」的aya_bootend.dic中所含的GetTimeSlot函式，就能輕鬆處理。<br>

（範例）新增聖誕節事件<br>
首先，在GetTimeSlot中加入以下內容。<br>

```
elseif month == 12 && day == 25
{
	"クリスマス"
}
```

接著，在OnBoot中加入只在聖誕節當天觸發的事件，就完成了。

```
elseif _timeslot == "クリスマス"
{
	"\1\s[10]\0\s[0]今日はクリスマスです。\e"
}
```
