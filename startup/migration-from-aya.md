# AYAからの移行

**Source:** StartUp/AYAからの移行

## 主な変更点

### DLL・ファイル名の変更

- `aya5.dll` → `yaya.dll`
- `descript.txt` と設定ファイルの名前を対応して変更
- セーブファイル: `aya5_variable.cfg` → `yaya_variable.cfg`

**セーブデータの引き継ぎ:** `aya_shiori3.dic` の `OnLoad` 先頭に旧フォーマットを復元・変換するコードを追加する。

### システム辞書の変更

システム辞書は単純な更新ではなく置き換えが必要。YAYAのデフォルト辞書は AYA5 が自動処理していたバイト値変換を行わなくなった。`NAMETOVALUE` などの一部の関数はシステム辞書から削除された。

## 移行手順（aya_shiori3.dic を改変していない場合）

1. `descript.txt` を `aya5.dll` → `yaya.dll` に変更
2. `aya5.dll` を削除し `yaya.dll` をインストール
3. `aya5.txt` → `yaya.txt` にリネーム
4. 紺野ややめをダウンロードしてシステムファイルを展開
5. systemフォルダの内容をゴーストにコピー
6. `system_config.txt` をゴーストディレクトリにコピー
7. `yaya.txt` で `aya_shiori3.dic` の参照を `include, system_config.txt` に変更
8. `config.dic` を設定: `SHIORI3FW.AUTO_DATA_CONVERT=1` と `SHIORI3FW.REF_ACCEL=0`

**ネット配布の場合:** `delete.txt` を作成し `aya5.dll` と `aya5.txt` を削除対象に追加する。

## 関連

- [StartUp/YAYAでゴーストを作る](./creating-ghost.md)
- [システム辞書/yaya_shiori3.dic](../system/yaya-shiori3-dic.md)
