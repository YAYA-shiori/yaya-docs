# Switch Personality Mid-Conversation

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

Let the mode be stored in the variable mode, with modes 0 and 1.<br>
(0 is normal mode, and 1 is angry mode)<br>
Write the RandomTalk event as follows.<br>

```
RandomTalk
{
	if ISINTEGER(mode) == 0 {
	mode = 0
	}
	_t = CALLBYNAME("RandomTalk%mode")
	_l = STRLEN(_t)
	if _l > 8 {
		_pos = _l - 8
		_emd = SUBSTR(_t, _pos, 8)
		if _emd == "->mode=1" {
		mode = 1
		_t = SUBSTR(_t, 0, _pos)
		}
		elseif _emd == "->mode=0" {
		mode = 0
		_t = SUBSTR(_t, 0, _pos)
		}
	}
	_t
}
```

This lets you switch modes in specific conversations, as follows.<br>

```
// \eの後で「->mode=?」(「?」は切り替えたいモードの数字)を入れる

RandomTalk0 : nonoverlap
{
	"\0\s[0]こんにちは。\e"
	"\0\s[0]怒ったぞー。\e->mode=1"
	"\0\s[0]やっほー\e"
	"\0\s[0]あはは。\e"
}

RandomTalk1 : nonoverlap
{
	"\0\s[7]いいかげんにして。\e"
	"\0\s[7]許してあげる。\e->mode=0"
	"\0\s[7]もう、だまされないよ。\e"
	"\0\s[7]ウソばっかり。\e"
}
```

(From the et cetera bulletin board. Partially modified)
