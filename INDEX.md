# YAYA マニュアル INDEX

伺かのSHIORI「YAYA」言語マニュアルのMarkdown版インデックス。

元ソース: https://emily.shillest.net/ayaya/

---

## マニュアル/文法 (grammar/)

| ファイル | 内容 |
|---------|------|
| [01-basic-settings.md](grammar/01-basic-settings.md) | 基本設定 |
| [02-functions.md](grammar/02-functions.md) | 関数 |
| [03-values-and-variables.md](grammar/03-values-and-variables.md) | 値と変数 |
| [04-arithmetic.md](grammar/04-arithmetic.md) | 算術演算 |
| [05-arrays.md](grammar/05-arrays.md) | 配列 |
| [06-string-embedding.md](grammar/06-string-embedding.md) | 文字列埋め込み |
| [07-flow-control.md](grammar/07-flow-control.md) | フロー制御 |
| [08-preprocessor.md](grammar/08-preprocessor.md) | プリプロセッサ |
| [09-reserved-words.md](grammar/09-reserved-words.md) | 予約語 |
| [10-yaya-as-windows-dll.md](grammar/10-yaya-as-windows-dll.md) | Windows DLLとしてのYAYA |
| [11-character-encoding.md](grammar/11-character-encoding.md) | 文字コード |

---

## マニュアル/基本 (basic/)

| ファイル | 内容 |
|---------|------|
| [variables.md](basic/variables.md) | 変数 |
| [functions.md](basic/functions.md) | 関数 |
| [branching.md](basic/branching.md) | 条件分岐 |
| [loops.md](basic/loops.md) | ループ |
| [arrays.md](basic/arrays.md) | 配列 |
| [operators.md](basic/operators.md) | 演算子 |

---

## システム辞書 (system/)

| ファイル | 内容 |
|---------|------|
| [yaya-shiori3-dic.md](system/yaya-shiori3-dic.md) | yaya_shiori3.dic |
| [yaya-optional-dic.md](system/yaya-optional-dic.md) | yaya_optional.dic |
| [system-functions-index.md](system/system-functions-index.md) | システム関数一覧 |
| [error-handling-functions.md](system/error-handling-functions.md) | エラー処理関数 |
| [shiori-OnCallLimit.md](system/shiori-OnCallLimit.md) | OnCallLimit |
| [shiori-OnLoopLimit.md](system/shiori-OnLoopLimit.md) | OnLoopLimit |
| [shiori-OnMemoryError.md](system/shiori-OnMemoryError.md) | OnMemoryError |
| [shiori-OnMemoryLimit.md](system/shiori-OnMemoryLimit.md) | OnMemoryLimit |

---

## StartUp / チュートリアル (startup/)

| ファイル | 内容 |
|---------|------|
| [creating-ghost.md](startup/creating-ghost.md) | ゴーストの作り方 |
| [tutorial-01-preparation.md](startup/tutorial-01-preparation.md) | チュートリアル1: 準備 |
| [tutorial-02-writing-dialogue.md](startup/tutorial-02-writing-dialogue.md) | チュートリアル2: セリフを書く |
| [tutorial-03-variables.md](startup/tutorial-03-variables.md) | チュートリアル3: 変数 |
| [migration-from-aya.md](startup/migration-from-aya.md) | AYAからの移行 |
| [migration-from-satolili.md](startup/migration-from-satolili.md) | 里々からの移行 |

---

## その他 (other/)

| ファイル | 内容 |
|---------|------|
| [yaya.md](other/yaya.md) | YAYAについて |
| [yaya-as-saori.md](other/yaya-as-saori.md) | SAORIとしてのYAYA |
| [yaya-as-makoto.md](other/yaya-as-makoto.md) | MAKOTOとしてのYAYA |
| [yaya-as-plugin.md](other/yaya-as-plugin.md) | プラグインとしてのYAYA |
| [saori-usage.md](other/saori-usage.md) | SAORIの使い方 |
| [talklib.md](other/talklib.md) | talklib |
| [simple-yaya-template.md](other/simple-yaya-template.md) | シンプルなYAYAテンプレート |
| [troubleshooting.md](other/troubleshooting.md) | トラブルシューティング |

---

## マニュアル/関数 (functions/)

### 型取得/変換

