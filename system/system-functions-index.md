# システム関数一覧

**Source:** マニュアル/システム関数

## 概要

YAYAに組み込まれているシステム関数の一覧。詳細は各関数のページ（`functions/` ディレクトリ）を参照。

## A-C

| 関数 | 説明 |
|------|------|
| [ACOS](../functions/ACOS.md) | アークコサインを返す（ラジアン） |
| [ANY](../functions/ANY.md) | 配列からランダムに1要素を選択 |
| [APPEND_RUNTIME_DIC](../functions/APPEND_RUNTIME_DIC.md) | ランタイム辞書に動的追記 |
| [ARRAYDEDUP](../functions/ARRAYDEDUP.md) | 配列から重複要素を削除 |
| [ARRAYSIZE](../functions/ARRAYSIZE.md) | 配列の要素数を返す |
| [ASEARCH](../functions/ASEARCH.md) | 配列を検索し最初の一致インデックスを返す |
| [ASEARCHEX](../functions/ASEARCHEX.md) | 配列を検索しすべての一致インデックスを返す |
| [ASIN](../functions/ASIN.md) | アークサインを返す（ラジアン） |
| [ASORT](../functions/ASORT.md) | 配列をソートする |
| [ATAN](../functions/ATAN.md) | アークタンジェントを返す（ラジアン） |
| [BINSTRTOI](../functions/BINSTRTOI.md) | 2進数文字列を整数に変換 |
| [BITWISE_AND](../functions/BITWISE_AND.md) | ビットAND |
| [BITWISE_NOT](../functions/BITWISE_NOT.md) | ビットNOT |
| [BITWISE_OR](../functions/BITWISE_OR.md) | ビットOR |
| [BITWISE_SHIFT](../functions/BITWISE_SHIFT.md) | ビットシフト |
| [BITWISE_XOR](../functions/BITWISE_XOR.md) | ビットXOR |
| [CEIL](../functions/CEIL.md) | 切り上げ |
| [CHARSETIDTOTEXT](../functions/CHARSETIDTOTEXT.md) | 文字コードIDをテキストに変換 |
| [CHARSETLIB](../functions/CHARSETLIB.md) | 外部ライブラリの文字コードを設定 |
| [CHARSETLIBEX](../functions/CHARSETLIBEX.md) | 特定の外部ライブラリの文字コードを設定 |
| [CHARSETTEXTTOID](../functions/CHARSETTEXTTOID.md) | 文字コードテキストをIDに変換 |
| [CHR](../functions/CHR.md) | UCS-2コードを文字に変換 |
| [CHRCODE](../functions/CHRCODE.md) | 文字のUCS-2コードを返す |
| [CLEARERRORLOG](../functions/CLEARERRORLOG.md) | エラーログをクリア |
| [COS](../functions/COS.md) | コサインを返す |
| [COSH](../functions/COSH.md) | 双曲線コサインを返す |
| [CUTSPACE](../functions/CUTSPACE.md) | 前後の空白・タブを除去 |
| [CVAUTO](../functions/CVAUTO.md) | 文字列を適切な型に自動変換 |
| [CVAUTOEX](../functions/CVAUTOEX.md) | CVAUTOの拡張版 |
| [CVINT](../functions/CVINT.md) | 変数を整数型に変換 |
| [CVREAL](../functions/CVREAL.md) | 変数を実数型に変換 |
| [CVSTR](../functions/CVSTR.md) | 変数を文字列型に変換 |

## D-F

