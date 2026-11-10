# 工具提示

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

在 Windows 中，會依情況顯示於滑鼠游標下方的小型說明視窗。（[參考圖片](http://f.hatena.ne.jp/ponapalt/20090127221447)）<br>
使用「`\n`」換行。<br>
另外，外殼的碰撞判定工具提示請在[surfaces.txt 中指定](http://ghost-dev.g.hatena.ne.jp/ponapalt/20090101)。

會顯示在外殼上。<br>
僅 SSP2.1.58 以後的版本支援。

```
// YAYA/Tc533-2 + yaya_shiori3.dic
// AYA5系テンプレートの場合はreference[*]をreference*に変えること

On_tooltip
{
  AYATEMPLATE.MouseEventExec('tooltip')
}
// 「tooltip[キャラクター番号][当たり判定の識別子]」にツールチップで表示させるテキストを記述
// 当たり判定のない箇所は「tooltip[キャラクター番号]」
tooltip0Bust
{
  'ここにテキスト'
}
tooltip1Bust
{
  'ここにテキスト'
}
// 「はろーYAYAわーるど」yaya_tmpl_util.txtに記述済み
// 既に辞書にない場合こちらも一緒に記述
AYATEMPLATE.MouseEventExec
{
  _fname = _argv[0] + TOSTR(reference[3]) + TOSTR(reference[4])
  if ISFUNC(_fname) {
    EVAL(_fname)
    return
  }

  _fname = _argv[0] + TOSTR(reference[3])
  if ISFUNC(_fname) {
    EVAL(_fname)
    return
  }
}
```

※轉載自[にこらとてすらの反省会](http://home.384.jp/evidence/cgi-bin/archives/15.html)。

## 對話方塊工具提示

會顯示在對話方塊的選項上方。<br>
僅 SSP2.1.62 以後的版本支援。<br>
若使用 AYA5 系範本，或 SHIORI3FW.REF_ACCEL 設定為 1，也請將 `reference[*]` 改為 reference\*。

### 依選項 ID 判斷時

```
menu {
　"\1\s[10]\0\s[0]/
　\q[何か話して,Talking]\n/
　\q[自己紹介,Profile]\n/
　\q[閉じる,CloseBalloon]\n/
　\e"
}

On_balloon_tooltip {
　if ISFUNC( "BalloonTooltip_%(reference[1])" ) {
　	EVAL( "BalloonTooltip_%(reference[1])" )
　}
}

// 「BalloonTooltip_[選択肢ID]」にツールチップで表示させるテキストを記述
BalloonTooltip_Talking { "お話します" }
BalloonTooltip_Profile { "わたしのこと" }
BalloonTooltip_CloseBalloon { "バルーンを閉じます\n（放置しても閉じます）" }
```

### 依選項標籤判斷時

```
menu {
　"\1\s[10]\0\s[0]/
　\q[何か話して,Talking]\n/
　\q[自己紹介,Profile]\n/
　\q[閉じる,CloseBalloon]\n/
　\e"
}

On_balloon_tooltip {
　if ISFUNC( "BalloonTooltip_%(reference[0])" ) {
　	EVAL( "BalloonTooltip_%(reference[0])" )
　}
}

// 「BalloonTooltip_[選択肢ラベル]」にツールチップで表示させるテキストを記述
BalloonTooltip_何か話して { "お話します" }
BalloonTooltip_自己紹介 { "わたしのこと" }
BalloonTooltip_閉じる { "バルーンを閉じます\n（放置しても閉じます）" }
```

（注意：選項 ID（下方範例中的標籤）若包含無法用於函式名稱的符號（空白　!　"　#　$　%　&　(　)　\*　+　,　-　/　:　;　<　=　>　?　@　[　]　`　{　|　}　~），就無法使用這個方法。<br>
如果一定得使用這些符號，請刪除 reference 中對應的符號，或將它們轉換成全形字元等方式處理）

### 顯示跳轉目標 URL

讓使用者事先清楚知道將跳轉至哪個 URL。<br>
請搭配[從錨點標籤跳轉至 URL](url-jump-from-anchor.md)使用。

```
On_balloon_tooltip {
　if ISFUNC( "BalloonTooltip_%(reference[0])" ) {
　	EVAL( "BalloonTooltip_%(reference[0])" )
　}
  else {
	if RE_MATCH( reference[0], 'http://.+' ) {
		"以下のURLをブラウザで開きます\n%(reference[0])"
	}
}
```