| ファイル | 関数 |
|---------|------|
| [GETTYPE.md](functions/GETTYPE.md) | GETTYPE |
| [GETTYPEEX.md](functions/GETTYPEEX.md) | GETTYPEEX |
| [TOINT.md](functions/TOINT.md) | TOINT |
| [TOREAL.md](functions/TOREAL.md) | TOREAL |
| [TOSTR.md](functions/TOSTR.md) | TOSTR |
| [TOAUTO.md](functions/TOAUTO.md) | TOAUTO |
| [TOAUTOEX.md](functions/TOAUTOEX.md) | TOAUTOEX |
| [ISFUNC.md](functions/ISFUNC.md) | ISFUNC |
| [ISVAR.md](functions/ISVAR.md) | ISVAR |
| [CVINT.md](functions/CVINT.md) | CVINT |
| [CVSTR.md](functions/CVSTR.md) | CVSTR |
| [CVREAL.md](functions/CVREAL.md) | CVREAL |
| [CVAUTO.md](functions/CVAUTO.md) | CVAUTO |
| [CVAUTOEX.md](functions/CVAUTOEX.md) | CVAUTOEX |

### 配列操作

| ファイル | 関数 |
|---------|------|
| [ARRAYSIZE.md](functions/ARRAYSIZE.md) | ARRAYSIZE |
| [ARRAYDEDUP.md](functions/ARRAYDEDUP.md) | ARRAYDEDUP |
| [ASEARCH.md](functions/ASEARCH.md) | ASEARCH |
| [ASEARCHEX.md](functions/ASEARCHEX.md) | ASEARCHEX |
| [ASORT.md](functions/ASORT.md) | ASORT |
| [SETDELIM.md](functions/SETDELIM.md) | SETDELIM |
| [GETDELIM.md](functions/GETDELIM.md) | GETDELIM |
| [IARRAY.md](functions/IARRAY.md) | IARRAY |

### 文字列操作

| ファイル | 関数 |
|---------|------|
| [ANY.md](functions/ANY.md) | ANY |
| [CHR.md](functions/CHR.md) | CHR |
| [CHRCODE.md](functions/CHRCODE.md) | CHRCODE |
| [CUTSPACE.md](functions/CUTSPACE.md) | CUTSPACE |
| [ERASE.md](functions/ERASE.md) | ERASE |
| [GETSTRBYTES.md](functions/GETSTRBYTES.md) | GETSTRBYTES |
| [HAN2ZEN.md](functions/HAN2ZEN.md) | HAN2ZEN |
| [HEXSTRTOI.md](functions/HEXSTRTOI.md) | HEXSTRTOI |
| [BINSTRTOI.md](functions/BINSTRTOI.md) | BINSTRTOI |
| [INSERT.md](functions/INSERT.md) | INSERT |
| [ISINTSTR.md](functions/ISINTSTR.md) | ISINTSTR |
| [ISREALSTR.md](functions/ISREALSTR.md) | ISREALSTR |
| [REPLACE.md](functions/REPLACE.md) | REPLACE |
| [SPLIT.md](functions/SPLIT.md) | SPLIT |
| [SPLITPATH.md](functions/SPLITPATH.md) | SPLITPATH |
| [STRDIGEST.md](functions/STRDIGEST.md) | STRDIGEST |
| [STRDECODE.md](functions/STRDECODE.md) | STRDECODE |
| [STRENCODE.md](functions/STRENCODE.md) | STRENCODE |
| [STRFORM.md](functions/STRFORM.md) | STRFORM |
| [STRLEN.md](functions/STRLEN.md) | STRLEN |
| [STRSTR.md](functions/STRSTR.md) | STRSTR |
| [SUBSTR.md](functions/SUBSTR.md) | SUBSTR |
| [TOBINSTR.md](functions/TOBINSTR.md) | TOBINSTR |
| [TOHEXSTR.md](functions/TOHEXSTR.md) | TOHEXSTR |
| [TOLOWER.md](functions/TOLOWER.md) | TOLOWER |
| [TOUPPER.md](functions/TOUPPER.md) | TOUPPER |
| [TRANSLATE.md](functions/TRANSLATE.md) | TRANSLATE |
| [ZEN2HAN.md](functions/ZEN2HAN.md) | ZEN2HAN |

### 正規表現

