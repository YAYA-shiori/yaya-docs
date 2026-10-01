# OnTranslateの使い方

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

質問があったので、使い方の簡単な例を書いてみました。

<span style="color:red">aya_aitalk.dic</span>の先頭あたりの

```
//OnTranslate
//{
//	REPLACE(reference0, "。", "にゅ。")
//}
```

とコメントにして無効化している部分を以下に置き換えます。

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

## 解説

OnTranslateは、ゴーストがしゃべるスクリプトをまとめて後で置き換える際に使うものです。<br>
語尾を変えてみたり、敬称をつける際にだぶる現象を回避してみたり。

```
_text = REPLACE(_text, "たん殿", "たん")
```

「たん殿」を「たん」に置換しています。<br>
後ろの2つの " " はそれぞれ、置き換え前、置き換え後の言葉です。何に変えてもかまいません。

```
_text = RE_REPLACE(_text,"(ちゃん|くん|さん|殿)殿","殿")
```

「ちゃん殿」「くん殿」「さん殿」「殿殿」とだぶってマズそうなものを置換しています。

## 改造メモ

### 敬称がらみ

ほかにも、たとえば「様殿」もなんとかしたい場合は、

```
(ちゃん|くん|さん|殿)
```

と、括弧でくくって | 区切りにしてある部分に追加して

```
(ちゃん|くん|さん|殿|様)
```

とすると良いでしょうし、また、うちのゴーストでは「殿」を追加するのではなくて「さま」を追加してるんだ！という場合は、

```
_text = RE_REPLACE(_text,"(ちゃん|くん|さん|殿|様|さま)さま","さま")
```

と、こんな感じでしょうか。

### 自動ウエイトもどきがらみ

たとえば

```
_text = REPLACE(_text, "！", "！\w5")
_text = REPLACE(_text, "？", "？\w5")
```

とした場合に、<br>
「！！！」や「？？？」が<br>
！`\w5`！`\w5`！`\w5`　？`\w5`？`\w5`？`\w5`<br>
……に置換されてしまい、なんだか微妙です。

```
_text = RE_REPLACE(_text ,'！(?=[^！\\])', '！\w5')
_text = RE_REPLACE(_text ,'？(?=[^？\\])', '？\w5')
```

ちょっとややこしい正規表現なので解説は控えますが、これで解決できます。

### 自動ウエイト：さらにパーフェクトな方法

上記方法ですとタグ内部などまで置換されてひどい目に遭います。
そのへんを解決した関数を以下に用意しました。

2020/3/29更新 EVAL内部での不要な変数展開を削除

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

使い方は以下のコードを一番上のOnTranslateの中に（自動ウエイト部分を一旦消して）仕込むだけです。

```
 _text = TextOnlyTranslator(_text,'TextOnlyTranslatorFunc')
```

正規表現は、[ukiya:正規表現講座/おまけ１](http://ukiya.sakura.ne.jp/index.php?正規表現講座/おまけ１)を使っています。
