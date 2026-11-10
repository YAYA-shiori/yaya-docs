# 在对话过程中切换人格模式

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

假设使用变量 mode 保存模式，模式有 0 和 1 两种。<br>
（0 为普通模式，1 为愤怒模式）<br>
随机对话事件 RandomTalk 按如下方式编写。<br>

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

这样就可以像下面这样，在特定对话中切换模式。<br>

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

（摘自 et cetera. 的论坛，内容略有修改）
