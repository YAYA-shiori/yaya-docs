# Reading RSS with xaoric.dll

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

xaoric.dll distribution site: <https://code.google.com/p/csaori/>

- (Note: SSP2.4.11 added support for [execute,rss-get] and the corresponding SHIORI EVENT, so the ghost can retrieve RSS without using this SAORI.)

### Example of reading Nico Nico Douga tag-search RSS

- This is for SSP versions that support 「execute,http-get」 and 「OnExecuteHTTPComplete」.
- Place xaoric.dll in the same directory as yaya.dll.
- We recommend taking steps to avoid burdening the server, such as limiting execution to once per hour.

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

The arrays 「nico_title」, 「nico_link」, 「nico_pubDate」, and 「nico_description」 contain video titles, video URLs, video posting times, and video descriptions or thumbnail URLs, respectively.
