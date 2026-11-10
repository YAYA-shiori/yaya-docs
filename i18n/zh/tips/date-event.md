# 日期事件

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

使用模板人格「紺野あやめ」的aya_bootend.dic中的GetTimeSlot函数会很方便。<br>

（例）添加圣诞节事件<br>
首先，在GetTimeSlot中添加以下语句。<br>

```
elseif month == 12 && day == 25
{
	"クリスマス"
}
```

接下来，在OnBoot中添加仅在圣诞节当天触发的事件即可。

```
elseif _timeslot == "クリスマス"
{
	"\1\s[10]\0\s[0]今日はクリスマスです。\e"
}
```
