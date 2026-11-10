# 从简易数组构建菜单

> 转自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

根据元素数量会动态变化的数组构建菜单并判断选择结果。

１）准备一个用于初始化的函数。

```
MyTestMenuItem
{
	testmenuitem1 = "てすと１,てすと２,てすと３"
	testmenuitem2 = "テスト１,テスト２,テスト３,テスト４,テスト５"
}
```

２）在 OnFirstBoot 和 OnBoot 中调用 MyTestMenuItem。

３）将处理代码嵌入现有函数中。

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