| 関数 | 説明 |
|------|------|
| [DICLOAD](../functions/DICLOAD.md) | 辞書ファイルを読み込む |
| [DICUNLOAD](../functions/DICUNLOAD.md) | 辞書ファイルをアンロード |
| [DUMPVAR](../functions/DUMPVAR.md) | 変数をダンプ |
| [ERASE](../functions/ERASE.md) | 文字列から部分文字列を削除 |
| [ERASEVAR](../functions/ERASEVAR.md) | 変数を削除 |
| [EVAL](../functions/EVAL.md) | 文字列を式として評価 |
| [EXECUTE](../functions/EXECUTE.md) | 外部プログラムを実行 |
| [EXECUTE_WAIT](../functions/EXECUTE_WAIT.md) | 外部プログラムを実行して完了を待つ |
| [FATTRIB](../functions/FATTRIB.md) | ファイル属性を取得・設定 |
| [FCHARSET](../functions/FCHARSET.md) | ファイルの文字コードを設定 |
| [FCLOSE](../functions/FCLOSE.md) | ファイルを閉じる |
| [FCOPY](../functions/FCOPY.md) | ファイルをコピー |
| [FDEL](../functions/FDEL.md) | ファイルを削除 |
| [FDIGEST](../functions/FDIGEST.md) | ファイルのハッシュを計算 |
| [FENUM](../functions/FENUM.md) | ファイル・ディレクトリを列挙 |
| [FLOOR](../functions/FLOOR.md) | 切り捨て |
| [FMOVE](../functions/FMOVE.md) | ファイルを移動 |
| [FOPEN](../functions/FOPEN.md) | ファイルを開く |
| [FREAD](../functions/FREAD.md) | ファイルから読み込む |
| [FREADBIN](../functions/FREADBIN.md) | バイナリとしてファイルを読み込む |
| [FREADENCODE](../functions/FREADENCODE.md) | エンコード変換しながら読み込む |
| [FRENAME](../functions/FRENAME.md) | ファイルをリネーム |
| [FSEEK](../functions/FSEEK.md) | ファイルポインタを移動 |
| [FSIZE](../functions/FSIZE.md) | ファイルサイズを返す |
| [FSTATUS](../functions/FSTATUS.md) | ファイルI/O操作のステータスを返す |
| [FTELL](../functions/FTELL.md) | ファイルポインタ位置を返す |
| [FUNCDECL_ERASE](../functions/FUNCDECL_ERASE.md) | 動的関数宣言を削除 |
| [FUNCDECL_READ](../functions/FUNCDECL_READ.md) | 動的関数宣言を読み込む |
| [FUNCDECL_WRITE](../functions/FUNCDECL_WRITE.md) | 動的関数宣言を書き出す |
| [FUNCTIONEX](../functions/FUNCTIONEX.md) | 外部ライブラリ関数を呼び出す |
| [FWRITE](../functions/FWRITE.md) | ファイルに書き込む |
| [FWRITE2](../functions/FWRITE2.md) | ファイルに書き込む（改行付き） |
| [FWRITEBIN](../functions/FWRITEBIN.md) | バイナリとしてファイルに書き込む |
| [FWRITEDECODE](../functions/FWRITEDECODE.md) | デコード変換しながら書き込む |

## G-I

| 関数 | 説明 |
|------|------|
| [GETCALLSTACK](../functions/GETCALLSTACK.md) | 呼び出しスタックを取得 |
| [GETDELIM](../functions/GETDELIM.md) | 現在のデリミタを取得 |
| [GETENV](../functions/GETENV.md) | 環境変数を取得 |
| [GETERRORLOG](../functions/GETERRORLOG.md) | エラーログを取得 |
| [GETFUNCINFO](../functions/GETFUNCINFO.md) | 関数情報を取得 |
| [GETFUNCLIST](../functions/GETFUNCLIST.md) | ユーザー定義関数一覧を取得 |
| [GETLASTERROR](../functions/GETLASTERROR.md) | 最後のエラーコードを取得 |
| [GETMEMINFO](../functions/GETMEMINFO.md) | メモリ情報を取得 |
| [GETSECCOUNT](../functions/GETSECCOUNT.md) | 秒数カウントを取得 |
| [GETSETTING](../functions/GETSETTING.md) | 設定値を取得 |
| [GETSTRBYTES](../functions/GETSTRBYTES.md) | 文字列のバイト数を返す |
| [GETSYSTEMFUNCLIST](../functions/GETSYSTEMFUNCLIST.md) | システム関数一覧を取得 |
| [GETTICKCOUNT](../functions/GETTICKCOUNT.md) | ティックカウントを取得 |
| [GETTIME](../functions/GETTIME.md) | 現在時刻を取得 |
| [GETTYPE](../functions/GETTYPE.md) | 変数の型を返す |
| [GETTYPEEX](../functions/GETTYPEEX.md) | 変数の型を詳細に返す |
| [GETVARLIST](../functions/GETVARLIST.md) | グローバル変数一覧を取得 |
| [HAN2ZEN](../functions/HAN2ZEN.md) | 半角を全角に変換 |
| [HEXSTRTOI](../functions/HEXSTRTOI.md) | 16進数文字列を整数に変換 |
| [IARRAY](../functions/IARRAY.md) | 汎用配列の初期化値 |
| [INSERT](../functions/INSERT.md) | 文字列に文字列を挿入 |
| [ISEVALUABLE](../functions/ISEVALUABLE.md) | 式として評価可能か確認 |
| [ISFUNC](../functions/ISFUNC.md) | 関数が存在するか確認 |
| [ISGLOBALDEFINE](../functions/ISGLOBALDEFINE.md) | グローバル定義が存在するか確認 |
| [ISINTSTR](../functions/ISINTSTR.md) | 整数文字列か確認 |
| [ISREALSTR](../functions/ISREALSTR.md) | 実数文字列か確認 |
| [ISVAR](../functions/ISVAR.md) | 変数が存在するか確認 |

