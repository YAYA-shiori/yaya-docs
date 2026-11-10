# YAYA 作为插件

> 转自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### 概要

这是用于让 yaya.dll 支持插件规范的词典集。<br>
可以使用 YAYA 语法创建插件。也可以使用 SAORI。<br>
由于采用 PLUGIN/2.0，因此几乎是 SSP 专用插件。<br>

### 发布网站

[整备班 -The Maintenance Shop-](http://ms.shillest.net/yaya_as.xhtml)

### 使用此工具创建的插件

- [今日伺か+](http://nikolat.starfree.jp/recghost/)
  - 这是 SSP 专用插件，可轻松将有关正在运行的「伺か」人格的内容发布到 Twitter

- [印章簿](http://navy.nm.land.to/post/)
  - 人格会为你盖印章（有时也会有各种条件）
  - [兼容人格列表](http://www10.atwiki.jp/postic/pages/13.html)

- [BalloonMaker](http://coderatte.ehoh.net/)
  - 可以制作对话框。

- [updater_yaya](http://home.384.jp/evidence/cgi-bin/archives/10.html)
  - 可以批量复制 SHIORI、SAORI、PLUGIN、HEADLINE 使用的 yaya.dll。

- [daumaker](https://github.com/nikolat/daumaker)
  - 创建 updates2.dau。

- [BalloonSelector](https://github.com/nikolat/balloonselector)
  - 对话框选择辅助插件。

- [第二版虚拟道顿堀游泳扩展](http://ms.shillest.net/yaya_as.xhtml)
  - 虚拟道顿堀插件。

- [第二版虚拟啤酒飞溅扩展](http://ms.shillest.net/yaya_as.xhtml)
  - 虚拟泼啤酒插件。

- [第二版虚拟实体化扩展](http://ms.shillest.net/yaya_as.xhtml)
  - 实体化？插件。

### 插件的创建方法

#### 「虚拟道顿堀插件」改写示例

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

如果还想让插件做其他事情，请参阅插件规范说明书

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

#### 其他

- 将 yaya.txt 中的 iolog, off 注释掉并开启日志输出，就可以了解插件会收到哪些事件（yaya.txt 的默认设置会忽略 OnSecondChange）；和人格一样，有些事件会触发，有些则不会。
- 从 Satori 使用 `\![raiseplugin]` 发送值时，「、」或「。」有时会自动附加等待标签（即使写成「φ。」也无法避免）
- 打开插件资源管理器，将插件设为禁用后再启用，即可重新加载插件

#### 参考网站

- [插件规范说明书](http://ssp.shillest.net/ukadoc/manual/spec_plugin.html)