| ファイル | 関数 |
|---------|------|
| [RE_SEARCH.md](functions/RE_SEARCH.md) | RE_SEARCH |
| [RE_MATCH.md](functions/RE_MATCH.md) | RE_MATCH |
| [RE_GREP.md](functions/RE_GREP.md) | RE_GREP |
| [RE_REPLACE.md](functions/RE_REPLACE.md) | RE_REPLACE |
| [RE_REPLACEEX.md](functions/RE_REPLACEEX.md) | RE_REPLACEEX |
| [RE_SPLIT.md](functions/RE_SPLIT.md) | RE_SPLIT |
| [RE_GETSTR.md](functions/RE_GETSTR.md) | RE_GETSTR |
| [RE_GETPOS.md](functions/RE_GETPOS.md) | RE_GETPOS |
| [RE_GETLEN.md](functions/RE_GETLEN.md) | RE_GETLEN |
| [RE_ASEARCH.md](functions/RE_ASEARCH.md) | RE_ASEARCH |
| [RE_ASEARCHEX.md](functions/RE_ASEARCHEX.md) | RE_ASEARCHEX |
| [RE_OPTION.md](functions/RE_OPTION.md) | RE_OPTION |

### 数学関数

| ファイル | 関数 |
|---------|------|
| [RAND.md](functions/RAND.md) | RAND |
| [SRAND.md](functions/SRAND.md) | SRAND |
| [FLOOR.md](functions/FLOOR.md) | FLOOR |
| [CEIL.md](functions/CEIL.md) | CEIL |
| [ROUND.md](functions/ROUND.md) | ROUND |
| [SIN.md](functions/SIN.md) | SIN |
| [COS.md](functions/COS.md) | COS |
| [TAN.md](functions/TAN.md) | TAN |
| [ASIN.md](functions/ASIN.md) | ASIN |
| [ACOS.md](functions/ACOS.md) | ACOS |
| [ATAN.md](functions/ATAN.md) | ATAN |
| [SINH.md](functions/SINH.md) | SINH |
| [COSH.md](functions/COSH.md) | COSH |
| [TANH.md](functions/TANH.md) | TANH |
| [LOG.md](functions/LOG.md) | LOG |
| [LOG10.md](functions/LOG10.md) | LOG10 |
| [POW.md](functions/POW.md) | POW |
| [SQRT.md](functions/SQRT.md) | SQRT |

### ビット演算

| ファイル | 関数 |
|---------|------|
| [BITWISE_AND.md](functions/BITWISE_AND.md) | BITWISE_AND |
| [BITWISE_OR.md](functions/BITWISE_OR.md) | BITWISE_OR |
| [BITWISE_XOR.md](functions/BITWISE_XOR.md) | BITWISE_XOR |
| [BITWISE_NOT.md](functions/BITWISE_NOT.md) | BITWISE_NOT |
| [BITWISE_SHIFT.md](functions/BITWISE_SHIFT.md) | BITWISE_SHIFT |

### ファイル操作

| ファイル | 関数 |
|---------|------|
| [FOPEN.md](functions/FOPEN.md) | FOPEN |
| [FCLOSE.md](functions/FCLOSE.md) | FCLOSE |
| [FREAD.md](functions/FREAD.md) | FREAD |
| [FREADENCODE.md](functions/FREADENCODE.md) | FREADENCODE |
| [FREADBIN.md](functions/FREADBIN.md) | FREADBIN |
| [FWRITE.md](functions/FWRITE.md) | FWRITE |
| [FWRITE2.md](functions/FWRITE2.md) | FWRITE2 |
| [FWRITEBIN.md](functions/FWRITEBIN.md) | FWRITEBIN |
| [FWRITEDECODE.md](functions/FWRITEDECODE.md) | FWRITEDECODE |
| [FCOPY.md](functions/FCOPY.md) | FCOPY |
| [FMOVE.md](functions/FMOVE.md) | FMOVE |
| [FDEL.md](functions/FDEL.md) | FDEL |
| [FRENAME.md](functions/FRENAME.md) | FRENAME |
| [FSIZE.md](functions/FSIZE.md) | FSIZE |
| [FENUM.md](functions/FENUM.md) | FENUM |
| [FCHARSET.md](functions/FCHARSET.md) | FCHARSET |
| [FATTRIB.md](functions/FATTRIB.md) | FATTRIB |
| [FDIGEST.md](functions/FDIGEST.md) | FDIGEST |
| [FSEEK.md](functions/FSEEK.md) | FSEEK |
| [FTELL.md](functions/FTELL.md) | FTELL |
| [MKDIR.md](functions/MKDIR.md) | MKDIR |
| [RMDIR.md](functions/RMDIR.md) | RMDIR |

