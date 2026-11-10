# Make Wheel Responses Feel Natural

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### Basic Wheel Response

```
OnMouseWheel
{
	//0番キャラホイール反応
	if reference[3]==0 {
		"\0ころころすんな！\e"
	}
}
```

Depending on the mouse or its settings, this may cause the ghost to say “ころころすんな！” two or three times in a row after scrolling the wheel just once.<br>
Avoid this by making the wheel response wait for a set interval.

### Example: Wheel Response After a Set Interval

```
OnMouseWheel
{
//ホイール間隔計算
_wheel_interval = systemuptime - wheel_prev
	//最後のホイール反応から一定秒数経過
	if _wheel_interval > 1 {
		//最後のホイール反応時刻を記憶
		wheel_prev = systemuptime
			//0番キャラホイール反応
			if reference[3]==0 {
				"\0ころころすんな！\e"
			}
	}
}

OnGhostUnload
{
	//ホイール反応で使用する変数の削除（これを実行しないと正常に動かない）
	ERASEVAR('wheel_prev')
}
```

The “1” in “if `_wheel_interval` > 1” can be any interval you prefer, in seconds.

### Related Tips

- [Make mouse responses (petting responses) feel natural](natural-mouse-response.md)
