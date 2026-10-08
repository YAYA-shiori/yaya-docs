# YAYAでゴーストを作る

## 1. テンプレートゴーストを選ぶ

まずは好きなテンプレートを選んで、改変してみる。

| テンプレート | 説明 |
|-----------|------|
| [はろーYAYAわーるど（紺野ややめ）](http://ms.shillest.net/yayame.xhtml) | 単体でもゴーストとして楽しめるテンプレートゴースト |
| [SimpleYAYAテンプレート](../other/simple-yaya-template.md) | もっとシンプルなテンプレートが欲しい人向け |
| [紺野りりす](http://ms.shillest.net/yayalilith.xhtml) | YAYA らしくない、強力な開発支援処理全部盛りが特徴。最終目標は、ベースウェア作者全面協力の、里々並みの簡単さと強力な拡張性を併せ持つ最強開発環境 |

### デバッガ

テンプレートではないが、デバッガとして [「玉」配布サイト](http://umeici.onjn.jp/)の「tama (debugger for aya)」を導入しておくことをおすすめする。使い方は[玉を使った辞書エラーチェック](../tips/tama-error-check.md)などを参考にすること。

### 注意

本格的に編集する前に、ネットワーク更新でファイルが変更されてしまう場合がある。紺野ややめ・紺野りりすを使用する場合は、`yaya_string.txt` の中の `homeurl` を無効にしておくこと。

## 2. マニュアルを読む

テンプレートに無いことをやってみたくなったり、テンプレートをどう改変すればいいのかわからなくなったりしたら、マニュアルを読む。

- この[マニュアル](../INDEX.md)

辞書を書くときに必要なさくらスクリプト、SHIORI Event などの情報は、このマニュアルには掲載されていない。こちらも併せて参照すること（すべて外部サイト）。

- [CROW・SSPリファレンス](http://crow.aqrs.jp/reference/all/)
- [UKADOC Project TOP](https://ssp.shillest.net/ukadoc/manual/index.html)
- [Disc-2 ゴースト制作](http://disc2.s56.xrea.com/manual/)

今まで他の SHIORI を使っていた場合は、ここを読むとスムーズに移行できる。

- [AYAからの移行](migration-from-aya.md)
- [里々からの移行](migration-from-satolili.md)

## 3. つまづいたら

[困ったときの対処法](../other/troubleshooting.md)を見る。「マニュアルを読んでもやり方がわからない」という場合は、[Tips](../INDEX.md) にやりたいことが載っているかもしれない。探してみること。

## 関連

- [チュートリアル1: 準備](./tutorial-01-preparation.md)
- [困ったときの対処法](../other/troubleshooting.md)
