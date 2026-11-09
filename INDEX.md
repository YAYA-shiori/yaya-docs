# YAYA マニュアル

伺か（ukagaka）の SHIORI「YAYA」の使い方と仕様をまとめたマニュアルです。YAYA と、その前身である AYA に関する情報や Tips も集めています。

プログラミングをしたことがない方にもわかるように書くことを目指しています。わかりにくいところや間違いを見つけたら、[整備班BTS](https://bts.shillest.net/)（報告フォーム）で気軽に教えてください。GitHub に慣れている方は、[Issues](https://github.com/YAYA-shiori/yaya-docs/issues) や Pull Request でも構いません。

> AI エージェント向けに、探し方の案内 [llms.txt](https://yaya-shiori.github.io/yaya-docs/llms.txt) を用意しています。各ページの Markdown 原稿は、リポジトリと同じパスの `.md`（例: `https://yaya-shiori.github.io/yaya-docs/startup/cheatsheet.md`）で取得できます。

## ダウンロード

- [ダウンロード（GitHub Releases）](https://github.com/YAYA-shiori/yaya-shiori/releases)
- [更新履歴](https://github.com/YAYA-shiori/yaya-shiori/wiki/ChangeLog)

## YAYA v6 (通称Tc600系)

- [steve green氏](https://github.com/steve02081504)の開発ブランチを取り込み、互換性を調整し、大幅強化版としてリリースしたものです。
- 変数の柔軟性、高速ヘッダ解析、XML/JSONなどのパーサ、DB(SQLite)など、500系と高い互換性を保ちながら大幅な改修が行われています。
- まずはざっくり知りたい → [YAYA 6 登場](other/yaya6-launch.md)
- YAYA Tc5xx-x から Tc6xx-x (v5系からv6系) に移行したい →[600 での変更点](other/changes-600.md)（`yaya.dll` を置き換えるだけで、辞書もセーブファイルもそのまま動きます。気をつける点は関数名の衝突など数点だけです）

## はじめての方へ

- YAYA や AYA って何？ → [YAYAについて](other/yaya.md)
- YAYA の書き方をざっと確認したい → [チートシート](startup/cheatsheet.md)
- はじめてゴーストを作りたいんだけど？ → [ゴーストの作り方](startup/creating-ghost.md)
- AYA でゴーストを作っていたけど、YAYA に移りたい → [AYAからの移行](startup/migration-from-aya.md)
- 里々から YAYA に移りたい → [里々からの移行](startup/migration-from-satolili.md)

## 調べたいとき

- プログラミングをしたことがない！ → [基本](basic/)
- YAYA の文法を知りたい → [文法](grammar/)、[チートシート](startup/cheatsheet.md)
- どんな組み込み（システム）関数があるの？ → [用途別の関数一覧](functions/)
- 関数を名前から探したい → [システム関数一覧](system/system-functions-index.md)
- エラーを調べたい・処理したい → [エラー処理関数](system/error-handling-functions.md)

ページ上部の検索窓からも探せます。

## システム辞書・テンプレート

- システム辞書について → [yaya_shiori3.dic](system/yaya-shiori3-dic.md)、[yaya_optional.dic](system/yaya-optional-dic.md)
- テンプレートゴーストについて → [ゴーストの作り方](startup/creating-ghost.md)、[シンプルなYAYAテンプレート](other/simple-yaya-template.md)
- トークを手軽に書きたい → [talklib](other/talklib.md)
- SHIORI 以外の使い方 → [SAORIとしてのYAYA](other/yaya-as-saori.md)、[MAKOTOとしてのYAYA](other/yaya-as-makoto.md)、[プラグインとしてのYAYA](other/yaya-as-plugin.md)

## 困ったとき

- いろいろなノウハウを知りたい → [Tips](tips/)
- 作っていて困ったことがあったら → [トラブルシューティング](other/troubleshooting.md)
- それでも解決しないときや、YAYA の不具合らしいときは → [整備班BTS](https://bts.shillest.net/)（報告フォーム）で聞いてみましょう。GitHub に慣れている方は、[yaya-shiori の Issues](https://github.com/YAYA-shiori/yaya-shiori/issues) や Pull Request でも構いません
- [開発情報検索](http://ukadev.shillest.net/) で検索すると、答えが見つかるかもしれません

## 関連ツール

- [紺野ややめ](https://github.com/YAYA-shiori/konnoyayame) — YAYA のテンプレートゴースト
- [玉（tama）](https://github.com/YAYA-shiori/tama/releases) — 辞書のエラーチェックやデバッグに使うツール
- [yaya-CI-check](https://github.com/YAYA-shiori/yaya-CI-check) — GitHub Actions で辞書を検査する CI ツール
- [ukagaka-doc-mcp](https://github.com/finelagusaz/ukagaka-doc-mcp) - AIによる開発で伺か関連の仕様を勝手に探してもらうためのツール
