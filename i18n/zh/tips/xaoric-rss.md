# 使用 xaoric.dll 读取 RSS

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

xaoric.dll 发布网站　<https://code.google.com/p/csaori/>

- （补充：SSP2.4.11 支持[execute,rss-get]及与之对应的 SHIORI EVENT，因此即使不使用这个 SAORI，也可以由人格端获取 RSS）

### 读取 NicoNico 动画标签搜索 RSS 的示例

- 仅适用于支持「execute,http-get」和「OnExecuteHTTPComplete」的版本的 SSP。
- 将 xaoric.dll 放在与 yaya.dll 相同的目录中。
- 建议采取措施，尽量减轻服务器负担，例如设置为每小时最多执行一次。

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

「nico_title」中会保存视频标题，「nico_link」中会保存视频 URL，「nico_pubDate」中会保存视频发布时间，「nico_description」中会保存视频说明、缩略图 URL 等组成的数组。
