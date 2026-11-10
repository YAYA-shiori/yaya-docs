# Tooltip

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

A small explanatory window that is displayed as appropriate under the mouse pointer in Windows. ([Reference image](http://f.hatena.ne.jp/ponapalt/20090127221447))<br>
Use「`\n`」to insert a line break.<br>
Incidentally, shell hit-test tooltips are [specified in surfaces.txt](http://ghost-dev.g.hatena.ne.jp/ponapalt/20090101).

Displayed above the shell.<br>
Supported only in SSP 2.1.58 and later.

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

※ Reposted from [Nicol and Tesla's Review Meeting](http://home.384.jp/evidence/cgi-bin/archives/15.html).

## Balloon Tooltips

Displayed above balloon choices.<br>
Supported only in SSP 2.1.62 and later.<br>
For AYA5-series templates or when SHIORI3FW.REF_ACCEL is set to 1, change `reference[*]` to reference\* here as well.

### Identify by choice ID

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

### Identify by choice label

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

(Note: This method cannot be used if the choice ID (the label in the example below) contains symbols that cannot be used in function names (space　!　"　#　$　%　&　(　)　\*　+　,　-　/　:　;　<　=　>　?　@　[　]　`　{　|　}　~).<br>
If you need to use such symbols, work around this by removing the relevant symbols from reference or converting them to full-width characters.)

### Display the destination URL

Make it easy to see in advance which URL will be opened.<br>
Use this together with [Jump to a URL from an anchor tag](url-jump-from-anchor.md).

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
