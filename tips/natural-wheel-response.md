# ホイール反応を自然なものにする

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

### 素のままのホイール反応

```
OnMouseWheel
{
	//0番キャラホイール反応
	if reference[3]==0 {
		"\0ころころすんな！\e"
	}
}
```

こう書くと、マウスの種類や設定によっては一回ホイール回しただけで2～3回連続「ころころすんな！」とトークされてしまうことがある。<br>
これを一定間隔時間が空いてからホイール反応させるようにして回避。

### 一定間隔空いてからホイール反応例

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

「if `_wheel_interval` > 1」の「1」は好みの秒数で。

### 関連Tips

- [マウス反応（なで反応）を自然なものにする](natural-mouse-response.md)
