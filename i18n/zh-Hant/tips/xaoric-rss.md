# 使用 xaoric.dll 讀取 RSS

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

xaoric.dll 發佈網站　<https://code.google.com/p/csaori/>

- （補充：SSP2.4.11 已支援 [execute,rss-get] 及對應的 SHIORI EVENT，因此即使不使用此 SAORI，也可以由人格端取得 RSS）

### 讀取 NicoNico 動畫標籤搜尋 RSS 範例

- 僅適用於支援「execute,http-get」和「OnExecuteHTTPComplete」的 SSP 版本。
- 將 xaoric.dll 放在與 yaya.dll 相同的目錄中。
- 建議採取一些措施，避免對伺服器造成過多負擔，例如限制為每小時執行一次。

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

「nico_title」會存放影片標題、「nico_link」會存放影片 URL、「nico_pubDate」會存放影片投稿時間，而「nico_description」會存放影片說明文字、縮圖 URL 等資訊的陣列。
