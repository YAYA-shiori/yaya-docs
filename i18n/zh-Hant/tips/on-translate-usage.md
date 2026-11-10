# OnTranslate 的使用方法

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) 轉載自 AYAYA Wiki

有人提問，因此我寫了一個簡單的使用範例。

<span style="color:red">aya_aitalk.dic</span>開頭附近的

```
//OnTranslate
//{
//	REPLACE(reference0, "。", "にゅ。")
//}
```

將註解掉而停用的部分替換成以下內容。

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

## 說明

OnTranslate 用於將人格說出的腳本集中起來，之後再進行替換。<br>
例如改變語尾，或避免加上敬稱時出現重複的情況。

```
_text = REPLACE(_text, "たん殿", "たん")
```

這會將「たん殿」替換為「たん」。<br>
後面兩個 " " 分別是替換前和替換後的詞語。替換成什麼都可以。

```
_text = RE_REPLACE(_text,"(ちゃん|くん|さん|殿)殿","殿")
```

這會替換「ちゃん殿」「くん殿」「さん殿」「殿殿」等看起來重複、不太妥當的稱謂。

## 修改備註

### 稱謂相關

此外，例如想處理「様殿」的話，

```
(ちゃん|くん|さん|殿)
```

可以在以括號括起來、用 | 分隔的部分新增項目，

```
(ちゃん|くん|さん|殿|様)
```

另外，如果你的角色不是加上「殿」，而是加上「さま」！

```
_text = RE_REPLACE(_text,"(ちゃん|くん|さん|殿|様|さま)さま","さま")
```

大概可以像這樣處理。

### 自動等待的類似功能

例如

```
_text = REPLACE(_text, "！", "！\w5")
_text = REPLACE(_text, "？", "？\w5")
```

這樣一來，<br>
「！！！」或「？？？」會<br>
被替換成 ！`\w5`！`\w5`！`\w5`　？`\w5`？`\w5`？`\w5`<br>
……結果有點微妙。

```
_text = RE_REPLACE(_text ,'！(?=[^！\\])', '！\w5')
_text = RE_REPLACE(_text ,'？(?=[^？\\])', '？\w5')
```

這是稍微複雜一點的正規表示式，因此就不詳細解說了，不過這樣就能解決問題。

### 自動等待：更完善的方法

使用上述方法時，連標籤內部等部分也會被替換，造成麻煩。
以下提供一個能解決這些問題的函式。

更新於 2020/3/29：移除 EVAL 內部不必要的變數展開

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

使用方法是在最上方的 OnTranslate 中加入以下程式碼（先暫時刪除自動等待的部分）即可。

```
 _text = TextOnlyTranslator(_text,'TextOnlyTranslatorFunc')
```

正規表示式參考了[ukiya：正規表示式講座／附錄１](http://ukiya.sakura.ne.jp/index.php?正規表現講座/おまけ１)。
