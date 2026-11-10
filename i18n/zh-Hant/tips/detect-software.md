# 判別正在使用的軟體

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

判別正在使用的軟體（baseware）。

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

將這個方法加以應用，可以更換對話內容、限制功能等…。<br>
稍微花點心思嘗試一下，或許會很有趣。（猫夢紗）

## 關於 basewarename

變數 basewarename 不一定會存放 baseware 的名稱，因此
將 basewarename 改寫為 basewarenameex 會比較安全。<br>
（變數「basewarenameex」存在於[はろーYAYAわーるど](http://ms.shillest.net/yayame.xhtml)、[SimpleYAYA 範本](../other/simple-yaya-template.md)等處。
其他範本可能沒有這個變數）
