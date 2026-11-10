# How to Use OnTranslate

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

Someone asked about it, so I wrote a simple example of how to use it.

Near the beginning of <span style="color:red">aya_aitalk.dic</span>,

```
//OnTranslate
//{
//	REPLACE(reference0, "。", "にゅ。")
//}
```

replace the section that is commented out and disabled with the following.

```
OnTranslate
{
   //とりあえず最初のおまじない(一時変数にとりあえず代入)
   _text = reference0
   
   //勝手にスクリプトにウエイトをかける例
   _text = REPLACE(_text, "、", "、\w5")
   _text = REPLACE(_text, "。", "。\w5")
   _text = REPLACE(_text, "…", "…\w5")
   
   //敬称置換の例
   //例外は先に書いておく
   _text = REPLACE(_text, "たん殿", "たん")
   
   //「さん殿」とかだぶりそうなのを置換
   _text = RE_REPLACE(_text,"(ちゃん|くん|さん|殿)殿","殿")
   
   //ここはおまじないのつもりで。消しちゃだめです。
   //(一時変数で置き換え処理したものを結果として返す)
   _text
}
```

## Explanation

OnTranslate is used to replace the ghost's speech script all at once afterward.<br>
For example, you can change sentence endings or prevent honorifics from being duplicated.

```
_text = REPLACE(_text, "たん殿", "たん")
```

This replaces "たん殿" with "たん".<br>
The last two " " are the words before and after replacement, respectively. You can change them to anything you like.

```
_text = RE_REPLACE(_text,"(ちゃん|くん|さん|殿)殿","殿")
```

This replaces phrases that would look problematic if duplicated, such as "ちゃん殿", "くん殿", "さん殿", and "殿殿".

## Modification notes

### Honorifics

For other cases, for example, if you also want to handle “様殿,”

```
(ちゃん|くん|さん|殿)
```

add it to the part enclosed in parentheses and separated by |, like this:

```
(ちゃん|くん|さん|殿|様)
```

That should work. Or, if your ghost uses “さま” instead of adding “殿,” you could do this:

```
_text = RE_REPLACE(_text,"(ちゃん|くん|さん|殿|様|さま)さま","さま")
```

Something like this.

### About automatic-wait approximations

For example,

```
_text = REPLACE(_text, "！", "！\w5")
_text = REPLACE(_text, "？", "？\w5")
```

In this case, <br>
“！！！” and “？？？”<br>
！`\w5`！`\w5`！`\w5`　？`\w5`？`\w5`？`\w5`<br>
… get replaced as shown, which is not ideal.

```
_text = RE_REPLACE(_text ,'！(?=[^！\\])', '！\w5')
_text = RE_REPLACE(_text ,'？(?=[^？\\])', '？\w5')
```

This uses a somewhat complicated regular expression, so I’ll skip the explanation, but this solves the problem.

### Automatic wait: an even more perfect method

With the method above, even text inside tags gets replaced, which can cause serious problems.
The following function addresses that.

Updated 2020/3/29: Removed unnecessary variable expansion inside EVAL

```
TextOnlyTranslator
{
	_string = RE_SPLIT(_argv[0],'\\(\\|q\[.*?\]\[.*?\]|[!&8cfijmpqsn]\[.*?\]|[-*+014567bcehntuvxz]|_[ablmsuvw]\[.*?\]|__(t|[qw]\[.*?\])|_[!?+nqsV]|[sipw][0-9])')
	_n = ARRAYSIZE(_string)
	_tag = RE_GETSTR()
	_tr = ''
	_qs = 0
	
	for _i = 0 ; _i < _n ; _i++ {
		_tr += EVAL("%(_argv[1])(_string[_i],_qs)")
		_tr += _tag[_i]
		if '\_q' _in_ _tag[_i] {
			_qs = ! _qs
		}
	}
	
	_tr
}

TextOnlyTranslatorFunc
{
	//_argv[0] = 置換対象テキスト
	//_argv[1] = クイックセクション内か否か
	
	_text = _argv[0]
	if ! _argv[1] {
		_text = REPLACE(_text, "、", "、\w5")
		_text = REPLACE(_text, "。", "。\w9")
		_text = REPLACE(_text, "…", "…\w9")
		_text = REPLACE(_text, "？", "？\w9")
		_text = RE_REPLACE(_text , '\n\n(?=[^\[])', '\w9\n\n')
		_text = RE_REPLACE(_text ,'！(?=[^！])', '！\w9')
	}
	_text
}
```

To use it, just add the following code inside OnTranslate at the very top (after temporarily removing the automatic-wait section).

```
 _text = TextOnlyTranslator(_text,'TextOnlyTranslatorFunc')
```

For regular expressions, this uses [Regex Tutorial/Extra 1](http://ukiya.sakura.ne.jp/index.php?正規表現講座/おまけ１).