### 外部ライブラリ

| ファイル | 関数 |
|---------|------|
| [LOADLIB.md](functions/LOADLIB.md) | LOADLIB |
| [UNLOADLIB.md](functions/UNLOADLIB.md) | UNLOADLIB |
| [REQUESTLIB.md](functions/REQUESTLIB.md) | REQUESTLIB |
| [FUNCTIONEX.md](functions/FUNCTIONEX.md) | FUNCTIONEX |
| [CHARSETLIB.md](functions/CHARSETLIB.md) | CHARSETLIB |
| [CHARSETLIBEX.md](functions/CHARSETLIBEX.md) | CHARSETLIBEX |

### システム情報

| ファイル | 関数 |
|---------|------|
| [GETTIME.md](functions/GETTIME.md) | GETTIME |
| [GETTICKCOUNT.md](functions/GETTICKCOUNT.md) | GETTICKCOUNT |
| [GETSECCOUNT.md](functions/GETSECCOUNT.md) | GETSECCOUNT |
| [GETMEMINFO.md](functions/GETMEMINFO.md) | GETMEMINFO |
| [GETENV.md](functions/GETENV.md) | GETENV |
| [READFMO.md](functions/READFMO.md) | READFMO |

### メタ操作・特殊関数

| ファイル | 関数 |
|---------|------|
| [EVAL.md](functions/EVAL.md) | EVAL |
| [ISEVALUABLE.md](functions/ISEVALUABLE.md) | ISEVALUABLE |
| [ERASEVAR.md](functions/ERASEVAR.md) | ERASEVAR |
| [LETTONAME.md](functions/LETTONAME.md) | LETTONAME |
| [LSO.md](functions/LSO.md) | LSO |
| [SAVEVAR.md](functions/SAVEVAR.md) | SAVEVAR |
| [RESTOREVAR.md](functions/RESTOREVAR.md) | RESTOREVAR |
| [GETSETTING.md](functions/GETSETTING.md) | GETSETTING |
| [SETSETTING.md](functions/SETSETTING.md) | SETSETTING |
| [GETFUNCLIST.md](functions/GETFUNCLIST.md) | GETFUNCLIST |
| [GETFUNCINFO.md](functions/GETFUNCINFO.md) | GETFUNCINFO |
| [GETVARLIST.md](functions/GETVARLIST.md) | GETVARLIST |
| [GETSYSTEMFUNCLIST.md](functions/GETSYSTEMFUNCLIST.md) | GETSYSTEMFUNCLIST |
| [GETCALLSTACK.md](functions/GETCALLSTACK.md) | GETCALLSTACK |
| [CHARSETTEXTTOID.md](functions/CHARSETTEXTTOID.md) | CHARSETTEXTTOID |
| [CHARSETIDTOTEXT.md](functions/CHARSETIDTOTEXT.md) | CHARSETIDTOTEXT |
| [EXECUTE.md](functions/EXECUTE.md) | EXECUTE |
| [EXECUTE_WAIT.md](functions/EXECUTE_WAIT.md) | EXECUTE_WAIT |
| [LICENSE.md](functions/LICENSE.md) | LICENSE |
| [APPEND_RUNTIME_DIC.md](functions/APPEND_RUNTIME_DIC.md) | APPEND_RUNTIME_DIC |
| [OUTPUTNUM.md](functions/OUTPUTNUM.md) | OUTPUTNUM |
| [DICLOAD.md](functions/DICLOAD.md) | DICLOAD |
| [DICUNLOAD.md](functions/DICUNLOAD.md) | DICUNLOAD |
| [FUNCDECL_ERASE.md](functions/FUNCDECL_ERASE.md) | FUNCDECL_ERASE |
| [FUNCDECL_READ.md](functions/FUNCDECL_READ.md) | FUNCDECL_READ |
| [FUNCDECL_WRITE.md](functions/FUNCDECL_WRITE.md) | FUNCDECL_WRITE |
| [UNDEFFUNC.md](functions/UNDEFFUNC.md) | UNDEFFUNC |
| [ISGLOBALDEFINE.md](functions/ISGLOBALDEFINE.md) | ISGLOBALDEFINE |
| [PROCESSGLOBALDEFINE.md](functions/PROCESSGLOBALDEFINE.md) | PROCESSGLOBALDEFINE |
| [SETGLOBALDEFINE.md](functions/SETGLOBALDEFINE.md) | SETGLOBALDEFINE |
| [UNDEFGLOBALDEFINE.md](functions/UNDEFGLOBALDEFINE.md) | UNDEFGLOBALDEFINE |

