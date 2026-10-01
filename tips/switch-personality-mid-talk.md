# 会話の途中で人格を切り替える

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

モードは変数 mode で持ち、0 と 1 のモードがあるとします。<br>
(0は通常モード、1は怒りモード)<br>
ランダムトークイベント RandomTalk は以下のように記述します。<br>

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

これで以下のように、特定の会話でモードを切り替えられます。<br>

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

(et cetera. の掲示板より。一部改変)
