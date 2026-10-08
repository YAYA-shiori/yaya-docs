# AYAからの移行

既存の AYA5 ゴーストを YAYA へ移行する。

## 注意点

### DLL名称の変更

DLL 名称が `aya5.dll` から `yaya.dll` に変更になる。

- そのため、`aya5.txt` は `yaya.txt` に名前を変える必要がある
- セーブファイル名が `yaya_variable.cfg` になり、セーブデータがそのままでは移行されない

これを避けるための機能が用意されている。`aya_shiori3.dic` を開き、`load` 関数の `OnLoad` の手前に、次のコードを追加する。

```
if FSIZE('yaya_variable.cfg') <= 0 {
	RESTOREVAR('aya5_variable.cfg')
	SAVEVAR('yaya_variable.cfg')
	FDEL('aya5_variable.cfg')
}
```

`aya_shiori3.dic` をいじっていない場合は、[システム辞書](../system/yaya-shiori3-dic.md)の項目を見ながら、必要なファイルをダウンロードして上書きすると、簡単に移行できる（過去互換辞書を使う場合は、`yaya.txt` の `aya_shiori3.dic` の後に、AYA 互換のための辞書を書き足す。現在のシステム辞書では `compatible.dic` がこれにあたる）。

### システム辞書の変更

システム辞書が変更になる（置き換えることを推奨する）。

- SAORI の戻り値などは、AYA5 のシステム辞書ではバイト値 1 をコンマに置き換え、数字は文字列ではなく数値に変換されていたが、YAYA 用のシステム辞書では、デフォルトではこの作業が行われない
- 一部の関数（`NAMETOVALUE` など）がシステム辞書に含まれない

## 移行手順

ここでは、**AYA5 で `aya_shiori3.dic` をいじっていない場合**の移行手順を示す。以下の作業はすべて、ゴーストの辞書フォルダ（`ghost/master/`）での作業。

1. `descript.txt` の `shiori,aya5.dll` を `shiori,yaya.dll` に書き換える
2. `aya5.dll` を削除し、`yaya.dll` を置く
3. `aya5.txt` を `yaya.txt` に変更する
4. [紺野ややめ](http://ms.shillest.net/yayame.xhtml)をダウンロードし、NAR ファイルを ZIP として解凍するか、ゴーストをインストールして中のファイルを見られる状態にする
5. [システム辞書](../system/yaya-shiori3-dic.md)を参照し、`system` フォルダ以下をコピーする
6. `system_config.txt` をコピーする
7. `yaya.txt` 内の `dic,aya_shiori3.dic` を消去し、代わりに `include, system_config.txt` と書く
8. `config.dic` を開き、`SHIORI3FW.AUTO_DATA_CONVERT` を 1、`SHIORI3FW.REF_ACCEL` を 0 にする

以上の作業により、だいたいの移行に関するエラーが解消される。

## ネットワーク配布の場合

ネットワーク配布では、`aya5.dll` と `aya5.txt` はすでに要らないものなので、次の内容の `delete.txt` などを使って削除するとよい。

```
ghost/master/aya5.dll
ghost/master/aya5.txt
```

## 関連

- [YAYAでゴーストを作る](./creating-ghost.md)
- [システム辞書/yaya_shiori3.dic](../system/yaya-shiori3-dic.md)
