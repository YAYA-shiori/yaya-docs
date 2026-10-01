# アンカータグからURLジャンプ

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

[選択肢をいきなり独立した関数で書く](independent-choice-function.md)の＋α。<br>
IDが<http://～で始まっているとそのURLにジャンプ。><br>
これを入れておくとRSS表示時も記事タイトルクリックでURLジャンプできます。

### 基礎

```
OnAnchorSelect
{
	_id = reference[0]
	// アンカーのIDの冒頭に「http://～」があればWebサイトを開く。
	if RE_MATCH(_id, 'http://.+') {
		_url = AYATEMPLATE.EscapeText(_id)
		"\C\j[%(_url)] \e"
	// それ以外はIDと同じ名前のイベントへジャンプ
	} elseif ISFUNC(_id) {
		EVAL(_id)
	}
}

OnAnchorSelectEx
{
	_id = reference[1]
	// アンカーのIDの冒頭に「http://～」があればWebサイトを開く。
	if RE_MATCH(_id, 'http://.+') {
		_url = AYATEMPLATE.EscapeText(_id)
		"\C\j[%(_url)] \e"
	// それ以外はIDと同じ名前のイベントへジャンプ
	} elseif ISFUNC(_id) {
		EVAL(_id)
	}
}

// 「[[はろーYAYAわーるど>http://ms.shillest.net/yayame.xhtml]]」にあるエスケープ関数。
// 辞書になければこちらも記述。
AYATEMPLATE.EscapeText
{
	_r = _argv[0]
	if RE_SEARCH(_r,'[,"\[\]]') {
		'"' + REPLACE(_r,'"','""') + '"'
	}
	else {
		_r
	}
}
```

### アンカータグの書き方

```
\_a[URL]文字列\_a/
```

### 使用例

```
sample { 	
	"\1\s[10]\0\s[0]/
	文Wikiを開きます。\n\n/
	\_a[http://emily.shillest.net/ayaya/?FrontPage]ここをクリック\_a/
	\e"
}
```

「`\C`」を入れる事によりバルーンの表示そのままの状態でURLジャンプができる（SSPのみ）<br>
SSP以外のベースウェアでは空白のバルーンを表示した上でURLジャンプするはず。<br>
ちなみに選択肢の場合はこちらで何もしなくても仕様上IDがURLだとそのURLをブラウザで開く。

### ツールチップと併用

[ツールチップ](tooltip.md)ページの「ジャンプ先URLを表示」を併用すると、どのURLに飛ぶのか事前にわかりやすくなり親切です。
