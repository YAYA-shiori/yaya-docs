# YAYA as PLUGIN

**Source:** YAYA as PLUGIN

## 概要

yaya.dllのプラグイン規格対応用辞書セット。YAYA構文でプラグインを作成でき、SAORI連携もサポートする。PLUGIN/2.0仕様に対応し、主にSSP専用のプラグインシステムとして機能する。

## 配布

[The Maintenance Shop](http://ms.shillest.net/yaya_as.xhtml) で入手可能。

## 作成されたプラグイン例

| プラグイン名 | 説明 |
|-----------|------|
| きょうの伺か+ | ゴースト向けTwitter連携 |
| スタンプ帳 | スタンプコレクションプラグイン |
| BalloonMaker | バルーン作成ユーティリティ |
| BalloonSelector | バルーン選択サポート |

## プラグイン作成方法

必要なファイルは3つ：

### yaya_plugin_main.txt
`OnMenuExec` イベントハンドラを含む。プラグインメニューアクセス時にどのイベントを起動するか、Reference値、対象ゴースト指定、バルーンマーカー、ダイアログスクリプトを記述。

### descript.txt
設定ファイル。文字コード（Shift_JIS）、プラグイン名、作者情報、ファイル名（yaya.dll）、プラグインID（UUIDツールで生成）、更新URLを記載。

### install.txt
インストールメタデータ。プラグインの種類、名前、ディレクトリ指定を記載。

## 注意事項

- イベント監視には yaya.txt のログを有効化する
- 里々経由で値を送信する際、句読点に自動のwaitタグが付く場合がある
- プラグインのリロードはプラグインエクスプローラーから無効化→有効化のサイクルで行う

## 関連

- [YAYA as SAORI](./yaya-as-saori.md)
- PLUGIN/2.0仕様: http://ssp.shillest.net/ukadoc/manual/spec_plugin.html
