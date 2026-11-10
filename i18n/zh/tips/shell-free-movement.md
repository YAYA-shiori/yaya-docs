# 外壳自由移动

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

**（注意）**<br>
仅适用于 SSP/CROW。在 Materia 中无法自由移动。

若要在人格一侧定义外壳的自由移动，请将以下内容加入对话脚本。

```
\0\1\_s\![set,alignmenttodesktop,free]\_s
```

（示例）将其加入紺野あやめ的 OnBoot 中

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

- 进阶用法。

切换外壳自由移动和固定在屏幕底部的状态。<br>

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

写好这个脚本后，请将 %movement_status<br>
添加到 OnBoot、OnGhostChanged 和 OnShellChanged 中。<br>
（示例）

```
OnShellChanged
{
	"\0\s[0]%reference0シェルに替わりました。どうですか？/
	\w6\1\s[10]イイ！%movement_status\e"
}
```
