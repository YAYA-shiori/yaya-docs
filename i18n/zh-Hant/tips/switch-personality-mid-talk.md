# 在對話途中切換人格模式

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

假設以變數 mode 保存模式，並有 0 和 1 兩種模式。<br>
（0 為一般模式，1 為生氣模式）<br>
隨機對話事件 RandomTalk 撰寫如下。<br>

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

如此一來，就能像以下範例一樣，在特定對話中切換模式。<br>

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

（摘自 et cetera. 的留言板，內容略有修改）