## J-P

| 関数 | 説明 |
|------|------|
| [LETTONAME](../functions/LETTONAME.md) | 変数名を動的に指定して代入 |
| [LICENSE](../functions/LICENSE.md) | ライセンス情報を表示 |
| [LINT.GetFuncUsedBy](../functions/LINT.GetFuncUsedBy.md) | 関数の使用箇所を取得（LINT） |
| [LINT.GetGlobalVarLetted](../functions/LINT.GetGlobalVarLetted.md) | グローバル変数の代入箇所を取得（LINT） |
| [LINT.GetGlobalVarUsedBy](../functions/LINT.GetGlobalVarUsedBy.md) | グローバル変数の使用箇所を取得（LINT） |
| [LINT.GetLocalVarLetted](../functions/LINT.GetLocalVarLetted.md) | ローカル変数の代入箇所を取得（LINT） |
| [LINT.GetLocalVarUsedBy](../functions/LINT.GetLocalVarUsedBy.md) | ローカル変数の使用箇所を取得（LINT） |
| [LINT.GetUserDefFuncUsedBy](../functions/LINT.GetUserDefFuncUsedBy.md) | ユーザー定義関数の使用箇所を取得（LINT） |
| [LOADLIB](../functions/LOADLIB.md) | 外部ライブラリを読み込む |
| [LOG](../functions/LOG.md) | 自然対数を返す |
| [LOG10](../functions/LOG10.md) | 常用対数を返す |
| [LOGGING](../functions/LOGGING.md) | ログに出力 |
| [LSO](../functions/LSO.md) | 最後に選択されたオプションのインデックスを返す |
| [MKDIR](../functions/MKDIR.md) | ディレクトリを作成 |
| [OUTPUTNUM](../functions/OUTPUTNUM.md) | 数値の出力書式を設定 |
| [POW](../functions/POW.md) | べき乗を返す |
| [PROCESSGLOBALDEFINE](../functions/PROCESSGLOBALDEFINE.md) | グローバル定義を処理 |

## Q-S

