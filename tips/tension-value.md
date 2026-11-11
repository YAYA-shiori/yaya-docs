# テンション(感情値)の上下

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

旧版（文 Ver.4 向け）の記事を、現行の関数名（`SETDELIM` `TOINT` `CHR`）に書き換えたものです。

会話の内容によって、テンション(感情値)を上下させて<br>
キャラクターの反応を変える方法として、下記のやり方があります。<br>
変数 `tention` が感情値を表す場合の例。

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

トークの際に `OnTalk` を呼ぶようにしてください。<br>
(et cetera. の雑記内より)

## 仕組み

`#define` は辞書の生テキストを置換するので、`\e:tention-5` は読み込み時に、`\e` の後ろに制御文字 `CHR(1)` と `-5` が続く文字列になります。`OnTalk` はこの文字列を `CHR(1)` で区切り、最後の要素（`-5`）を数値にして `tention` に足し、区切りごと取り除いてから出力します。

- [SETDELIM](../functions/SETDELIM.md)
- [TOINT](../functions/TOINT.md)
- [ERASE](../functions/ERASE.md)
- [#define](../grammar/08-preprocessor.md#define)
