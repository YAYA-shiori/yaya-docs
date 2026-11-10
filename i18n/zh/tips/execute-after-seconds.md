# 经过指定秒数后执行事件

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### 使用 SetDelayEvent 函数的示例

- 使用 Hello YAYA World 或 SimpleYAYA 模板的 yaya_shiori3.dic 中的 [SetDelayEvent 函数](../system/yaya-shiori3-dic.md)。

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

### 使用自定义函数的示例

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

如果想同时计量多个计时器，还需要进一步改进。
