# Detecting the Software in Use

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

Detects the software (baseware) in use.

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

You can use this to change talk topics, restrict features, and so on...<br>
With a little ingenuity, you might come up with something interesting. (Nekoyumesha)

## About basewarename

Since the variable basewarename does not necessarily contain the name of the baseware,
it is safer to change basewarename to basewarenameex.<br>
(The variable "basewarenameex" is available in [Hello YAYA World](http://ms.shillest.net/yayame.xhtml), [SimpleYAYA template](../other/simple-yaya-template.md), and so on.
It may not be available in other templates.)
