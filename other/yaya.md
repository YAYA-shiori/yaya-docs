# YAYAについて

## YAYA、AYAとは

- 「やや」と読みます。文字列処理を行うための DLL です。
- ゴースト（デスクトップにキャラクターを立たせるソフト、[SSP](http://ssp.shillest.net/) などのベースウェアの上で動くキャラクターのこと）の頭脳をつかさどる、SHIORI（栞、しおり）と呼ばれる基本部分の一種です。
- SHIORI には他に、[里々](https://ukatech.shillest.net/satori-docs/)、[華和梨](https://ukatech.shillest.net/kawari-docs/)、結奈などがあります。
- 里々から移りたい方は [里々からの移行](../startup/migration-from-satolili.md) をどうぞ。

## コンセプト

- C 言語に似た記述が特徴です。プログラムをかじった人なら、すんなり入っていけるかもしれません。
- プログラミングをしたことがない方にも使ってもらえるよう、このマニュアルには [基本](../INDEX.md#基本-basic) も用意しています。
- 汎用言語として作られているので、用途は SHIORI だけに限られません。SHIORI 以外の使い方は、次のページを参照してください。
  - [SAORIとしてのYAYA](yaya-as-saori.md)
  - [MAKOTOとしてのYAYA](yaya-as-makoto.md)
  - [プラグインとしてのYAYA](yaya-as-plugin.md)
- システム辞書を入れ替えて、SAORI としての利用もされています。
- ゴースト以外にも、汎用の文字列処理用の組み込み言語として使うことも、不可能ではありません。汎用言語 DLL としての YAYA については、[WindowsDLLとしてのYAYA](../grammar/10-yaya-as-windows-dll.md) を参照してください。
- 配布しているバイナリは Windows 用の `yaya.dll` です。ソースは Linux・FreeBSD・macOS でもビルドでき、動作の確認も行っています（配布しているのは Windows 版だけです）。もし動かないところを見つけたら、教えてください。

## 「汎用言語として作られている」とは

- `yaya.dll` 単体では、SHIORI として利用するための機能を全く持っていません。DLL の形式が SHIORI 規格に沿っているだけの、汎用言語 DLL です。
- そのため、「システム辞書」と呼ばれる一連の YAYA スクリプトファイルを使って、SHIORI としての動作をさせています。
- このマニュアルの [文法](../INDEX.md#文法-grammar) や [システム関数](../INDEX.md#システム関数組み込み関数-functions) は、汎用言語としての YAYA を解説しています。SHIORI としての動作は、[システム辞書](../INDEX.md#システム辞書-system) のページで解説しています。
- そのため、「ゴーストの SHIORI として利用する」場合の参考としてマニュアルの文法を見ると、違和感を感じるかもしれません（「request 関数なんてないよ！」「On〜 イベントの呼び出しはいつ行われるの？」）。
- 「ゴーストの SHIORI としての YAYA」を深く理解したいときは、[yaya_shiori3.dic](../system/yaya-shiori3-dic.md) のページも、あわせて読むことをお勧めします。

## YAYAとAYAの違い

- AYA は umeici さんの作成された SHIORI です。最後のバージョンは 5.8 で、[::: et cetera.](http://umeici.onjn.jp/) から入手できます。
- YAYA は、umeici さんの AYA Ver.5 を原型に、YAYA 開発チーム（整備班）が引き継いで、改造・発展させているものです。
- YAYA には、500 系（Tc5xx-x）と 600 系（Tc6xx-x。YAYA 6）があります。600 系では、ハッシュや入れ子の配列、JSON・XML などの読み書き、SQLite が使えるようになりました。500 系の辞書は、`yaya.dll` を置き換えるだけで、ほぼそのまま動きます。詳しくは [YAYA 6 登場](yaya6-launch.md) と [600 での変更点](changes-600.md) を見てください。

### どっちを使えばいいの？

AYA と YAYA のどちらを使えばよいか迷ったときのために、簡単な比較を載せておきます。

|  | 新機能・更新 | 安定性 |
|---|---|---|
| AYA | △ AYA の更新は停止しています。 | ○ AYA 5.8 になってからずいぶん経ちますが、安定しています。 |
| YAYA | ○ YAYA 開発チームが、新機能の追加と更新を続けています。 | △ 頻繁に更新されるぶん、バージョンによって動作が変わることがあります。更新するときは、変更履歴を確認してください。 |

単純に言うと…

- すでに AYA で動いているゴーストに、特に機能的な不満が無ければ、AYA のままで問題ありません。
- これからゴーストを作る方や、新しい機能をどんどん試してみたい方は、YAYA を使ってください。AYA から移りたいときは、[AYAからの移行](../startup/migration-from-aya.md) を見てください。

このマニュアルでは、YAYA を中心に情報を掲載しています。

## 配布・関連ツール

- [ダウンロード（GitHub Releases）](https://github.com/YAYA-shiori/yaya-shiori/releases)
- [更新履歴](https://github.com/YAYA-shiori/yaya-shiori/wiki/ChangeLog)
- [紺野ややめ](https://github.com/YAYA-shiori/konnoyayame) — YAYA のテンプレートゴースト
- [玉（tama）](https://github.com/YAYA-shiori/tama/releases) — 辞書のエラーチェックやデバッグに使うツール
- [yaya-CI-check](https://github.com/YAYA-shiori/yaya-CI-check) — GitHub Actions で辞書を検査する CI ツール

## このマニュアルの構成

| 知りたいこと | ページ |
|---|---|
| YAYA の書き方をざっと確認したい | [チートシート](../startup/cheatsheet.md) |
| はじめてゴーストを作りたい | [ゴーストの作り方](../startup/creating-ghost.md)、[チュートリアル](../startup/tutorial-01-preparation.md) |
| プログラミングをしたことがない | [基本](../INDEX.md#基本-basic) |
| 文法を知りたい | [文法](../INDEX.md#文法-grammar) |
| 組み込み関数を調べたい | [用途別の関数一覧](../INDEX.md#システム関数組み込み関数-functions)、[システム関数一覧](../system/system-functions-index.md) |
| システム辞書について知りたい | [yaya_shiori3.dic](../system/yaya-shiori3-dic.md)、[yaya_optional.dic](../system/yaya-optional-dic.md) |
| いろいろなノウハウを知りたい | [Tips](../INDEX.md#tips-tips) |
| 困ったとき | [トラブルシューティング](troubleshooting.md) |
