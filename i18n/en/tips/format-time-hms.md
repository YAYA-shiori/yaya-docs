# Convert Seconds to Hours, Minutes, and Seconds

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

## Function

```
sec_hms {
_v=TOINT(_argv[0])

_a1=_v/3600
_a2=(_v-(_a1*3600))/60
_a3=(_v-(_a1*3600))-(_a2*60)

_v=(_a1,_a2,_a3)
_v
}
```

### Usage

```
sec_hms ( 秒数 )
```

Returns an array of “hours [0], minutes [1], and seconds [2].”<br>
Even if the number of “hours” is 30, it will return “30 hours,” not “1 day and 6 hours” (modify the function if you also need units for years, months, and days).<br>

### Example

- This uses the time-related function ghostuptime in yaya_shiori3.dic.

```
ゴースト起動時間
{
	//ghostuptimeはゴーストの連続起動時間（単位：秒）
	_h = sec_hms (ghostuptime)[0]
	_m = sec_hms (ghostuptime)[1]
	_s = sec_hms (ghostuptime)[2]
	"\0\s[0]私が起動してから%(_h)時間%(_m)分%(_s)秒経過しました。\e"
}
```
