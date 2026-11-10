# 工具提示

> 转载自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

在Windows中，指针下方适时显示的小型说明窗口。（[参考图片](http://f.hatena.ne.jp/ponapalt/20090127221447)）<br>
使用「`\n`」换行。<br>
顺带一提，外壳的命中区域工具提示由[surfaces.txt指定](http://ghost-dev.g.hatena.ne.jp/ponapalt/20090101)。

会显示在外壳上。<br>
仅支持SSP2.1.58及更高版本。

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

※转载自[にこらとてすらの反省会](http://home.384.jp/evidence/cgi-bin/archives/15.html)。

## 对话框工具提示

显示在对话框的选项上方。<br>
仅支持SSP2.1.62及更高版本。<br>
此外，如果使用AYA5系模板，或者SHIORI3FW.REF_ACCEL设置为1，则将`reference[*]`改为reference\*。

### 根据选项ID进行判断时

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

### 根据选项标签进行判断时

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

（注：如果选项ID（下例中的标签）中含有不能用于函数名的符号（空格　!　"　#　$　%　&　(　)　\*　+　,　-　/　:　;　<　=　>　?　@　[　]　`　{　|　}　~），就不能使用这种方法。<br>
如果确实必须使用，请删除reference中对应的符号，或将其转换为全角字符等。）

### 显示跳转目标URL

让用户提前了解将要跳转到哪个URL。<br>
请与[从锚点标签跳转URL](url-jump-from-anchor.md)配合使用。

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
