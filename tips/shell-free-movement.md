# シェルの自由移動

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

**(注意)**<br>
SSP/CROWのみで使えます。Materiaでは自由移動になりません。

ゴースト側でシェルの自由移動を定義する場合、下記を会話スクリプトに組み込んでください。

```
\0\1\_s\![set,alignmenttodesktop,free]\_s
```

(例)紺野あやめのOnBootに組み込む場合

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

- 応用編。

シェルの自由移動、画面下固定を切り替える場合。<br>

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

このスクリプトを記述したあと、%movement_statusを<br>
OnBoot、OnGhostChanged、OnShellChangedに追加してください。<br>
(例)

```
OnShellChanged
{
	"\0\s[0]%reference0シェルに替わりました。どうですか？/
	\w6\1\s[10]イイ！%movement_status\e"
}
```
