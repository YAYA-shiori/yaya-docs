# Jump to a URL from an anchor tag

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

This is an add-on to [Writing choices directly as independent functions](independent-choice-function.md).<br>
If the ID starts with <http://～で始まっているとそのURLにジャンプ。><br>
With this in place, clicking an article title also jumps to its URL when displaying an RSS feed.

### Basics

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

### Writing an Anchor Tag

```
\_a[URL]文字列\_a/
```

### Example

```
sample { 	
	"\1\s[10]\0\s[0]/
	文Wikiを開きます。\n\n/
	\_a[http://emily.shillest.net/ayaya/?FrontPage]ここをクリック\_a/
	\e"
}
```

By adding 「`\C`」, you can jump to a URL while keeping the balloon display as it is (SSP only).<br>
On baseware other than SSP, it should jump to the URL after displaying an empty balloon.<br>
For choices, the specification is that if the ID is a URL, the URL opens in a browser without any additional action on your part.

### Using with Tooltips

Using this together with “Show destination URL” on the [Tooltip](tooltip.md) page makes it easier and more helpful for users to see in advance which URL they will be taken to.
