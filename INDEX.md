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

- プログラミングをしたことがない！ → [基本](#基本)
- YAYA の文法を知りたい → [文法](#文法)、[チートシート](startup/cheatsheet.md)
- どんな組み込み（システム）関数があるの？ → [用途別の関数一覧](#システム関数組み込み関数)
- 関数を名前から探したい → [システム関数一覧](system/system-functions-index.md)
- エラーを調べたい・処理したい → [エラー処理関数](system/error-handling-functions.md)

ページ上部の検索窓からも探せます。

## システム辞書・テンプレート

- システム辞書について → [yaya_shiori3.dic](system/yaya-shiori3-dic.md)、[yaya_optional.dic](system/yaya-optional-dic.md)
- テンプレートゴーストについて → [ゴーストの作り方](startup/creating-ghost.md)、[シンプルなYAYAテンプレート](other/simple-yaya-template.md)
- トークを手軽に書きたい → [talklib](other/talklib.md)
- SHIORI 以外の使い方 → [SAORIとしてのYAYA](other/yaya-as-saori.md)、[MAKOTOとしてのYAYA](other/yaya-as-makoto.md)、[プラグインとしてのYAYA](other/yaya-as-plugin.md)

## 困ったとき

- いろいろなノウハウを知りたい → [Tips](#tips)
- 作っていて困ったことがあったら → [トラブルシューティング](other/troubleshooting.md)
- それでも解決しないときや、YAYA の不具合らしいときは → [整備班BTS](https://bts.shillest.net/)（報告フォーム）で聞いてみましょう。GitHub に慣れている方は、[yaya-shiori の Issues](https://github.com/YAYA-shiori/yaya-shiori/issues) や Pull Request でも構いません
- [開発情報検索](http://ukadev.shillest.net/) で検索すると、答えが見つかるかもしれません

## 関連ツール

- [紺野ややめ](https://github.com/YAYA-shiori/konnoyayame) — YAYA のテンプレートゴースト
- [玉（tama）](https://github.com/YAYA-shiori/tama/releases) — 辞書のエラーチェックやデバッグに使うツール
- [yaya-CI-check](https://github.com/YAYA-shiori/yaya-CI-check) — GitHub Actions で辞書を検査する CI ツール
- [ukagaka-doc-mcp](https://github.com/finelagusaz/ukagaka-doc-mcp) - AIによる開発で伺か関連の仕様を勝手に探してもらうためのツール

---

## 文法

- [基本設定](grammar/01-basic-settings.md)
- [関数](grammar/02-functions.md)
- [値と変数](grammar/03-values-and-variables.md)
- [算術演算](grammar/04-arithmetic.md)
- [配列](grammar/05-arrays.md)
- [文字列埋め込み](grammar/06-string-embedding.md)
- [フロー制御](grammar/07-flow-control.md)
- [プリプロセッサ](grammar/08-preprocessor.md)
- [予約語](grammar/09-reserved-words.md)
- [Windows DLLとしてのYAYA](grammar/10-yaya-as-windows-dll.md)
- [文字コード](grammar/11-character-encoding.md)
- [ハッシュ（Tc600-3以降）](grammar/12-hash.md)
- [値の入れ子と多次元代入（Tc600-3以降）](grammar/13-nesting.md)
- [正規表現](grammar/14-regular-expressions.md)

---

## 基本

- [変数](basic/variables.md)
- [関数](basic/functions.md)
- [条件分岐](basic/branching.md)
- [ループ](basic/loops.md)
- [配列](basic/arrays.md)
- [演算子](basic/operators.md)

---

## システム辞書

- [yaya_shiori3.dic](system/yaya-shiori3-dic.md)
- [yaya_optional.dic](system/yaya-optional-dic.md)
- [システム関数一覧](system/system-functions-index.md)
- [エラー処理関数](system/error-handling-functions.md)
- [OnCallLimit](system/shiori-OnCallLimit.md)
- [OnLoopLimit](system/shiori-OnLoopLimit.md)
- [OnMemoryError](system/shiori-OnMemoryError.md)
- [OnMemoryLimit](system/shiori-OnMemoryLimit.md)

---

## StartUp / チュートリアル

- [チートシート](startup/cheatsheet.md)
- [ゴーストの作り方](startup/creating-ghost.md)
- [チュートリアル1: 準備](startup/tutorial-01-preparation.md)
- [チュートリアル2: セリフを書く](startup/tutorial-02-writing-dialogue.md)
- [チュートリアル3: 変数](startup/tutorial-03-variables.md)
- [AYAからの移行](startup/migration-from-aya.md)
- [里々からの移行](startup/migration-from-satolili.md)

---

## その他

- [YAYAについて](other/yaya.md)
- [SAORIとしてのYAYA](other/yaya-as-saori.md)
- [MAKOTOとしてのYAYA](other/yaya-as-makoto.md)
- [プラグインとしてのYAYA](other/yaya-as-plugin.md)
- [SAORIの使い方](other/saori-usage.md)
- [talklib](other/talklib.md)
- [シンプルなYAYAテンプレート](other/simple-yaya-template.md)
- [トラブルシューティング](other/troubleshooting.md)
- [LINT系関数の仕様と制約](other/lint-functions.md)
- [600 での変更点（Tc600-3以降）](other/changes-600.md)
- [YAYA 6 登場（600 系の紹介）](other/yaya6-launch.md)

---

## システム関数(組み込み関数)

### 型取得/変換

- [GETTYPE](functions/GETTYPE.md)
- [GETTYPEEX](functions/GETTYPEEX.md)
- [TOINT](functions/TOINT.md)
- [TOREAL](functions/TOREAL.md)
- [TOSTR](functions/TOSTR.md)
- [TOAUTO](functions/TOAUTO.md)
- [TOAUTOEX](functions/TOAUTOEX.md)
- [ISFUNC](functions/ISFUNC.md)
- [ISVAR](functions/ISVAR.md)
- [CVINT](functions/CVINT.md)
- [CVSTR](functions/CVSTR.md)
- [CVREAL](functions/CVREAL.md)
- [CVAUTO](functions/CVAUTO.md)
- [CVAUTOEX](functions/CVAUTOEX.md)
- [PARSEJSON](functions/PARSEJSON.md)
- [PARSEXML](functions/PARSEXML.md)
- [PARSEHTML](functions/PARSEHTML.md)
- [PARSEHEADER](functions/PARSEHEADER.md)
- [DUMPJSON](functions/DUMPJSON.md)
- [DUMPXML](functions/DUMPXML.md)
- [PARSEYAML](functions/PARSEYAML.md)
- [PARSETOML](functions/PARSETOML.md)
- [DUMPYAML](functions/DUMPYAML.md)
- [DUMPTOML](functions/DUMPTOML.md)

### 配列操作

- [ARRAYSIZE](functions/ARRAYSIZE.md)
- [ARRAYDEDUP](functions/ARRAYDEDUP.md)
- [ASEARCH](functions/ASEARCH.md)
- [ASEARCHEX](functions/ASEARCHEX.md)
- [ASORT](functions/ASORT.md)
- [SETDELIM](functions/SETDELIM.md)
- [GETDELIM](functions/GETDELIM.md)
- [IARRAY](functions/IARRAY.md)

### ハッシュ操作

- [IHASH](functions/IHASH.md)
- [HASH_KEYS](functions/HASH_KEYS.md)
- [HASH_VALUES](functions/HASH_VALUES.md)
- [HASH_SPLIT](functions/HASH_SPLIT.md)
- [HASH_EXIST](functions/HASH_EXIST.md)
- [HASH_SIZE](functions/HASH_SIZE.md)

### 文字列操作

- [ANY](functions/ANY.md)
- [CHR](functions/CHR.md)
- [CHRCODE](functions/CHRCODE.md)
- [CUTSPACE](functions/CUTSPACE.md)
- [ERASE](functions/ERASE.md)
- [GETSTRBYTES](functions/GETSTRBYTES.md)
- [HAN2ZEN](functions/HAN2ZEN.md)
- [HEXSTRTOI](functions/HEXSTRTOI.md)
- [BINSTRTOI](functions/BINSTRTOI.md)
- [INSERT](functions/INSERT.md)
- [ISINTSTR](functions/ISINTSTR.md)
- [ISREALSTR](functions/ISREALSTR.md)
- [REPLACE](functions/REPLACE.md)
- [SPLIT](functions/SPLIT.md)
- [SPLITPATH](functions/SPLITPATH.md)
- [STRDIGEST](functions/STRDIGEST.md)
- [STRDECODE](functions/STRDECODE.md)
- [STRENCODE](functions/STRENCODE.md)
- [STRFORM](functions/STRFORM.md)
- [STRLEN](functions/STRLEN.md)
- [STRSTR](functions/STRSTR.md)
- [SUBSTR](functions/SUBSTR.md)
- [TOBINSTR](functions/TOBINSTR.md)
- [TOHEXSTR](functions/TOHEXSTR.md)
- [TOLOWER](functions/TOLOWER.md)
- [TOUPPER](functions/TOUPPER.md)
- [TRANSLATE](functions/TRANSLATE.md)
- [ZEN2HAN](functions/ZEN2HAN.md)

### 正規表現

- [RE_SEARCH](functions/RE_SEARCH.md)
- [RE_MATCH](functions/RE_MATCH.md)
- [RE_GREP](functions/RE_GREP.md)
- [RE_REPLACE](functions/RE_REPLACE.md)
- [RE_REPLACEEX](functions/RE_REPLACEEX.md)
- [RE_SPLIT](functions/RE_SPLIT.md)
- [RE_GETSTR](functions/RE_GETSTR.md)
- [RE_GETPOS](functions/RE_GETPOS.md)
- [RE_GETLEN](functions/RE_GETLEN.md)
- [RE_ASEARCH](functions/RE_ASEARCH.md)
- [RE_ASEARCHEX](functions/RE_ASEARCHEX.md)
- [RE_OPTION](functions/RE_OPTION.md)

### 数学関数

- [RAND](functions/RAND.md)
- [SRAND](functions/SRAND.md)
- [FLOOR](functions/FLOOR.md)
- [CEIL](functions/CEIL.md)
- [ROUND](functions/ROUND.md)
- [SIN](functions/SIN.md)
- [COS](functions/COS.md)
- [TAN](functions/TAN.md)
- [ASIN](functions/ASIN.md)
- [ACOS](functions/ACOS.md)
- [ATAN](functions/ATAN.md)
- [SINH](functions/SINH.md)
- [COSH](functions/COSH.md)
- [TANH](functions/TANH.md)
- [LOG](functions/LOG.md)
- [LOG10](functions/LOG10.md)
- [POW](functions/POW.md)
- [SQRT](functions/SQRT.md)

### ビット演算

- [BITWISE_AND](functions/BITWISE_AND.md)
- [BITWISE_OR](functions/BITWISE_OR.md)
- [BITWISE_XOR](functions/BITWISE_XOR.md)
- [BITWISE_NOT](functions/BITWISE_NOT.md)
- [BITWISE_SHIFT](functions/BITWISE_SHIFT.md)

### ファイル操作

- [FOPEN](functions/FOPEN.md)
- [FCLOSE](functions/FCLOSE.md)
- [FREAD](functions/FREAD.md)
- [FREADENCODE](functions/FREADENCODE.md)
- [FREADBIN](functions/FREADBIN.md)
- [FREADJSON](functions/FREADJSON.md)
- [FREADXML](functions/FREADXML.md)
- [FREADHTML](functions/FREADHTML.md)
- [FREADYAML](functions/FREADYAML.md)
- [FREADTOML](functions/FREADTOML.md)
- [FWRITE](functions/FWRITE.md)
- [FWRITE2](functions/FWRITE2.md)
- [FWRITEBIN](functions/FWRITEBIN.md)
- [FWRITEDECODE](functions/FWRITEDECODE.md)
- [FWRITEJSON](functions/FWRITEJSON.md)
- [FWRITEXML](functions/FWRITEXML.md)
- [FWRITEYAML](functions/FWRITEYAML.md)
- [FWRITETOML](functions/FWRITETOML.md)
- [FCOPY](functions/FCOPY.md)
- [FMOVE](functions/FMOVE.md)
- [FDEL](functions/FDEL.md)
- [FRENAME](functions/FRENAME.md)
- [FSIZE](functions/FSIZE.md)
- [FENUM](functions/FENUM.md)
- [FCHARSET](functions/FCHARSET.md)
- [FATTRIB](functions/FATTRIB.md)
- [FSTATUS](functions/FSTATUS.md)
- [FDIGEST](functions/FDIGEST.md)
- [FSEEK](functions/FSEEK.md)
- [FTELL](functions/FTELL.md)
- [MKDIR](functions/MKDIR.md)
- [RMDIR](functions/RMDIR.md)

### データベース

- [SQLOPEN](functions/SQLOPEN.md)
- [SQLCLOSE](functions/SQLCLOSE.md)
- [SQLEXEC](functions/SQLEXEC.md)
- [SQLQUERY](functions/SQLQUERY.md)

### 外部ライブラリ

- [LOADLIB](functions/LOADLIB.md)
- [UNLOADLIB](functions/UNLOADLIB.md)
- [REQUESTLIB](functions/REQUESTLIB.md)
- [FUNCTIONEX](functions/FUNCTIONEX.md)
- [CHARSETLIB](functions/CHARSETLIB.md)
- [CHARSETLIBEX](functions/CHARSETLIBEX.md)

### システム情報

- [GETTIME](functions/GETTIME.md)
- [GETTIMEZONE](functions/GETTIMEZONE.md)
- [GETTICKCOUNT](functions/GETTICKCOUNT.md)
- [GETSECCOUNT](functions/GETSECCOUNT.md)
- [GETMEMINFO](functions/GETMEMINFO.md)
- [GETENV](functions/GETENV.md)
- [READFMO](functions/READFMO.md)

### メタ操作・特殊関数

- [EVAL](functions/EVAL.md)
- [ISEVALUABLE](functions/ISEVALUABLE.md)
- [ERASEVAR](functions/ERASEVAR.md)
- [LETTONAME](functions/LETTONAME.md)
- [LSO](functions/LSO.md)
- [SAVEVAR](functions/SAVEVAR.md)
- [RESTOREVAR](functions/RESTOREVAR.md)
- [SERIALIZEVAR](functions/SERIALIZEVAR.md)
- [DESERIALIZEVAR](functions/DESERIALIZEVAR.md)
- [GETSETTING](functions/GETSETTING.md)
- [SETSETTING](functions/SETSETTING.md)
- [GETFUNCLIST](functions/GETFUNCLIST.md)
- [GETFUNCINFO](functions/GETFUNCINFO.md)
- [GETVARLIST](functions/GETVARLIST.md)
- [GETSYSTEMFUNCLIST](functions/GETSYSTEMFUNCLIST.md)
- [CHARSETTEXTTOID](functions/CHARSETTEXTTOID.md)
- [CHARSETIDTOTEXT](functions/CHARSETIDTOTEXT.md)
- [EXECUTE](functions/EXECUTE.md)
- [EXECUTE_WAIT](functions/EXECUTE_WAIT.md)
- [EXECUTE_CAPTURE](functions/EXECUTE_CAPTURE.md)
- [LICENSE](functions/LICENSE.md)
- [APPEND_RUNTIME_DIC](functions/APPEND_RUNTIME_DIC.md)
- [OUTPUTNUM](functions/OUTPUTNUM.md)
- [DICLOAD](functions/DICLOAD.md)
- [DICUNLOAD](functions/DICUNLOAD.md)
- [FUNCDECL_ERASE](functions/FUNCDECL_ERASE.md)
- [FUNCDECL_READ](functions/FUNCDECL_READ.md)
- [FUNCDECL_WRITE](functions/FUNCDECL_WRITE.md)
- [UNDEFFUNC](functions/UNDEFFUNC.md)
- [ISGLOBALDEFINE](functions/ISGLOBALDEFINE.md)
- [PROCESSGLOBALDEFINE](functions/PROCESSGLOBALDEFINE.md)
- [SETGLOBALDEFINE](functions/SETGLOBALDEFINE.md)
- [UNDEFGLOBALDEFINE](functions/UNDEFGLOBALDEFINE.md)

### 通信・プロセス間通信

- [DIRECTSSTP](functions/DIRECTSSTP.md)

### スレッド

- [THREADSTART](functions/THREADSTART.md)
- [THREADSTATE](functions/THREADSTATE.md)
- [THREADSTOP](functions/THREADSTOP.md)
- [THREADJOIN](functions/THREADJOIN.md)
- [THREADRESULT](functions/THREADRESULT.md)
- [THREADCLOSE](functions/THREADCLOSE.md)

### デバッグ

- [LOGGING](functions/LOGGING.md)
- [GETLASTERROR](functions/GETLASTERROR.md)
- [SETLASTERROR](functions/SETLASTERROR.md)
- [GETERRORLOG](functions/GETERRORLOG.md)
- [GETCALLSTACK](functions/GETCALLSTACK.md)
- [CLEARERRORLOG](functions/CLEARERRORLOG.md)
- [DUMPVAR](functions/DUMPVAR.md)
- [SLEEP](functions/SLEEP.md)
- [SETTAMAHWND](functions/SETTAMAHWND.md)
- [LINT.GetFuncUsedBy](functions/LINT.GetFuncUsedBy.md)
- [LINT.GetGlobalVarLetted](functions/LINT.GetGlobalVarLetted.md)
- [LINT.GetGlobalVarUsedBy](functions/LINT.GetGlobalVarUsedBy.md)
- [LINT.GetLocalVarLetted](functions/LINT.GetLocalVarLetted.md)
- [LINT.GetLocalVarUsedBy](functions/LINT.GetLocalVarUsedBy.md)
- [LINT.GetUserDefFuncUsedBy](functions/LINT.GetUserDefFuncUsedBy.md)
- [LINT.GetVarRefs](functions/LINT.GetVarRefs.md)

---

## Tips

- [C言語利用者のためのヒント](tips/hints-for-c-users.md)
- [OnFileDrop2の使い方](tips/on-file-drop2.md)
- [OnTranslateの使い方](tips/on-translate-usage.md)
- [OnTranslateイベント](tips/on-translate-event.md)
- [SAKURAスクリプトタグをエスケープする](tips/escape-sakura-tags.md)
- [SAKURAスクリプトタグを取り除く](tips/remove-sakura-tags.md)
- [SAORIの使い方](tips/saori-usage.md)
- [caseを使って条件分岐で手抜きをする](tips/easy-case-branching.md)
- [xaoric.dllを使ったRSS読み取り](tips/xaoric-rss.md)
- [お気に入りを書きやすくする](tips/easy-favorites.md)
- [アンカータグからURLジャンプ](tips/url-jump-from-anchor.md)
- [エディタ色分けファイル](tips/editor-color-files.md)
- [ゴーストのインストール日時を取得する](tips/ghost-install-datetime.md)
- [ゴーストの起動と終了に確実に何かする](tips/reliable-boot-shutdown.md)
- [ゴースト切替えメッセージを変化させる](tips/ghost-switch-message.md)
- [ゴースト切替えメッセージを変化させる(新)](tips/ghost-switch-message-new.md)
- [サーフェス値加算](tips/surface-value-addition.md)
- [シェルの自由移動](tips/shell-free-movement.md)
- [ツールチップ](tips/tooltip.md)
- [テキストの幅を揃える](tips/align-text-width.md)
- [テキストファイルから汎用配列を作成](tips/create-array-from-text.md)
- [フォルダ重複をチェックする](tips/check-folder-duplicates.md)
- [ページング](tips/paging.md)
- [ホイール反応を自然なものにする](tips/natural-wheel-response.md)
- [マウス反応（なで反応）を自然なものにする](tips/natural-mouse-response.md)
- [メニューを横一ライン反転](tips/menu-horizontal-invert.md)
- [ユーザーの名前を覚える](tips/remember-username.md)
- [ランダムトークをさとりっぽく](tips/satori-style-random-talk.md)
- [中身の残っているディレクトリを削除する](tips/delete-nonempty-directory.md)
- [会話の途中で人格を切り替える](tips/switch-personality-mid-talk.md)
- [使用しているソフトを判別](tips/detect-software.md)
- [切り替え反応もいきなり独立した関数で書く](tips/independent-switch-function.md)
- [同時に違うことを喋る](tips/talk-different-simultaneously.md)
- [多重人格モード](tips/multiple-personality-mode.md)
- [指定秒数経過後にイベントを実行](tips/execute-after-seconds.md)
- [数当てゲーム](tips/number-guessing-game.md)
- [文のウソ・ホント](tips/talk-truth-lie.md)
- [文バトラー](tips/talk-battler.md)
- [日付イベント](tips/date-event.md)
- [日数計算](tips/day-count-calculation.md)
- [曜日を判別](tips/detect-weekday.md)
- [特殊文字を扱いたい](tips/handle-special-chars.md)
- [玉を使った辞書エラーチェック](tips/tama-error-check.md)
- [直前の会話をもう一度再生する](tips/replay-last-talk.md)
- [秒数を○時間○分○秒形式にする](tips/format-time-hms.md)
- [簡易配列→汎用配列の変換](tips/simple-to-generic-array.md)
- [簡易配列からメニューを構築する](tips/menu-from-array.md)
- [複雑な `_in_` チェック](tips/complex-in-check.md)
- [見切れ・重なり反応を里々風に](tips/collision-response-satolili-style.md)
- [誕生日を覚える](tips/remember-birthday.md)
- [起動してなかった時間により起動トークを変える](tips/vary-boot-talk-by-absence.md)
- [辞書の暗号化](tips/dictionary-encryption.md)
- [選択肢をいきなり独立した関数で書く](tips/independent-choice-function.md)
- [配列の要素数を取得](tips/get-array-size.md)
- [関数の返り値を捨てる](tips/discard-return-value.md)
- [関数・変数・さくらスクリプトを短縮して書く](tips/shorthand-writing.md)
- [音を鳴らす](tips/play-sound.md)
- [高速化](tips/optimization.md)
