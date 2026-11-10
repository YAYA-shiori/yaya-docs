# 從錨點標籤跳轉至 URL

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

[將選項直接寫成獨立函式](independent-choice-function.md)的＋α。<br>
IDが<http://～で始まっているとそのURLにジャンプ。><br>
加入這段程式碼後，顯示 RSS 時也可以點擊文章標題跳轉至 URL。

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

### 錨點標籤的寫法

```
\_a[URL]文字列\_a/
```

### 使用範例

```
sample { 	
	"\1\s[10]\0\s[0]/
	文Wikiを開きます。\n\n/
	\_a[http://emily.shillest.net/ayaya/?FrontPage]ここをクリック\_a/
	\e"
}
```

加入「`\C`」後，即可在對話方塊維持原本顯示狀態的情況下跳轉至 URL（僅限 SSP）<br>
在 SSP 以外的 baseware 上，應該會先顯示空白的對話方塊，再跳轉至 URL。<br>
順帶一提，選項的 ID 若是 URL，依照規格，即使不做任何處理也會在瀏覽器中開啟該 URL。

### 與工具提示併用

若同時使用[工具提示](tooltip.md)頁面的「顯示跳轉目的地 URL」，就能事先確認要前往哪個 URL，使用上也更方便。
