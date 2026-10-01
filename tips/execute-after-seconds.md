# 指定秒数経過後にイベントを実行

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

### SetDelayEvent関数での例

- はろーYAYAわーるどかSimpleYAYAテンプレートのyaya_shiori3.dicにある、[SetDelayEvent関数](../system/yaya-shiori3-dic.md)を使用しています。

```
30秒待たせるイベント
{
	"\0\s[0]それでは30秒お待ち下さい。\e"
　
	SHIORI3FW.SetDelayEvent( '30秒待った' , 30 )
}

30秒待たせるイベント_残り時間確認
{
	"\0\s[0]残り%(SHIORI3FW.DelayEventTime)秒です。\e"
}

30秒待った
{
	"\0\s[0]お待たせしました。\e"
}
```

### 自作関数での例

```
OnSecondChange { //これ以外は自作関数
	if timerFlag == 1 {
		OnTimerCounter
	}
}

OnTimerStart { //OnTimerStart(60)とかで呼び出す。
	timerFlag = 1
	timerCount_s = _argv[0]//timerCount_sの現在値が残り時間。
}

OnTimerCounter { //計測中処理
	timerCount_s--
	if timerCount_s <= 0 { //タイマ終了処理
			OnTimerEnd
	}
}

OnTimerEnd {
	timerFlag = 0
	timerCount_s = 0
	//タイマ終了時に何か処理する場合このへんに書く
}
```

タイマを同時にいくつか計測したい場合は、もう少し工夫が必要です。