### 通信・プロセス間通信

| ファイル | 関数 |
|---------|------|
| [DIRECTSSTP.md](functions/DIRECTSSTP.md) | DIRECTSSTP |

### デバッグ

| ファイル | 関数 |
|---------|------|
| [LOGGING.md](functions/LOGGING.md) | LOGGING |
| [GETLASTERROR.md](functions/GETLASTERROR.md) | GETLASTERROR |
| [SETLASTERROR.md](functions/SETLASTERROR.md) | SETLASTERROR |
| [GETERRORLOG.md](functions/GETERRORLOG.md) | GETERRORLOG |
| [CLEARERRORLOG.md](functions/CLEARERRORLOG.md) | CLEARERRORLOG |
| [DUMPVAR.md](functions/DUMPVAR.md) | DUMPVAR |
| [SLEEP.md](functions/SLEEP.md) | SLEEP |
| [SETTAMAHWND.md](functions/SETTAMAHWND.md) | SETTAMAHWND |
| [LINT.GetFuncUsedBy.md](functions/LINT.GetFuncUsedBy.md) | LINT.GetFuncUsedBy |
| [LINT.GetGlobalVarLetted.md](functions/LINT.GetGlobalVarLetted.md) | LINT.GetGlobalVarLetted |
| [LINT.GetGlobalVarUsedBy.md](functions/LINT.GetGlobalVarUsedBy.md) | LINT.GetGlobalVarUsedBy |
| [LINT.GetLocalVarLetted.md](functions/LINT.GetLocalVarLetted.md) | LINT.GetLocalVarLetted |
| [LINT.GetLocalVarUsedBy.md](functions/LINT.GetLocalVarUsedBy.md) | LINT.GetLocalVarUsedBy |
| [LINT.GetUserDefFuncUsedBy.md](functions/LINT.GetUserDefFuncUsedBy.md) | LINT.GetUserDefFuncUsedBy |

---

## Tips (tips/)

