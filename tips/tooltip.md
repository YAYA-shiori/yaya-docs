# ツールチップ

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

Windowsにおいて、マウスポインタの下に適宜表示される小さな説明窓のこと。（[参考画像](http://f.hatena.ne.jp/ponapalt/20090127221447)）<br>
改行は「`\n`」で行う。<br>
ちなみにシェルの辺り判定ツールチップは[surfaces.txtで指定する](http://ghost-dev.g.hatena.ne.jp/ponapalt/20090101)。

シェルの上に表示されます。<br>
SSP2.1.58以降のみ対応。

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

※[にこらとてすらの反省会](http://home.384.jp/evidence/cgi-bin/archives/15.html)より転載させていただきました。

## バルーンツールチップ

バルーンの選択肢の上に表示されます。<br>
SSP2.1.62以降のみ対応。<br>
こちらもAYA5系テンプレート、またはSHIORI3FW.REF_ACCEL設定が1の場合は`reference[*]`をreference\*に。

### 選択肢IDで判別する場合

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

### 選択肢ラベルで判別する場合

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

（注：選択肢ID（下の例ではラベル）に関数名に使えない記号（空白　!　"　#　$　%　&　(　)　\*　+　,　-　/　:　;　&lt;　=　>　?　@　[　]　`　{　|　}　~ ）が混じっているとこの方法は使えません。<br>
どうしても使わないといけない場合はreference内該当記号を削除する、全角に変換するなどして対処してください）

### ジャンプ先URLを表示

どのURLに飛ぶのか事前にわかりやすくする。<br>
[アンカータグからURLジャンプ](url-jump-from-anchor.md)と併用して使ってください。

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
