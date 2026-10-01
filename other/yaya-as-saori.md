# YAYA as SAORI

> [AYAYA Wiki](https://emily.shillest.net/ayayaold/) より転載

### 概要

摂理氏作、yaya.dllをSAORIとして呼び出すモジュールです。<br>
YAYA以外のSHIORIからYAYAの機能を使う事が可能になります。

デフォルトの状態ではYAYAのビルトイン（システム）関数のみ利用できます。<br>
追加モジュールを導入することにより更に用途が広がります。YAYAの文法がわかる人はこの追加モジュールを自分で作成することができます。<br>

### ダウンロード

- ~~[yaya_as_saori_2021_10_08.zip](../attachment/yaya_as_saori_2021_10_08.zip)~~
- [Releases · YAYA-shiori/yaya-as-saori · GitHub](https://github.com/YAYA-shiori/yaya-as-saori/releases)

### 追加モジュール

- [jsonパーサ with オブジェクト風の何か](http://c-lege.hacca.jp/ukgk/ukst.html)
  - jsonをjavascriptのオブジェクト風に読み込み、要素の取り出し等の操作が行えるモジュール。
- [calendae](http://gallnuts.webcrow.jp/dump.shtml)
  - 暦に関する計算機能モジュール。
- [sub-edittext](http://gallnuts.webcrow.jp/dump.shtml)
  - テキストファイルの編集機能モジュール。
- [ssu.aym](http://rabbitbike.oh.land.to/nicky/log200803.html)
  - ssu（里々同梱SAORI）と同じ動作をさせる。
- [Reta](http://navy.nm.land.to/post/)
  - テキストファイルやインストールされてるゴーストのシェル名、文/里々/華和梨/美坂のセーブデータを読み取る。

### 解説サイト

- [SAORI/YAYA - 里々Wiki](http://soliton.sub.jp/satori/index.php?SAORI%2FYAYA)
  - 里々から利用する方法の解説。
- [AYA as SAORI里々向け簡易解説](http://navy.nm.land.to/post/a_a_s.html)
  - AYA as SAORIの方の解説ですがYAYA as SAORIでも利用可能（ただしYAYAから追加された関数は無し）

### デモゴースト

- [紺野さやめ](http://navy.nm.land.to/post/)
  - 里々用デモゴースト。同梱されているSAORIのバージョンが古いため、入れ替え推奨。

### モジュールの自作

- 通常の辞書と同じように、[yaya.txt](../grammar/01-basic-settings.md)に追記することで自由に追加できます。<br>慣習上「.aym」という拡張子（※aya moduleの略）にする事が多いですが、それ以外であっても動作に影響はありません。
- SAORIの引数は、モジュール内で`REQ.ARGS[*]`という配列に格納されています。<br>Argument0は`REQ.ARGS[0]`で、それ以降も同様です。
- SAORIの戻り値は、モジュール内でRES.RESULTおよび`RES.VALUE*`という変数に代入する事で返却します。<br>単数戻り値ResultはRES.RESULTに、複数戻り値Value\*はそれぞれ一つずつ`RES.VALUE*`に返却します。<br>`RES.VALUE*`は**配列ではない**事に注意してください。代入にはシステム関数[EVAL](../functions/EVAL.md)が便利であるかもしれません。
- もし引数が不正等の理由から、SAORIとしての機能が正常に実行出来なかった場合には、関数の戻り値として（SAORI戻り値ではなく）数値-1を返却します。<br>YAYA as SAORIシステム部が戻り値として-1を受け取ると、不正な呼び出しとしてエラーを通知します。<br>この時、YAYAのシステム関数[LOGGING](../functions/LOGGING.md)を利用して、エラーが発生したSAORI関数名とエラーの説明をログに残す事が推奨されます。
- 関数名は自由に設定して構いませんが、「モジュール名.関数名」といった組成にすることには少なくとも二つ意味があります。
  - 一つは、そうした組成の関数名について、YAYA as SAORIはモジュールのロード・アンロード用の仕組みを提供していることです。<br>モジュール名.関数名というピリオドを含む関数名が呼び出された時、YAYA as SAORIはモジュール名の部分を記憶します。<br>そして、同一のモジュール名を持つ関数が始めて呼ばれたときに、**モジュール名.Load**という関数がないかを探し、あれば実行します。<br>また、yaya.dllがアンロードされるとき、**モジュール名.Unload**という関数がないかを探し、あれば実行します。<br>モジュール全体にわたって共通のグローバル変数を利用するような場合には、初期化・後始末にこうした仕組みを利用できるでしょう。
  - もう一つは、このようにモジュール名を関数名の前に冠しておくことで、いくらか関数名が重複しにくくなることです。<br>モジュールは異なる複数人が作成した物が共存することがありますし、当然一人で複数のモジュールを個別に作ることもあります。<br>そうした場合を想定してこのように命名しておけば、関数名が重複するリスクをある程度低めることができるでしょう。

## 添付ファイル

- [yaya_as_saori_2014_01_04.zip](../attachment/yaya_as_saori_2014_01_04.zip)
- [yaya_as_saori_2014_11_08.zip](../attachment/yaya_as_saori_2014_11_08.zip)
- [yaya_as_saori_2014_11_08b.zip](../attachment/yaya_as_saori_2014_11_08b.zip)
- [yaya_as_saori_2015_12_30.zip](../attachment/yaya_as_saori_2015_12_30.zip)
- [yaya_as_saori_2021_06_14-2.zip](../attachment/yaya_as_saori_2021_06_14-2.zip)
- [yaya_as_saori_2021_06_14.zip](../attachment/yaya_as_saori_2021_06_14.zip)
- [yaya_as_saori_2021_06_17.zip](../attachment/yaya_as_saori_2021_06_17.zip)
- [yaya_as_saori_2021_06_24-2.zip](../attachment/yaya_as_saori_2021_06_24-2.zip)
- [yaya_as_saori_2021_06_24.zip](../attachment/yaya_as_saori_2021_06_24.zip)
- [yaya_as_saori_2021_06_25.zip](../attachment/yaya_as_saori_2021_06_25.zip)
- [yaya_as_saori_2021_06_28.zip](../attachment/yaya_as_saori_2021_06_28.zip)
- [yaya_as_saori_2021_06_30.zip](../attachment/yaya_as_saori_2021_06_30.zip)
- [yaya_as_saori_2021_07_10.zip](../attachment/yaya_as_saori_2021_07_10.zip)
- [yaya_as_saori_2021_07_11-2.zip](../attachment/yaya_as_saori_2021_07_11-2.zip)
- [yaya_as_saori_2021_07_11.zip](../attachment/yaya_as_saori_2021_07_11.zip)
- [yaya_as_saori_2021_07_16.zip](../attachment/yaya_as_saori_2021_07_16.zip)
- [yaya_as_saori_2021_08_31.zip](../attachment/yaya_as_saori_2021_08_31.zip)
- [yaya_as_saori_2021_10_08.zip](../attachment/yaya_as_saori_2021_10_08.zip)