| ファイル | 内容 |
|---------|------|
| [hints-for-c-users.md](tips/hints-for-c-users.md) | C言語利用者のためのヒント |
| [on-file-drop2.md](tips/on-file-drop2.md) | OnFileDrop2の使い方 |
| [on-translate-usage.md](tips/on-translate-usage.md) | OnTranslateの使い方 |
| [on-translate-event.md](tips/on-translate-event.md) | OnTranslateイベント |
| [escape-sakura-tags.md](tips/escape-sakura-tags.md) | SAKURAスクリプトタグをエスケープする |
| [remove-sakura-tags.md](tips/remove-sakura-tags.md) | SAKURAスクリプトタグを取り除く |
| [saori-usage.md](tips/saori-usage.md) | SAORIの使い方 |
| [easy-case-branching.md](tips/easy-case-branching.md) | caseを使って条件分岐で手抜きをする |
| [xaoric-rss.md](tips/xaoric-rss.md) | xaoric.dllを使ったRSS読み取り |
| [easy-favorites.md](tips/easy-favorites.md) | お気に入りを書きやすくする |
| [url-jump-from-anchor.md](tips/url-jump-from-anchor.md) | アンカータグからURLジャンプ |
| [editor-color-files.md](tips/editor-color-files.md) | エディタ色分けファイル |
| [ghost-install-datetime.md](tips/ghost-install-datetime.md) | ゴーストのインストール日時を取得する |
| [reliable-boot-shutdown.md](tips/reliable-boot-shutdown.md) | ゴーストの起動と終了に確実に何かする |
| [ghost-switch-message.md](tips/ghost-switch-message.md) | ゴースト切替えメッセージを変化させる |
| [ghost-switch-message-new.md](tips/ghost-switch-message-new.md) | ゴースト切替えメッセージを変化させる(新) |
| [surface-value-addition.md](tips/surface-value-addition.md) | サーフェス値加算 |
| [shell-free-movement.md](tips/shell-free-movement.md) | シェルの自由移動 |
| [tooltip.md](tips/tooltip.md) | ツールチップ |
| [align-text-width.md](tips/align-text-width.md) | テキストの幅を揃える |
| [create-array-from-text.md](tips/create-array-from-text.md) | テキストファイルから汎用配列を作成 |
| [check-folder-duplicates.md](tips/check-folder-duplicates.md) | フォルダ重複をチェックする |
| [paging.md](tips/paging.md) | ページング |
| [natural-wheel-response.md](tips/natural-wheel-response.md) | ホイール反応を自然なものにする |
| [natural-mouse-response.md](tips/natural-mouse-response.md) | マウス反応（なで反応）を自然なものにする |
| [menu-horizontal-invert.md](tips/menu-horizontal-invert.md) | メニューを横一ライン反転 |
| [remember-username.md](tips/remember-username.md) | ユーザーの名前を覚える |
| [satori-style-random-talk.md](tips/satori-style-random-talk.md) | ランダムトークをさとりっぽく |
| [delete-nonempty-directory.md](tips/delete-nonempty-directory.md) | 中身の残っているディレクトリを削除する |
| [switch-personality-mid-talk.md](tips/switch-personality-mid-talk.md) | 会話の途中で人格を切り替える |
| [detect-software.md](tips/detect-software.md) | 使用しているソフトを判別 |
| [independent-switch-function.md](tips/independent-switch-function.md) | 切り替え反応もいきなり独立した関数で書く |
| [talk-different-simultaneously.md](tips/talk-different-simultaneously.md) | 同時に違うことを喋る |
| [multiple-personality-mode.md](tips/multiple-personality-mode.md) | 多重人格モード |
| [execute-after-seconds.md](tips/execute-after-seconds.md) | 指定秒数経過後にイベントを実行 |
| [number-guessing-game.md](tips/number-guessing-game.md) | 数当てゲーム |
| [talk-truth-lie.md](tips/talk-truth-lie.md) | 文のウソ・ホント |
| [talk-battler.md](tips/talk-battler.md) | 文バトラー |
| [date-event.md](tips/date-event.md) | 日付イベント |
| [day-count-calculation.md](tips/day-count-calculation.md) | 日数計算 |
| [detect-weekday.md](tips/detect-weekday.md) | 曜日を判別 |
| [handle-special-chars.md](tips/handle-special-chars.md) | 特殊文字を扱いたい |
| [tama-error-check.md](tips/tama-error-check.md) | 玉を使った辞書エラーチェック |
| [replay-last-talk.md](tips/replay-last-talk.md) | 直前の会話をもう一度再生する |
| [format-time-hms.md](tips/format-time-hms.md) | 秒数を○時間○分○秒形式にする |
| [simple-to-generic-array.md](tips/simple-to-generic-array.md) | 簡易配列→汎用配列の変換 |
| [menu-from-array.md](tips/menu-from-array.md) | 簡易配列からメニューを構築する |
| [complex-in-check.md](tips/complex-in-check.md) | 複雑な _in_ チェック |
| [collision-response-satolili-style.md](tips/collision-response-satolili-style.md) | 見切れ・重なり反応を里々風に |
| [remember-birthday.md](tips/remember-birthday.md) | 誕生日を覚える |
| [vary-boot-talk-by-absence.md](tips/vary-boot-talk-by-absence.md) | 起動してなかった時間により起動トークを変える |
| [dictionary-encryption.md](tips/dictionary-encryption.md) | 辞書の暗号化 |
| [independent-choice-function.md](tips/independent-choice-function.md) | 選択肢をいきなり独立した関数で書く |
| [get-array-size.md](tips/get-array-size.md) | 配列の要素数を取得 |
| [discard-return-value.md](tips/discard-return-value.md) | 関数の返り値を捨てる |
| [shorthand-writing.md](tips/shorthand-writing.md) | 関数・変数・さくらスクリプトを短縮して書く |
| [play-sound.md](tips/play-sound.md) | 音を鳴らす |
| [optimization.md](tips/optimization.md) | 高速化 |
