# Invert the Menu One Horizontal Line at a Time

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

Inverting the menu one horizontal line at a time (the width of the balloon) may make it easier to select items.

1) Prepare a function that pads menu items with spaces.

```
MENUITEM
{
	_menuitem = _argv[0]
	for _i = GETSTRBYTES(_menuitem) ; _i < 48 ; _i++
	{
		_menuitem += " "
	}
	_menuitem
}
```

2) Pass the title strings of the `\q` tags to the MENUITEM function. As an example, let's modify Konnono Ayame's menu.

- Original

```
OpenMenu
{
	"\0\s[0]"
	--
	"はい、なんでしょうか？"
	"%username、なんですか？"
	"ん‥‥どうしたの？"
	--
	"\n\n/
	\q[なんか話して,AITALK]\n/
	\q[しゃべり頻度を変えて,TALKINTERVAL]\n/
	\q[コミュニケート,COMMUNICATEOPEN]\n/
	\q[AIについて,ABOUTAYA]\n/
	\q[なんでもない,CANCEL]\e"
}
```

- Modified (for AYA5.7 fix3 and later)<br>
<span style="color:#cc0000">Caution!</span> This is only a **shortcut syntax for when enclosing text in " ".**<br>
If you want to concatenate the results of variables, functions, and so on, use the next item below.<br>
This is best suited for menus made up of plain strings that do not change and do not call functions.

```
OpenMenu
{
	"\0\s[0]"
	--
	"はい、なんでしょうか？"
	"%username、なんですか？"
	"ん‥‥どうしたの？"
	--
	"\n\n/
	\q[%(MENUITEM('なんか話して')),AITALK]\n/
	\q[%(MENUITEM('しゃべり頻度を変えて')),TALKINTERVAL]\n/
	\q[%(MENUITEM('コミュニケート')),COMMUNICATEOPEN]\n/
	\q[%(MENUITEM('AIについて')),ABOUTAYA]\n/
	\q[%(MENUITEM('なんでもない')),CANCEL]\e"
}
```

- Modified

```
OpenMenu
{
	"\0\s[0]"
	--
	"はい、なんでしょうか？"
	"%username、なんですか？"
	"ん‥‥どうしたの？"
	--
	"\n\n/
	\q[";--;MENUITEM("なんか話して");--;",AITALK]\n/
	\q[";--;MENUITEM("しゃべり頻度を変えて");--;",TALKINTERVAL]\n/
	\q[";--;MENUITEM("コミュニケート");--;",COMMUNICATEOPEN]\n/
	\q[";--;MENUITEM("AIについて");--;",ABOUTAYA]\n/
	\q[";--;MENUITEM("なんでもない");--;",CANCEL]\e"
}
```

- Modified (syntax without semicolons)

```
OpenMenu
{
	"\0\s[0]"
	--
	"はい、なんでしょうか？"
	"%username、なんですか？"
	"ん‥‥どうしたの？"
	--
	"\n\n/
	\q["
	--
	MENUITEM("なんか話して")
	--
	",AITALK]\n/
	\q["
	--
	MENUITEM("しゃべり頻度を変えて")
	--
	",TALKINTERVAL]\n/
	\q["
	--
	MENUITEM("コミュニケート")
	--
	",COMMUNICATEOPEN]\n/
	\q["
	--
	MENUITEM("AIについて")
	--
	",ABOUTAYA]\n/
	\q["
	--
	MENUITEM("なんでもない")
	--
	",CANCEL]\e"
}
```
