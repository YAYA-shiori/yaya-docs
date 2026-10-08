# 基礎設定

## 概要

YAYA のデフォルトの DLL ファイル名は `yaya.dll` で、主ファイル名 `yaya` は他の名前に自由に変更できる。

YAYA を動作させるには「基礎設定ファイル」と呼ばれるファイルが必要となる。基礎設定ファイルのファイル名は「主ファイル名.txt」で、デフォルトでは `yaya.txt` になる。DLL のファイル名を `hoge.dll` に変更したなら、基礎設定ファイルは `hoge.txt` になる。

基礎設定ファイルはテキストファイルで、実行される OS のデフォルトの文字コードで解読される。国際化を考慮する必要があるなら、マルチバイト文字コードに関する問題を避けるため、基礎設定ファイルは ASCII コードのみで記述するべきである。

設定ファイルが無い場合や、読み込む辞書がひとつも無い場合は、[シェルモード](#シェルモード)で動作する（Tc574-7 / Tc602-12以降。それまでは設定ファイルが無いとエラー E0005 で動作を止めていた）。

## 設定例

```
// dics
dic, basis.dic
dic, control./*doc*/ayc

// option parameters
charset, UTF-8
charset.dic, Shift_JIS
charset.setting, Shift_JIS
charset.output, UTF-8
charset.file, Shift_JIS
charset.save, UTF-8
charset.extension, Shift_JIS

msglang, english
log, executelog.txt
iolog, off
fncdepth, 16
```

設定はコマンドとパラメータをカンマで区切って指定する。空行（改行のみの行）、`//` 以降、および `/*` と `*/` で囲まれた領域はコメントと見なされる。

## 読み込み時に辞書エラーが起きた際の挙動

Tc555-1以降、読み込み時に辞書エラーが起きたときは、まず緊急時用の基礎設定ファイルで再度読み込みを試す。

緊急時用の基礎設定ファイルのファイル名は「主ファイル名_emerg.txt」で、デフォルトでは `yaya_emerg.txt` になる。DLL 名を変更したときの挙動も通常の基礎設定ファイルと同様。

それでもエラーになった場合は、request 関数から何も返さない（NULL）状態になる。

問題が起きたときのエラーログは [GETERRORLOG](../functions/GETERRORLOG.md) で取得できる。

`yaya_emerg.txt` による緊急モードは[シェルモード](#シェルモード)にはならない。`yaya_emerg.txt` が無ければ、これまでどおり動作を止める。

## 設定項目

### charset, name

標準の文字コードを設定する。次の予約値からいずれかを指定する。指定が無い場合は Shift_JIS として扱われる。

- `Shift_JIS` / `ShiftJIS` / `SJIS`: シフト JIS コード
- `UTF-8`: UTF-8
- `default`: 実行 OS のデフォルト文字コード

以下の `charset.` で始まるものは個別設定。必ず `charset` での一括指定より後に書くこと。

### charset.dic

辞書の文字コード。

### charset.setting

基礎設定ファイルそのものの文字コード。

### charset.output

request 関数での入出力の文字コード。

### charset.log

ログファイルや玉の出力の文字コード（Tc569-15以降）。

### charset.file

ファイル入出力の文字コード。

### charset.save

グローバル変数セーブファイル入出力の文字コード。

### charset.save.old

文字コード指定のない旧形式のセーブファイルを読み取るときの文字コード。

### charset.extension

外部 DLL（SAORI 等）入出力の文字コード。

### dic, filename ( , charset )

辞書ファイル `filename` をロードする。辞書ファイルは YAYA のスクリプトが記述されたプログラムソースファイルで、YAYA はここにプログラムされた内容を元に動作する。辞書ファイルはいくつでも指定して読み込める。

`filename` は load で指定されたパス位置からの相対パスで指定する。

標準の辞書ファイルは `charset` で指定した文字コードで記述されたプレーンテキストファイル。このほかに、一定の法則でスクランブルをかけた暗号化ファイルを読み込める。

ファイル名の後に文字コードをカンマ区切りで追加すると、指定したファイルはその文字コードで読み込まれる。

### dicif, filename ( , charset )

`dic` と同じだが、指定したファイルが存在しないときは無視する（Tc571-2以降）。

### dicdir, dirname ( , charset )

指定したディレクトリ以下のすべてのファイルを辞書として読み込む（Tc556-1以降）。ディレクトリ指定であること以外は `dic` と同じ。

!!! warning "読み込み順序"
    ファイルを読む順序は決まっていない。そのため、`globaldefine` などを定義するときに、読み込み順序によって問題が発生する可能性がある。`globaldefine` を定義するときは、必ず定義した辞書を最初のほうに読み込むこと。

`dicdir` で指定したディレクトリの中に `_loading_order_override.txt` か `_loading_order.txt` という名前のファイルがあるときは、`includeEX,(ディレクトリ)/_loading_order.txt` と書いたのと同じ挙動になる。`_loading_order_override.txt` → `_loading_order.txt` の順にファイルの存在をチェックし、先に見つかったほうのみ `includeEX` する（Tc571-2以降）。

`dic` の指定が無い場合や、`dicif` の対象がすべて存在しない、`dicdir` のディレクトリが空、などで読み込む辞書がひとつも無い場合は、[シェルモード](#シェルモード)で動作する（Tc574-7 / Tc602-12以降）。

### msglang, language

!!! note "ふつうは指定不要"
    ふつうは特に指定しなくても、エラーメッセージの言語は自動で切り替わる（Tc573-5以降）。

ログに記録されるエラーメッセージ類の言語を選択する。次の予約値からいずれかを指定する。指定が無い場合は `japanese` として扱われる。

- `japanese`
- `english`
- `chinese-simplified`
- `chinese-traditional`
- `german`
- `korean`

本設定は過去互換のために残されている。次の `messagetxt` を使うこと。

### messagetxt, filename ( , charset )

!!! note "ふつうは指定不要"
    ふつうは特に指定しなくても、エラーメッセージの言語は自動で切り替わる（Tc573-5以降）。

ログに記録されるエラーメッセージ類の言語ファイルを読み込む。たとえば次のように書く。`charset` を省略した場合は UTF-8（BOM 付）になる（Tc557以降）。

```
messagetxt,messagetxt/japanese.txt
messagetxt,messagetxt/english.txt
messagetxt,messagetxt/chinese-simplified.txt
messagetxt,messagetxt/chinese-traditional.txt
messagetxt,messagetxt/german.txt
messagetxt,messagetxt/korean.txt
```

言語ファイル名は [yaya-shiori の messagetxt](https://github.com/ponapalt/yaya-shiori/tree/500/messagetxt) で確認できる。

Tc570-1以降、Windows 上では言語ファイルを DLL に埋め込むようになったので、言語ファイル本体を配布する必要はない。`messagetxt` にファイル名を書く仕様は、Windows 以外の環境向けにそのまま残されている。

### basepath, directory

辞書等を読み込む基準点となるディレクトリを任意の場所に再設定する。設定しない場合、通常は `yaya.dll` と同じディレクトリになる（Tc557以降）。

### include, filename

基礎設定ファイルの内容を別ファイルから読み込む。指定したファイルの中身も有効な基礎設定として扱われる。

### includeEX, filename

`include` と基本的には同じ処理だが、`filename` に指定したファイル名がディレクトリ名を含む文字列だった場合に、そのディレクトリ内にカレントディレクトリを一時的に切り替えてから `include` 処理を行う（Tc559以降）。

### log, logfilename

実行ログをファイル `logfilename` に記録する。`charset.log` で指定した文字コードで書き込まれる。`logfilename` は load で指定されたパス位置からの相対パスで指定する。

### iolog, [on|off]

load、unload、request 実行時の入出力文字列と処理時間をログに記録するかを設定する。`on` で記録する。デフォルトでは `on` なので、不要な場合に `off` とすること。`off` 指定としても、玉にドラッグ＆ドロップして起動する使い方をした場合は強制的に `on` になる。

### iolog.filter.keyword, [無視判定文字列]

request の文字列中に指定した無視判定文字列が含まれていた場合、その request の I/O をログに記録しない（玉への出力もしない）ようにする。複数指定できる。旧定義名は `ignoreiolog`。

例: `OnSecondChange` と `OnMouse` 系のイベントを記録しない

```
ignoreiolog, ID: OnSecondChange //OnSecondChange無視
iolog.filter.keyword, OnMouse        //OnMouse系無視
```

基礎設定ファイルの書式上、無視判定文字列の前後の空白、およびコメント `//` 以降は無視される。

### iolog.filter.keyword.delete, [文字列]

上記を削除する。[SETSETTING](../functions/SETSETTING.md) 向けの書き方で、定義ファイルに直接書いてもあまり意味はない。

### iolog.filter.keyword.regex, [無視判定文字列：正規表現]

`iolog.filter.keyword` の正規表現版。

### iolog.filter.keyword.regex.delete, [文字列]

上記を削除する。[SETSETTING](../functions/SETSETTING.md) 向けの書き方で、定義ファイルに直接書いてもあまり意味はない。

### iolog.filter.mode, [モード]

上記の `iolog.filter.keyword` 以下の判定条件について、「条件に合致したものを出力しない」か「条件に合致したものだけを出力する」かを切り替える。定義しない場合は「条件に合致したものを出力しない」モードになる。

```
iolog.filter.mode,allowlist
iolog.filter.mode,whitelist
```

条件に合致したものだけを出力するモードに切り替える。

```
iolog.filter.mode,denylist
iolog.filter.mode,blacklist
```

条件に合致したものを出力しないモードに切り替える。

### fncdepth, [depth]

関数呼び出しの深さ上限を数値で指定する。デフォルト値は 32。最低値は 2 で、これより小さな値や不正な値を指定した場合も 2 として扱われる。0 にすると上限チェックをしないが、呼び出しが深すぎるとベースウェアごと落ちる（Tc556-1以降）。

上限に達すると [shiori.OnCallLimit](../system/shiori-OnCallLimit.md) が呼ばれる。

### looplimit, [count]

ループの回数上限を数値で指定する。デフォルト値は 10000。0 にすると上限チェックをしないが、延々と実行を続けてフリーズする。`foreach` には効果がない（Tc564-1以降）。

上限に達すると [shiori.OnLoopLimit](../system/shiori-OnLoopLimit.md) が呼ばれる。

### save.encode, [on|off]

セーブファイルを暗号化する。「暗号化」といってもたいしたものではないので、せいぜい多少わかりにくくする程度と考えること。一度 `on` にするとセーブファイルを削除するまで暗号化されたままになる。設定を変えるときは十分注意すること。

### save.auto, [on|off]

セーブファイル自動保存機能の ON/OFF を切り替える。ON の場合、一定時間ごとのバックアップと終了時の変数自動保存が行われる。OFF の場合は保存関数を明示的に呼ばない限り保存されない。標準は ON。

### embed.lazy, [on|off]

文字列のカッコなし `%` 埋め込みの名前を実行時に探す（デフォルト: `on`）。`off` で辞書の読み込み時に確定する（Tc604-1以降。[詳細](06-string-embedding.md#名前を読み込み時に確定する)）。

### maxlognum, [count]

[GETERRORLOG](../functions/GETERRORLOG.md) で取得できるログの最大値を設定する。デフォルト値は 256 要素。

## シェルモード

Tc574-7 / Tc602-12以降。設定ファイルが無いか、読み込む辞書がひとつも無い場合、YAYAは次の辞書だけを読み込んだものとして動作する。

```c
load { }
unload { }
request { EVAL(_argv[0]) }
```

requestに渡された文字列をそのまま [EVAL](../functions/EVAL.md) し、その結果を返す。式ひとつのほか、`;` や改行で区切った文の並びや制御文も書ける。ゴースト一式や辞書を用意しなくても、YAYAの式や関数の動作を手早く確かめられる。

| request の入力 | 返値 |
|---------------|------|
| `1+2` | `3` |
| `_a = 3; _a * 5` | `15` |
| `'hello' + ' world'` | `hello world` |
| `X = 10` | 空文字列（グローバル変数 `X` に 10 が入る） |
| `X` | `10` |

- グローバル変数は同じセッションの間は保持される
- 設定ファイルが無い場合は、変数の自動保存・復元（`yaya_variable.cfg`）を行わない。設定ファイルはあって辞書の指定だけが無い場合は、`save.auto` などの設定に従う
- シェルモードに入ると、ログに注記 N0002 が出る
- `dic` で指定した辞書ファイルが存在しない、辞書に文法エラーがある、`include` の対象が無い、といったエラーの場合はシェルモードにはならない
- SHIORIのリクエストもそのまま EVAL されるため、ゴーストとして使うためのものではない。YAYA の実行ファイル版（`yaya.exe`）で、空のディレクトリを `load` してから式を `request` で送る、といった使い方を想定している
