# メニューを横一ライン反転

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

メニューを横一ライン（バルーンの幅）で反転させると、選択しやすくなるかもしれません。

１）メニュー項目の後ろにスペースを補完する関数を用意します。

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

２）`\q`タグのタイトル文字列をMENUITEM関数に通します。例として紺野あやめのメニューを加工してみます。

- オリジナル

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

- 加工後(AYA5.7 fix3以降用)<br>
<span style="color:#cc0000">注意！</span>あくまでも**" "で囲む際に使える手抜き構文です。**<br>
変数や関数等の結果をつなげたいという場合などは、もうひとつ下の項目を使ってください。<br>
変化しない、関数を呼ばない、ただの文字列メニューの時にのみ使えると考えるとよいでしょう。

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

- 加工後（セミコロンを使用しない記述）

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
