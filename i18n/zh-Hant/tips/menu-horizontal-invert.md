# 將選單反轉為橫向一整行

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

將選單反轉成橫向一整行（對話方塊的寬度），或許能讓選取更容易。

１）準備一個在選單項目後補上空格的函式。

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

２）將`\q`標籤的標題字串傳入MENUITEM函式。以下以紺野あやめ的選單為例進行加工。

- 原始內容

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

- 加工後（適用於AYA5.7 fix3以後）<br>
<span style="color:#cc0000">注意！</span>這只是**用「"」括住時可使用的簡便語法。**<br>
如果要串接變數或函式等的結果，請使用下一個項目。<br>
這種寫法只適用於不會變化、不會呼叫函式的純文字選單。

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

- 加工後

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

- 加工後（不使用分號的寫法）

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
