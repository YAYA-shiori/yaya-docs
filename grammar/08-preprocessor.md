# プリプロセス

**Source:** マニュアル/文法/8.プリプロセス

## 概要

辞書ファイルの読み込み時に実行されるプリプロセッサコマンド。

## #define

辞書ファイルの生テキストに対して直接文字列置換を行う：

```
#define before after
```

宣言以降のすべてのテキストに対して、そのファイルの末尾まで適用される。置換は宣言された順に実行されるため、先に変換すべきものを先に書く。

## #globaldefine

`#define` と似ているが、スコープが広い：

```
#globaldefine before after
```

以降に読み込まれるすべての辞書ファイルにわたって有効。最初の辞書ファイルの先頭に置くと、プロジェクト全体に効果が及ぶ。

**処理順序:** `#define` の置換が先に実行され、次に `#globaldefine` の置換が行われる：

```
#globaldefine tea green
#define tea milk
"teacup"
```

結果: `"milkcup"` （`#define` が優先される）

## \_\_AYA\_SYSTEM\_FILE\_\_

YAYA Tc543-1 以降で使用可能。DLLからの現在ファイルの相対パスを返す：

```
"__AYA_SYSTEM_FILE__"
```

例：`"aya_aitalk.txt"` を出力

## \_\_AYA\_SYSTEM\_LINE\_\_

Tc543-1 以降で使用可能。`__AYA_SYSTEM_FILE__` と同じ仕組みで、実行中のファイルの現在行番号を返す。
