# YAYA as PLUGIN

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

### 概要

yaya.dllのプラグイン規格対応用辞書セットです。<br>
YAYAの文法でプラグインを作成することができます。SAORIを使用することも可能です。<br>
PLUGIN/2.0のため、ほぼSSP専用プラグインとなります。<br>

### 配布サイト

[整備班 -The Maintenance Shop-](http://ms.shillest.net/yaya_as.xhtml)

### これを利用して作成されたプラグイン

- [きょうの伺か+](http://nikolat.starfree.jp/recghost/)
  - Twitterに起動中の「伺か」のゴーストに関することを気軽に投稿できるSSP専用プラグイン

- [スタンプ帳](http://navy.nm.land.to/post/)
  - ゴーストさんがスタンプを押してくれます（いろいろ条件がある場合も）
  - [対応ゴーストリスト](http://www10.atwiki.jp/postic/pages/13.html)

- [BalloonMaker](http://coderatte.ehoh.net/)
  - バルーンを作れます。

- [updater_yaya](http://home.384.jp/evidence/cgi-bin/archives/10.html)
  - SHIORI, SAORI, PLUGIN, HEADLINE で使用するyaya.dllを一括コピーできます。

- [daumaker](https://github.com/nikolat/daumaker)
  - updates2.dauを作成します。

- [BalloonSelector](https://github.com/nikolat/balloonselector)
  - バルーン選択支援プラグイン。

- [第弐版仮想道頓堀水泳拡張](http://ms.shillest.net/yaya_as.xhtml)
  - バーチャル道頓堀プラグイン。

- [第弐版仮想麦酒飛散拡張](http://ms.shillest.net/yaya_as.xhtml)
  - バーチャルビールかけプラグイン。

- [第弐版仮想実体化拡張](http://ms.shillest.net/yaya_as.xhtml)
  - 実体化？プラグイン。

### プラグイン作成法

#### 「バーチャル道頓堀プラグイン」書き換え例

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

他に何かやらせたい事があればプラグイン仕様書参照

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

#### ほか

- yaya.txtのiolog, offをコメントアウトしログ出力オンにすると、プラグインにどんなイベントが発生するのか把握可能（yaya.txtデフォルト設定ではOnSecondChangeは無視）ゴーストと同じように発生するイベントとしないイベントがあり。
- 里々から`\![raiseplugin]`で値を送るとき「、」や「。」に自動的にウェイトタグが付く場合があり（「φ。」と書いても防げない）
- プラグインエクスプローラーを開き、プラグイン無効→有効でプラグインリロード

#### 参考サイト

- [プラグイン仕様書](http://ssp.shillest.net/ukadoc/manual/spec_plugin.html)
