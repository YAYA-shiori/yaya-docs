# 簡易配列からメニューを構築する

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

動的に要素数が変化する配列からメニューを構築し選択判定します。

１）初期化用の関数を用意します。

```
MyTestMenuItem
{
	testmenuitem1 = "てすと１,てすと２,てすと３"
	testmenuitem2 = "テスト１,テスト２,テスト３,テスト４,テスト５"
}
```

２）OnFirstBootおよびOnBootでMyTestMenuItemを呼びます。

３）既存の関数内に処理を埋め込みます。

```
OpenMenu
{
	"\0\s[0]/
		:
		:
	\q[メニュー１,TESTMENU1]\n/
	\q[メニュー２,TESTMENU2]\n/
		:
		:
	\e"
}

OnChoiceSelect
{
	//---- メニューアイテムIDを抽出する
	_menuitemid = 0	// ずっと下でこの変数を参照できるように、定義だけ行っておく。
	if STRSTR(reference0,"TESTMENUITEM1_",0) == 0
	{
		_menuitemid = TOINT(ERASE(reference0,0,STRLEN("TESTMENUITEM1_")))
		reference0 = "TESTMENUITEM1"
	}
	if STRSTR(reference0,"TESTMENUITEM2_",0) == 0
	{
		_menuitemid = TOINT(ERASE(reference0,0,STRLEN("TESTMENUITEM2_")))
		reference0 = "TESTMENUITEM2"
	}

	//---- メインメニュー
	case reference0
	{
			:
			:
		when "TESTMENU1"
		{
			//---- メニュー１表示
			_list = ""
			for _i = 0 ; testmenuitem1[_i] != "" ; _i++
			{
				_list += "\q[%(testmenuitem1[_i]),TESTMENUITEM1_%(_i)]\n"
			}
			"\0\s[0]\b[2]%(_list)\e"
		}
		when "TESTMENU2"
		{
			//---- メニュー２表示
			_list = ""
			for _i = 0 ; testmenuitem2[_i] != "" ; _i++
			{
				_list += "\q[%(testmenuitem2[_i]),TESTMENUITEM2_%(_i)]\n"
			}
			"\0\s[0]\b[2]%(_list)\e"
		}
		when "TESTMENUITEM1"
		{
			//---- とりあえずはアイテム文字列を喋るだけ
			"\0\s[0]%(testmenuitem1[_menuitemid])が選択されました。\e"
		}
		when "TESTMENUITEM2"
		{
			//---- とりあえずはアイテム文字列を喋るだけ
			"\0\s[0]%(testmenuitem2[_menuitemid])が選択されました。\e"
		}
			:
			:
	}
}
```
