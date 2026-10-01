# 使用しているソフトを判別

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

使用しているソフト（ベースウェア）を判別します。

```
BwName
{
	if basewarename == "embryo"
	{
		//---- 伺か専用
		"MATERIA"
	}
	elseif basewarename == "SSP"
	{
		//---- SSP専用
		"SSP"
	}
	elseif basewarename == "crow"
	{
		//---- CROW専用
		"CROW"
	}
	else
	{
		//---- その他の場合
		"etc"
	}
}
```

これを応用して、トークネタを変えたり、機能を制限したりと…。<br>
一工夫してみると、面白いかもしれません。(猫夢紗)

## basewarenameについて

変数basewarenameは必ずしもベースウェアの名前が入っているという訳ではないため
basewarenameをbasewarenameexに書き換えたほうが安全です。<br>
（変数「basewarenameex」は[はろーYAYAわーるど](http://ms.shillest.net/yayame.xhtml)、[SimpleYAYAテンプレート](../other/simple-yaya-template.md)などにあります。
他のテンプレートでは存在しない可能性があります）
