# 起動してなかった時間により起動トークを変える

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

```
//ゴーストアンロード時に呼ばれるイベント
OnGhostUnload
{
	//最後に終了した時の、1970/1/1 00:00:00からの経過秒取得
	LastCloseSecCount = GETSECCOUNT()
}

//OnBootやOnGhostChanged等から使う
起動イベント
{
	//最後に終了してから再起動までの経過秒取得
	_SecCount= GETSECCOUNT() - LastCloseSecCount

	//最後に終了してから再起動までの経過日数取得
	_DayCount = _SecCount/60/60/24
	
		//終了後10分以内に起動した
		if _SecCount < 600 {
			"\0あれ、帰ったと思ったらもう来たの？\e"
		}
		//終了後一週間以上経過して起動した
		elseif _DayCount > 7 {
			"\0%(_DayCount)日ぶりだね～！おひさし～！\e"
		}
		//それ以外の時の通常トーク
		else {
			"\0こんにちは！\e"
		}
}
```
