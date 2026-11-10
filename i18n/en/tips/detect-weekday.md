# Detecting the Day of the Week

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

```
weekj
{
　if weekday == 0
　{
　　// ---- 日曜日
　　"（日）"
　}
　elseif weekday == 1
　{
　　// ---- 月曜日
　　"（月）"
　}
　elseif weekday == 2
　{
　　// ---- 火曜日
　　"（火）"
　}
　elseif weekday == 3
　{
　　// ---- 水曜日
　　"（水）"
　}
　elseif weekday == 4
　{
　　// ---- 木曜日
　　"（木）"
　}
　elseif weekday == 5
　{
　　// ---- 金曜日
　　"（金）"
　}
　else
　{
　　// ---- 土曜日
　　"（土）"
　}
}
```

You can use this to change talk topics, restrict functionality, and so on…<br>
A little experimentation might lead to something interesting. (NekoQ)<br>

### Version Using an Array

If you simply want to return the day of the week, using an array…

```
weekj
{
       ("(日)","(月)","(火)","(水)","(木)","(金)","(土)")[weekday];
}
```

might be more elegant (though a little hard to understand).<br>
This notation can probably be easily adapted to other things, too (such as the traditional names for months).<br>
Hiroshi Sekiya

### Make It Even More Elegant with a Simple Array

This is slower than a generic array, but

```
weekj
{
  "(日),(月),(火),(水),(木),(金),(土)"[weekday]
}
```

also works. Since you just list the items separated by commas, this may be easier to adapt to other uses.