| 関数 | 説明 |
|------|------|
| [RAND](../functions/RAND.md) | 乱数を生成 |
| [READFMO](../functions/READFMO.md) | FMOからデータを読み込む |
| [REPLACE](../functions/REPLACE.md) | 文字列を置換 |
| [REQUESTLIB](../functions/REQUESTLIB.md) | 外部ライブラリにリクエストを送る |
| [RESTOREVAR](../functions/RESTOREVAR.md) | 変数を復元 |
| [RE_ASEARCH](../functions/RE_ASEARCH.md) | 正規表現で配列を検索 |
| [RE_ASEARCHEX](../functions/RE_ASEARCHEX.md) | 正規表現で配列を検索（全一致） |
| [RE_GETLEN](../functions/RE_GETLEN.md) | 正規表現マッチの長さを返す |
| [RE_GETPOS](../functions/RE_GETPOS.md) | 正規表現マッチの位置を返す |
| [RE_GETSTR](../functions/RE_GETSTR.md) | 正規表現マッチの文字列を返す |
| [RE_GREP](../functions/RE_GREP.md) | 正規表現でフィルタリング |
| [RE_MATCH](../functions/RE_MATCH.md) | 正規表現でマッチ確認 |
| [RE_OPTION](../functions/RE_OPTION.md) | 正規表現のオプションを設定 |
| [RE_REPLACE](../functions/RE_REPLACE.md) | 正規表現で置換 |
| [RE_REPLACEEX](../functions/RE_REPLACEEX.md) | 正規表現で置換（拡張） |
| [RE_SEARCH](../functions/RE_SEARCH.md) | 正規表現で検索 |
| [RE_SPLIT](../functions/RE_SPLIT.md) | 正規表現で分割 |
| [RMDIR](../functions/RMDIR.md) | ディレクトリを削除 |
| [ROUND](../functions/ROUND.md) | 四捨五入 |
| [SAVEVAR](../functions/SAVEVAR.md) | 変数を保存 |
| [SETDELIM](../functions/SETDELIM.md) | デリミタを設定 |
| [SETGLOBALDEFINE](../functions/SETGLOBALDEFINE.md) | グローバル定義を設定 |
| [SETLASTERROR](../functions/SETLASTERROR.md) | 最後のエラーコードを設定 |
| [SETSETTING](../functions/SETSETTING.md) | 設定値を変更 |
| [SETTAMAHWND](../functions/SETTAMAHWND.md) | 玉のウィンドウハンドルを設定 |
| [SIN](../functions/SIN.md) | サインを返す |
| [SINH](../functions/SINH.md) | 双曲線サインを返す |
| [SLEEP](../functions/SLEEP.md) | 処理を一時停止 |
| [SPLIT](../functions/SPLIT.md) | 文字列を分割して配列を返す |
| [SPLITPATH](../functions/SPLITPATH.md) | パスを分解 |
| [SQRT](../functions/SQRT.md) | 平方根を返す |
| [SRAND](../functions/SRAND.md) | 乱数シードを設定 |
| [STRDECODE](../functions/STRDECODE.md) | 文字列をデコード |
| [STRDIGEST](../functions/STRDIGEST.md) | 文字列のハッシュを計算 |
| [STRENCODE](../functions/STRENCODE.md) | 文字列をエンコード |
| [STRFORM](../functions/STRFORM.md) | 書式化文字列を生成 |
| [STRLEN](../functions/STRLEN.md) | 文字列の長さを返す |
| [STRSTR](../functions/STRSTR.md) | 文字列を検索 |
| [SUBSTR](../functions/SUBSTR.md) | 部分文字列を取得 |

## T-Z

| 関数 | 説明 |
|------|------|
| [TAN](../functions/TAN.md) | タンジェントを返す |
| [TANH](../functions/TANH.md) | 双曲線タンジェントを返す |
| [TOAUTO](../functions/TOAUTO.md) | 値を自動的に適切な型に変換 |
| [TOAUTOEX](../functions/TOAUTOEX.md) | TOAUTOの拡張版 |
| [TOBINSTR](../functions/TOBINSTR.md) | 整数を2進数文字列に変換 |
| [TOHEXSTR](../functions/TOHEXSTR.md) | 整数を16進数文字列に変換 |
| [TOINT](../functions/TOINT.md) | 値を整数に変換 |
| [TOLOWER](../functions/TOLOWER.md) | 文字列を小文字に変換 |
| [TOREAL](../functions/TOREAL.md) | 値を実数に変換 |
| [TOSTR](../functions/TOSTR.md) | 値を文字列に変換 |
| [TOUPPER](../functions/TOUPPER.md) | 文字列を大文字に変換 |
| [TRANSLATE](../functions/TRANSLATE.md) | 文字列を変換 |
| [UNDEFFUNC](../functions/UNDEFFUNC.md) | 関数定義を削除 |
| [UNDEFGLOBALDEFINE](../functions/UNDEFGLOBALDEFINE.md) | グローバル定義を削除 |
| [UNLOADLIB](../functions/UNLOADLIB.md) | 外部ライブラリをアンロード |
| [ZEN2HAN](../functions/ZEN2HAN.md) | 全角を半角に変換 |
