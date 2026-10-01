# xaoric.dllを使ったRSS読み取り

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

xaoric.dll配布サイト　<https://code.google.com/p/csaori/>

- (追記 SSP2.4.11では[execute,rss-get]およびそれに対応したSHIORI EVENTがサポートされたので、このSAORIを使わなくてもゴースト側でRSSの取得は可能)

### ニコニコ動画タグ検索RSSの読み取り例

- 「execute,http-get」「OnExecuteHTTPComplete」に対応したバージョンのSSP専用です。
- xaoric.dllをyaya.dllと同じ階層に置いています。
- なるべくサーバーに負担がかからないよう、例えば一時間に一度だけ実行できるようにする等の工夫を行うのを推奨します。

```
XaoricSample
{
	"\0\s[0]ニコニコ動画内「ゲーム実況」タグ動画を新着順に取得。"
	--
	//「execute,http-get」を使いRSSをダウンロードし、「var」フォルダ内に「TempRSS」というファイル名で保存
	"\C\![execute,http-get,http://www.nicovideo.jp/tag/%E3%82%B2%E3%83%BC%E3%83%A0%E5%AE%9F%E6%B3%81?sort=f&rss=2.0,--async=NiconicoRSSCheck,--file=TempRSS,--timeout=30]\e"
}

//http-get取得成功
OnExecuteHTTPComplete{
	_id = reference[1]
	//「--async=」で指定したイベント名へ飛ばす
	if ISFUNC(_id) {
		EVAL(_id)
	}
}

//http-get取得失敗
OnExecuteHTTPFailure {
	"\0\s[0]execute-http取得エラー。\e"
}

NiconicoRSSCheck
{
	//「var」フォルダ内「TempRSS」の絶対パスを取得
	_Path=GETSETTING("coreinfo.path")+'var\TempRSS'

	//xaoric.dllで「TempRSS」を開く
	_FileID = FUNCTIONEX('xaoric.dll' , 'open' , _Path)

	//動画情報を配列変数として保存
	nico_title = SPLIT(FUNCTIONEX('xaoric.dll' , 'get' , _FileID , '/rss/channel/item/title'),CHR(1))
	nico_link = SPLIT(FUNCTIONEX('xaoric.dll' , 'get' , _FileID , '/rss/channel/item/link'),CHR(1))
	nico_pubDate = SPLIT(FUNCTIONEX('xaoric.dll' , 'get' , _FileID , '/rss/channel/item/pubDate'),CHR(1))
	nico_description = SPLIT(FUNCTIONEX('xaoric.dll' , 'get' , _FileID , '/rss/channel/item/description'),CHR(1))

	//xaoric.dllを終了させる
	_ret = SPLIT(FUNCTIONEX('xaoric.dll' , 'close' , _FileID),CHR(1))

	"\0\s[0]ニコニコ動画内「ゲーム実況」タグ動画を新着順に取得成功。\e"
}
```

「nico_title」に動画タイトル、「nico_link」に動画URL、「nico_pubDate」に動画投稿時刻、「nico_description」に動画説明文やサムネイルURL等の配列が入ります。
