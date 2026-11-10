# YAYA as PLUGIN

> 轉載自 [AYAYA Wiki](https://emily.shillest.net/ayayaold/)

### 概要

這是一組用於讓 yaya.dll 支援外掛規格的辭典。<br>
可以使用 YAYA 語法製作外掛，也可以使用 SAORI。<br>
由於採用 PLUGIN/2.0，因此幾乎是 SSP 專用外掛。<br>

### 發布網站

[整備班 -The Maintenance Shop-](http://ms.shillest.net/yaya_as.xhtml)

### 使用此模組製作的外掛

- [今日伺か+](http://nikolat.starfree.jp/recghost/)
  - 可將與目前正在執行的「伺か」人格相關的內容，輕鬆發布到 Twitter 的 SSP 專用外掛

- [集章簿](http://navy.nm.land.to/post/)
  - 人格會幫你蓋章（有時也會有各種條件）
  - [支援人格清單](http://www10.atwiki.jp/postic/pages/13.html)

- [BalloonMaker](http://coderatte.ehoh.net/)
  - 可以製作對話方塊。

- [updater_yaya](http://home.384.jp/evidence/cgi-bin/archives/10.html)
  - 可以一次複製 SHIORI、SAORI、PLUGIN、HEADLINE 使用的 yaya.dll。

- [daumaker](https://github.com/nikolat/daumaker)
  - 建立 updates2.dau。

- [BalloonSelector](https://github.com/nikolat/balloonselector)
  - 協助選擇對話方塊的外掛。

- [第二版虛擬道頓堀游泳擴充](http://ms.shillest.net/yaya_as.xhtml)
  - 虛擬道頓堀外掛。

- [第二版虛擬啤酒潑灑擴充](http://ms.shillest.net/yaya_as.xhtml)
  - 虛擬潑啤酒外掛。

- [第二版虛擬實體化擴充](http://ms.shillest.net/yaya_as.xhtml)
  - 實體化？外掛。

### 外掛製作方法

#### 「虛擬道頓堀外掛」修改範例

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

如果還想讓外掛執行其他操作，請參閱外掛規格文件

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

- 在 yaya.txt 中將 iolog, off 註解掉並開啟日誌輸出，就能掌握外掛會收到哪些事件（yaya.txt 的預設設定會忽略 OnSecondChange）。有些事件會像人格一樣發生，有些則不會。
- 從 Satori 使用 `\![raiseplugin]` 傳送值時，「、」或「。」有時會自動加上等待標籤（即使寫成「φ。」也無法避免）
- 開啟外掛瀏覽器，將外掛停用再啟用，即可重新載入外掛

#### 參考網站

- [外掛規格文件](http://ssp.shillest.net/ukadoc/manual/spec_plugin.html)
