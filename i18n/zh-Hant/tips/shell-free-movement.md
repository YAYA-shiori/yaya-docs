# 外殼自由移動

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

**（注意）**<br>
僅能在 SSP/CROW 中使用。在 Materia 中不會自由移動。

若要在人格端定義外殼自由移動，請將以下內容加入對話指令碼。

```
\0\1\_s\![set,alignmenttodesktop,free]\_s
```

（範例）在紺野あやめ的 OnBoot 中加入

```
OnBoot
{
	//---- まず双方のサーフィスを表示
	"\0\s[0]\1\s[10]\0\1\_s\![set,alignmenttodesktop,free]\_s" // ←ここに組み込む
	--
	//---- 起動時間を確認してあいさつを変化
	_timeslot = GetTimeSlot
	if _timeslot == "朝"
	(以下省略)
```

- 應用篇。

切換外殼自由移動與固定在畫面底部時。<br>

```
Free_movement
{
	"\0\s[0]どうされますか？\n\n[half]<br>/
	\![*]\q[自由に動いて,Free_movement_On]\n/
	\![*]\q[一番下にいて,Free_movement_Off]\e"
}

Free_movement_On
{
	movement = 1
	"\0\s[5]はい、分かりました。\0\1\_s\![set,alignmenttodesktop,free]\_s\e"
}

Free_movement_Off
{
	movement = 0
	"\0\s[0]はい、分かりました。\0\1\_s\![set,alignmenttodesktop,bottom]\_s\e"
}

// 起動時用
movement_status
{
	CALLBYNAME("movement_status%movement")
}

movement_status0
{
	"\0\1\_s\![set,alignmenttodesktop,bottom]\_s"
}

movement_status1
{
	"\0\1\_s\![set,alignmenttodesktop,free]\_s"
}
```

撰寫此指令碼後，請將 %movement_status 加入<br>
OnBoot、OnGhostChanged、OnShellChanged。<br>
（範例）

```
OnShellChanged
{
	"\0\s[0]%reference0シェルに替わりました。どうですか？/
	\w6\1\s[10]イイ！%movement_status\e"
}
```
