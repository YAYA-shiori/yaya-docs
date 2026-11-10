# YAYA as PLUGIN

> Reposted from [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### Overview

A dictionary set for using yaya.dll with the plugin specification.<br>
You can create plugins using YAYA syntax. You can also use SAORI.<br>
Because it uses PLUGIN/2.0, it is almost exclusively for SSP plugins.<br>

### Distribution site

[The Maintenance Shop](http://ms.shillest.net/yaya_as.xhtml)

### Plugins created using this

- [Today's Ukagaka+](http://nikolat.starfree.jp/recghost/)
  - An SSP-only plugin for easily posting to Twitter about the ghosts of “Ukagaka” currently running

- [Stamp Book](http://navy.nm.land.to/post/)
  - Ghosts will stamp your book (sometimes subject to various conditions)
  - [List of compatible ghosts](http://www10.atwiki.jp/postic/pages/13.html)

- [BalloonMaker](http://coderatte.ehoh.net/)
  - Create balloons.

- [updater_yaya](http://home.384.jp/evidence/cgi-bin/archives/10.html)
  - Copies yaya.dll for use with SHIORI, SAORI, PLUGIN, and HEADLINE all at once.

- [daumaker](https://github.com/nikolat/daumaker)
  - Creates updates2.dau.

- [BalloonSelector](https://github.com/nikolat/balloonselector)
  - A plugin that helps you select balloons.

- [Virtual Dotonbori Swimming Extension, Second Edition](http://ms.shillest.net/yaya_as.xhtml)
  - A virtual Dotonbori plugin.

- [Virtual Beer-Splashing Extension, Second Edition](http://ms.shillest.net/yaya_as.xhtml)
  - A virtual beer-splashing plugin.

- [Virtual Materialization Extension, Second Edition](http://ms.shillest.net/yaya_as.xhtml)
  - A materialization? plugin.

### How to create a plugin

#### Example: editing the “Virtual Dotonbori Plugin”

- yaya_plugin_main.txt

```
//↓プラグインメニュー（SSP＞オーナードローメニュー＞プラグイン＞【このプラグインの名前】）をクリックすると発生するイベント
OnMenuExec
{
	//★↓ここに発生させたいイベント名を書く
	res_event = 'OnDive'

	//★↓ここに発生させたいイベント中で返すReferenceを書く
	//省略可。Reference1以降も同じように記述可。0から昇順に並べること。
	res_reference[0] = '道頓堀'

	//★↓ここでスクリプトやイベントを送るゴーストのSakura名を指定
	//「__SYSTEM_ALL_GHOST__」で全起動中ゴースト
	//省略するとプラグインメニューを実行したゴースト
	//res_target = '__SYSTEM_ALL_GHOST__'

	//★↓ここでバルーンのマーカー(下に小さく出るステータス表示)に表示する文字を指定
	res_marker = 'バーチャル道頓堀プラグイン'
	
	//★↓ここにres_targetで指定したゴーストに喋らせるトークやさくらスクリプトを書く
	'\h\s[5]どぼ～ん。\w9\w9\u\s[11]…\w5…\w5…\w5…\w5…。\e'
}

//プラグインのバージョン
version
{
	'Tombori/1.1'
}
```

For anything else you want it to do, see the plugin specification.

- descript.txt

```
//文字コード
Charset,Shift_JIS

//名前　（★絶対変更する）
name,バーチャル道頓堀

//作者　（★絶対変更する）
//craftmanwは日本語も可、craftmanは英語のみ。どっちか片方でもOK
craftman,SSP BUGTRAQ
//craftmanw

//PLUGIN DLL
filename,yaya.dll

//オプション指定-OnSecondChangeの通知頻度
//0で無効、標準1
secondchangeinterval,0

//プラグインID　（★絶対変更する）
//http://www.famkruithof.net/uuid/uuidgen とかで生成できます
//一度書いたら変えないこと
id,CBC695FA-4395-48d0-8ADB-0DBCE19BF34E

//更新URL　（★絶対変更する、使わないなら削除）
homeurl,http://ms.shillest.net/plugin/tombori/
```

- install.txt

```
type,plugin
//プラグイン名　（★絶対変更する）
name,バーチャル道頓堀
//インストールディレクトリ名　（★絶対変更する）
directory,TOMBORI
```

#### Other

- In yaya.txt, comment out iolog, off and enable logging to see which events are triggered for the plugin (with the default yaya.txt settings, OnSecondChange is ignored); as with ghosts, some events are triggered and others are not.
- When sending values from Satori using `\![raiseplugin]`, a wait tag may be added automatically after “、” or “。” (writing “φ。” does not prevent this).
- Open Plugin Explorer, then disable and re-enable the plugin to reload it.

#### Reference

- [Plugin Specification](http://ssp.shillest.net/ukadoc/manual/spec_plugin.html)
