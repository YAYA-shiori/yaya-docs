# Changes in Tension (Emotion Value)

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) Reposted from AYAYA Wiki

This is an article for the old version (文 Ver.4), updated to use the current function names (`SETDELIM` `TOINT` `CHR`).

Here is a method for changing a character's reactions by increasing or decreasing<br>
tension (emotion value) according to the content of the conversation.<br>
Example where the variable `tention` represents the emotion value.

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

Call `OnTalk` when delivering a talk.<br>
(From the notes in et cetera.)

## How It Works

`#define` replaces raw text in the dictionary, so when loaded, `\e:tention-5` becomes a string with the control character `CHR(1)` followed by `-5` after `\e`. `OnTalk` splits this string at `CHR(1)`, converts the last element (`-5`) to a number and adds it to `tention`, then removes the element and delimiter before outputting the result.

- [SETDELIM](../functions/SETDELIM.md)
- [TOINT](../functions/TOINT.md)
- [ERASE](../functions/ERASE.md)
- [#define](../grammar/08-preprocessor.md#define)
