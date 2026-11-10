# 判断正在使用的软件

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

判断正在使用的软件（baseware）。

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

以此为基础，可以更改对话内容、限制功能等……<br>
稍作改进的话，说不定会很有趣。（猫夢紗）

## 关于basewarename

变量basewarename不一定会存储baseware的名称，
因此将basewarename改写为basewarenameex会更安全。<br>
（变量「basewarenameex」存在于[はろーYAYAわーるど](http://ms.shillest.net/yayame.xhtml)、[SimpleYAYA模板](../other/simple-yaya-template.md)等模板中。
其他模板中可能不存在）
