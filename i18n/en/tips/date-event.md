# Date Events

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

It is convenient to use the GetTimeSlot function in aya_bootend.dic from the template ghost “Konnoyayame”.<br>

(Example) Adding a Christmas event<br>
First, add the following statement to GetTimeSlot.<br>

```
elseif month == 12 && day == 25
{
	"クリスマス"
}
```

Next, add an event to OnBoot that is triggered only on Christmas Day, and you are done.

```
elseif _timeslot == "クリスマス"
{
	"\1\s[10]\0\s[0]今日はクリスマスです。\e"
}
```
