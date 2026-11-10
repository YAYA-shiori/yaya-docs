# OnTranslate的用法

> 转自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

有人提出了相关问题，所以这里写了一个简单的用法示例。

<span style="color:red">aya_aitalk.dic</span>开头附近的

```
//OnTranslate
//{
//	REPLACE(reference0, "。", "にゅ。")
//}
```

将注释掉而处于无效状态的部分替换为以下内容。

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

## 说明

OnTranslate用于集中替换人格说出的脚本。<br>
例如更改句尾，或者避免添加敬称时出现重复。

```
_text = REPLACE(_text, "たん殿", "たん")
```

这里将「たん殿」替换为「たん」。<br>
后面的两个 " " 分别表示替换前和替换后的词语。可以替换成任意内容。

```
_text = RE_REPLACE(_text,"(ちゃん|くん|さん|殿)殿","殿")
```

这里将「ちゃん殿」「くん殿」「さん殿」「殿殿」等看起来会重复、不太合适的内容替换掉。

## 改造备忘

### 敬称相关

此外，例如想要处理「様殿」之类的情况时，

```
(ちゃん|くん|さん|殿)
```

可以在用括号括起并以 | 分隔的部分中添加

```
(ちゃん|くん|さん|殿|様)
```

这样就可以了；另外，如果你想在自己的人格中添加的不是「殿」，而是「さま」的话，

```
_text = RE_REPLACE(_text,"(ちゃん|くん|さん|殿|様|さま)さま","さま")
```

大概像这样就可以了。

### 自动等待仿制功能相关

例如

```
_text = REPLACE(_text, "！", "！\w5")
_text = REPLACE(_text, "？", "？\w5")
```

这样处理时，<br>
「！！！」或「？？？」会被<br>
！`\w5`！`\w5`！`\w5`　？`\w5`？`\w5`？`\w5`<br>
……替换成这样，总觉得不太理想。

```
_text = RE_REPLACE(_text ,'！(?=[^！\\])', '！\w5')
_text = RE_REPLACE(_text ,'？(?=[^？\\])', '？\w5')
```

正则表达式稍微有些复杂，这里就不作说明了，但这样就能解决问题。

### 自动等待：更完美的方法

使用上述方法时，连标签内部等内容也会被替换，导致问题。
下面提供了一个可以解决这些问题的函数。

2020/3/29更新 删除EVAL内部不必要的变量展开

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

只需将以下代码放入最上方的OnTranslate中（先删除自动等待部分）即可。

```
 _text = TextOnlyTranslator(_text,'TextOnlyTranslatorFunc')
```

正则表达式使用了[ukiya:正規表現講座/おまけ１](http://ukiya.sakura.ne.jp/index.php?正規表現講座/おまけ１)。
