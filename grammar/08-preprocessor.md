# プリプロセス

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

## \_\_AYA\_SYSTEM\_FUNC\_\_

Tc574-2 以降（600 系は Tc602-2 以降）で使用可能。関数の中に書くと、その関数の名前に置き換わる：

```
OnTest
{
	LOGGING("__AYA_SYSTEM_FUNC__: called")
}
```

例：`"OnTest: called"` を出力

- 置き換わるのは関数の `{` `}` の中だけ。関数名に付けた重複回避オプション（`:nonoverlap` など）は含まれない
- `#define` の置換後の文字列に含まれていても置き換わるので、ログ出力用のマクロに使える
- [APPEND_RUNTIME_DIC](../functions/APPEND_RUNTIME_DIC.md) で追加する関数の中でも使える

## #ifdef / #ifndef / #elifdef / #elifndef / #else / #endif

Tc574-2 以降（600 系は Tc602-2 以降）で使用可能。名前が定義されているかどうかで、辞書の一部を読み込むかどうかを切り替える：

```
#ifdef 名前
（名前が定義されていれば読み込む）
#elifdef 別の名前
（最初の名前が未定義で、別の名前が定義されていれば読み込む）
#else
（どれにも当てはまらなければ読み込む）
#endif
```

- `#ifndef` / `#elifndef` は「定義されていなければ」
- `#elifdef` / `#elifndef` / `#else` は省略できる。`#elifdef` / `#elifndef` はいくつでも書ける
- 入れ子にできる
- 行頭の空白は無視されるので、字下げしてよい。関数の中でも使える
- 行末に `//` コメントを書ける
- 条件式は書けない（`#if` は無い）

読み込まれない区間の行は、構文を解析しない。存在しないシステム関数の呼び出しや、その YAYA が知らない構文を書いてもエラーにならない。区間内の `#define` / `#globaldefine` も登録されない。

ただし、コメント（`/* */`）・行末の `/` による行の結合・ヒアドキュメントは先に処理される。ヒアドキュメントの中に書いた `#endif` などは、プリプロセッサとして扱われない。

### 判定の対象になる名前

| 名前 | 定義されている条件 |
|---|---|
| `#define` の名前 | そのファイルの、その行より前で定義されている |
| `#globaldefine` の名前 | それより前に読み込まれた辞書ファイル（同じファイルならその行より前）で定義されている |
| `__AYA_SYSTEM_YAYA5__` | 500 系の YAYA |
| `__AYA_SYSTEM_YAYA6__` | 600 系の YAYA |
| `__AYA_SYSTEM_SYSFUNC_関数名__` | そのシステム関数がある（例：`__AYA_SYSTEM_SYSFUNC_FREADJSON__`） |
| `__AYA_SYSTEM_FILE__` / `__AYA_SYSTEM_LINE__` / `__AYA_SYSTEM_FUNC__` | 常に定義されている |

`__AYA_SYSTEM_YAYA5__` / `__AYA_SYSTEM_YAYA6__` / `__AYA_SYSTEM_SYSFUNC_関数名__` は `#ifdef` 系の判定にだけ使われる名前で、辞書の中の文字列は置き換えない。

`#globaldefine` は読み込み順の影響を受ける。後で読み込まれる辞書ファイルの `#globaldefine` は見えない。

### 500 系と 600 系で共用する辞書

600 系で増えた構文や関数を使うと、500 系では読み込み時にエラーになる（未知の関数の呼び出しは E0071 など）。`#ifdef` で書き分ければ、どちらでもエラーにならない：

```
#ifdef __AYA_SYSTEM_YAYA6__
LoadConfig
{
	FREADJSON('config.json')
}
#else
LoadConfig
{
	// 500 系向けの代わりの処理
}
#endif
```

特定のシステム関数があるかどうかで書き分けるときは `__AYA_SYSTEM_SYSFUNC_関数名__` を使う。こちらは今後の版で関数が追加されたときにも、そのまま使える：

```
#ifdef __AYA_SYSTEM_SYSFUNC_DUMPJSON__
	_s = DUMPJSON(_data)
#else
	_s = ''
#endif
```

`#ifdef` を知らない古い YAYA（Tc574-1 以前、Tc602-1 以前）では、`#ifdef` などの行がエラー E0076 になり、区間の中身もすべて解析される。共用の辞書を配布するときは、対応する YAYA の版を明記すること。

## #error / #warning

Tc574-2 以降（600 系は Tc602-2 以降）で使用可能。読み込み時にエラー・警告を出す：

```
#ifndef __AYA_SYSTEM_YAYA6__
#error この辞書は YAYA 600 系（Tc602-2 以降）が必要です
#endif
```

- `#error` はエラー E0104 を出す。辞書エラーになるので、緊急モードで読み込まれる
- `#warning` は警告 W0028 を出す。読み込みは続く
- 後ろに書いた文字列がメッセージに続けて出力される（行末の `//` コメントは除く）
- `#ifdef` などで読み込まれない区間では何もしない

## エラー

| 番号 | 内容 |
|---|---|
| E0074 | `#ifdef` 系に名前が無い、名前が2つ以上ある、`#else` / `#endif` の後ろに文字列がある |
| E0101 | 対応する `#ifdef` / `#ifndef` が無い `#elifdef` / `#elifndef` / `#else` / `#endif` |
| E0102 | `#else` の後に `#elifdef` / `#elifndef` / `#else` がある |
| E0103 | `#ifdef` / `#ifndef` が `#endif` で閉じられていない（いちばん内側の `#ifdef` の行を表示する） |
| E0104 | `#error` |
| W0028 | `#warning` |
