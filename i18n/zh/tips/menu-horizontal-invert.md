# 将菜单按一整行宽度翻转

> 转引自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

将菜单按一整行（对话框宽度）翻转，或许会更容易选择。

1）准备一个在菜单项后补足空格的函数。

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

2）将`\q`标签的标题字符串传入MENUITEM函数。下面以加工紺野あやめ的菜单为例。

- 原始版本

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

- 加工后（适用于AYA5.7 fix3及更高版本）<br>
<span style="color:#cc0000">注意！</span>这只是一种仅适用于用**" "括起来时的简写语法。**<br>
如果想拼接变量或函数等的结果，请使用下面再下一项中的方法。<br>
最好将其理解为：只适用于不会变化、不调用函数的纯文本菜单。

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

- 加工后

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

- 加工后（不使用分号的写法）

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
