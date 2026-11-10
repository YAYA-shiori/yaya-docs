# 讓滑鼠滾輪反應更自然

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### 原始的滑鼠滾輪反應

```
OnMouseWheel
{
	//0番キャラホイール反応
	if reference[3]==0 {
		"\0ころころすんな！\e"
	}
}
```

如此撰寫時，依滑鼠種類或設定而定，只滾動一次滑鼠滾輪，有時也會連續說出「ころころすんな！」2～3 次。<br>
可以改成等經過一定間隔後才觸發滑鼠滾輪反應，以避免這種情況。

### 間隔一段時間後才觸發滑鼠滾輪反應的範例

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

「if `_wheel_interval` > 1」中的「1」可依喜好設定秒數。

### 相關 Tips

- [讓滑鼠反應（撫摸反應）更自然](natural-mouse-response.md)
