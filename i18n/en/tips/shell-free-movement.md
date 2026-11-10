# Free Movement of the Shell

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

**(Note)**<br>
This works only with SSP/CROW. The shell cannot move freely in Materia.

To define free movement for the shell on the ghost side, add the following to the conversation script.

```
\0\1\_s\![set,alignmenttodesktop,free]\_s
```

(Example) To add it to Konnonayame's OnBoot

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

- Advanced example.

To switch between free movement of the shell and fixing it to the bottom of the screen.<br>

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

After writing this script, add %movement_status to<br>
OnBoot, OnGhostChanged, and OnShellChanged.<br>
(Example)

```
OnShellChanged
{
	"\0\s[0]%reference0シェルに替わりました。どうですか？/
	\w6\1\s[10]イイ！%movement_status\e"
}
```
