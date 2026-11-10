# 从锚点标签跳转到 URL

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

[直接将选项写成独立函数](independent-choice-function.md)的补充。<br>
ID若以<http://～で始まっているとそのURLにジャンプ。>开头，就会跳转到该 URL。<br>
添加这段代码后，在显示 RSS 时点击文章标题也可以跳转到 URL。

### 基础

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

### 锚点标签的写法

```
\_a[URL]文字列\_a/
```

### 使用示例

```
sample { 	
	"\1\s[10]\0\s[0]/
	文Wikiを開きます。\n\n/
	\_a[http://emily.shillest.net/ayaya/?FrontPage]ここをクリック\_a/
	\e"
}
```

添加「`\C`」后，可以在保持对话框显示原样的状态下跳转到 URL（仅限 SSP）。<br>
在 SSP 以外的 baseware 上，应该会先显示空白对话框，再跳转到 URL。<br>
另外，对于选项，即使不做任何处理，按照规格，只要 ID 是 URL，就会在浏览器中打开该 URL。

### 与工具提示配合使用

配合[工具提示](tooltip.md)页面中的“显示跳转目标 URL”，可以事先了解将要跳转到哪个 URL，更加方便。
