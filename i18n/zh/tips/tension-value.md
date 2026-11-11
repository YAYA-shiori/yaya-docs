# 情绪值（情感值）的升降

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

本文将旧版（面向文 Ver.4）的文章中的函数名改写为当前的函数名（`SETDELIM` `TOINT` `CHR`）。

根据对话内容升降情绪值，<br>
从而改变角色反应的方法如下。<br>
以下以变量 `tention` 表示情绪值为例。

```
#define :tention+  %(CHR(1))
#define :tention-  %(CHR(1))-

TalkScript
{
	if tention > 10
	{
		"ハイテンション！"
		"舞い上がってお茶こぼした…\e:tention-5"
	}
	elseif tention > 5
	{
		"普通テンション"
		"阪神勝ったー！\e:tention+5"
	}
	else
	{
		"鬱"
	}
}

OnTalk
{
	_script = TalkScript
	SETDELIM(_script, CHR(1))
	_lastindex = ARRAYSIZE(_script) - 1
	if _lastindex > 0 {
		tention += TOINT(_script[_lastindex])
		_lastlen = STRLEN(_script[_lastindex])
		_eraseindex = STRLEN(_script) - _lastlen - 1
		_erasesize = _lastlen + 1
		_script = ERASE(_script, _eraseindex, _erasesize)
	}
	_script
}
```

请在对话时调用 `OnTalk`。<br>
（摘自 et cetera. 的杂记）

## 原理

`#define` 会替换词典的原始文本，因此 `\e:tention-5` 在加载时会变成 `\e` 后面接着控制字符 `CHR(1)` 和 `-5` 的字符串。`OnTalk` 会用 `CHR(1)` 分割这个字符串，将最后一个元素（`-5`）转换为数值并加到 `tention` 上，然后连同分隔符一起删除，再输出字符串。

- [SETDELIM](../functions/SETDELIM.md)
- [TOINT](../functions/TOINT.md)
- [ERASE](../functions/ERASE.md)
- [#define](../grammar/08-preprocessor.md#define)
