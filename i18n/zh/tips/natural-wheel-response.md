# 让滚轮反应更自然

> 转引自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### 原样的滚轮反应

```
OnMouseWheel
{
	//0番キャラホイール反応
	if reference[3]==0 {
		"\0ころころすんな！\e"
	}
}
```

这样编写时，根据鼠标类型或设置，有时只滚动一次滚轮，就会连续对话2～3次「ころころすんな！」。<br>
可以通过让滚轮反应在经过固定时间间隔后才触发来避免这种情况。

### 间隔固定时间后触发滚轮反应的示例

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

「if `_wheel_interval` > 1」中的「1」可以改为自己喜欢的秒数。

### 相关提示

- [让鼠标反应（抚摸反应）更自然](natural-mouse-response.md)
