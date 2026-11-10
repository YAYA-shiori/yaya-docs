# 系統函式一覽

## 概要

YAYA 內建的系統函式一覽。詳細資訊請參閱各函式的頁面（`functions/` 目錄）。

## A-C

| 函式 | 說明 |
|------|------|
| [ACOS](../functions/ACOS.md) | 傳回反餘弦（弧度） |
| [ANY](../functions/ANY.md) | 從陣列中隨機選取 1 個元素 |
| [APPEND_RUNTIME_DIC](../functions/APPEND_RUNTIME_DIC.md) | 動態追加至執行階段辭典 |
| [ARRAYDEDUP](../functions/ARRAYDEDUP.md) | 移除陣列中的重複元素 |
| [ARRAYSIZE](../functions/ARRAYSIZE.md) | 傳回陣列的元素數量 |
| [ASEARCH](../functions/ASEARCH.md) | 搜尋陣列並傳回第一個符合項目的索引 |
| [ASEARCHEX](../functions/ASEARCHEX.md) | 搜尋陣列並傳回所有符合項目的索引 |
| [ASIN](../functions/ASIN.md) | 傳回反正弦（弧度） |
| [ASORT](../functions/ASORT.md) | 排序陣列 |
| [ATAN](../functions/ATAN.md) | 傳回反正切（弧度） |
| [BINSTRTOI](../functions/BINSTRTOI.md) | 將二進位字串轉換為整數 |
| [BITWISE_AND](../functions/BITWISE_AND.md) | 位元 AND |
| [BITWISE_NOT](../functions/BITWISE_NOT.md) | 位元 NOT |
| [BITWISE_OR](../functions/BITWISE_OR.md) | 位元 OR |
| [BITWISE_SHIFT](../functions/BITWISE_SHIFT.md) | 位元移位 |
| [BITWISE_XOR](../functions/BITWISE_XOR.md) | 位元 XOR |
| [CEIL](../functions/CEIL.md) | 無條件進位 |
| [CHARSETIDTOTEXT](../functions/CHARSETIDTOTEXT.md) | 將字元編碼 ID 轉換為文字 |
| [CHARSETLIB](../functions/CHARSETLIB.md) | 設定外部程式庫的字元編碼 |
| [CHARSETLIBEX](../functions/CHARSETLIBEX.md) | 設定特定外部程式庫的字元編碼 |
| [CHARSETTEXTTOID](../functions/CHARSETTEXTTOID.md) | 將字元編碼文字轉換為 ID |
| [CHR](../functions/CHR.md) | 將 UCS-2 碼轉換為字元 |
| [CHRCODE](../functions/CHRCODE.md) | 傳回字元的 UCS-2 碼 |
| [CLEARERRORLOG](../functions/CLEARERRORLOG.md) | 清除錯誤記錄 |
| [COS](../functions/COS.md) | 傳回餘弦 |
| [COSH](../functions/COSH.md) | 傳回雙曲餘弦 |
| [CUTSPACE](../functions/CUTSPACE.md) | 移除前後的空白與定位字元 |
| [CVAUTO](../functions/CVAUTO.md) | 自動將字串轉換為適當的型別 |
| [CVAUTOEX](../functions/CVAUTOEX.md) | CVAUTO 的擴充版 |
| [CVINT](../functions/CVINT.md) | 將變數轉換為整數型別 |
| [CVREAL](../functions/CVREAL.md) | 將變數轉換為實數型別 |
| [CVSTR](../functions/CVSTR.md) | 將變數轉換為字串型別 |

## D-F

| 函式 | 說明 |
|------|------|
| [DESERIALIZEVAR](../functions/DESERIALIZEVAR.md) | 從 SERIALIZEVAR 的字串還原變數（Tc607-3 以後） |
| [DICLOAD](../functions/DICLOAD.md) | 載入辭典檔案 |
| [DICUNLOAD](../functions/DICUNLOAD.md) | 卸載辭典檔案 |
| [DUMPJSON](../functions/DUMPJSON.md) | 將值轉換為 JSON 字串（Tc602-1 以後） |
| [DUMPTOML](../functions/DUMPTOML.md) | 將雜湊轉換為 TOML 字串（Tc602-5 以後） |
| [DUMPVAR](../functions/DUMPVAR.md) | 傾印變數 |
| [DUMPXML](../functions/DUMPXML.md) | 將元素的雜湊轉換為 XML 字串（Tc602-1 以後） |
| [DUMPYAML](../functions/DUMPYAML.md) | 將值轉換為 YAML 字串（Tc602-5 以後） |
| [ERASE](../functions/ERASE.md) | 從字串中刪除子字串 |
| [ERASEVAR](../functions/ERASEVAR.md) | 刪除變數 |
| [EVAL](../functions/EVAL.md) | 將字串作為運算式或陳述式序列進行評估 |
| [EXECUTE](../functions/EXECUTE.md) | 執行外部程式 |
| [EXECUTE_CAPTURE](../functions/EXECUTE_CAPTURE.md) | 執行外部程式，傳入標準輸入並擷取標準輸出與標準錯誤輸出（Tc608-3 以後） |
| [EXECUTE_WAIT](../functions/EXECUTE_WAIT.md) | 執行外部程式並等待其完成 |
| [FATTRIB](../functions/FATTRIB.md) | 取得或設定檔案屬性 |
| [FCHARSET](../functions/FCHARSET.md) | 設定檔案的字元編碼 |
| [FCLOSE](../functions/FCLOSE.md) | 關閉檔案 |
| [FCOPY](../functions/FCOPY.md) | 複製檔案 |
| [FDEL](../functions/FDEL.md) | 刪除檔案 |
| [FDIGEST](../functions/FDIGEST.md) | 計算檔案的雜湊值 |
| [FENUM](../functions/FENUM.md) | 列舉檔案與目錄 |
| [FLOOR](../functions/FLOOR.md) | 無條件捨去 |
| [FMOVE](../functions/FMOVE.md) | 移動檔案 |
| [FOPEN](../functions/FOPEN.md) | 開啟檔案 |
| [FREAD](../functions/FREAD.md) | 從檔案讀取 |
| [FREADBIN](../functions/FREADBIN.md) | 將檔案作為二進位資料讀取 |
| [FREADENCODE](../functions/FREADENCODE.md) | 轉換編碼後讀取 |
| [FREADHTML](../functions/FREADHTML.md) | 一次讀取整個 HTML 檔案並轉換為雜湊（Tc605-1 以後） |
| [FREADJSON](../functions/FREADJSON.md) | 一次讀取整個 JSON 檔案並轉換為雜湊或陣列（Tc601-1 以後） |
| [FREADTOML](../functions/FREADTOML.md) | 一次讀取整個 TOML 檔案並轉換為雜湊（Tc602-5 以後） |
| [FREADXML](../functions/FREADXML.md) | 一次讀取整個 XML 檔案並轉換為雜湊（Tc601-1 以後） |
| [FREADYAML](../functions/FREADYAML.md) | 一次讀取整個 YAML 檔案並轉換為雜湊或陣列（Tc602-5 以後） |
| [FRENAME](../functions/FRENAME.md) | 重新命名檔案 |
| [FSEEK](../functions/FSEEK.md) | 移動檔案指標 |
| [FSIZE](../functions/FSIZE.md) | 傳回檔案大小 |
| [FSTATUS](../functions/FSTATUS.md) | 傳回檔案 I/O 操作的狀態 |
| [FTELL](../functions/FTELL.md) | 傳回檔案指標的位置 |
| [FUNCDECL_ERASE](../functions/FUNCDECL_ERASE.md) | 刪除動態函式宣告 |
| [FUNCDECL_READ](../functions/FUNCDECL_READ.md) | 讀取動態函式宣告 |
| [FUNCDECL_WRITE](../functions/FUNCDECL_WRITE.md) | 寫出動態函式宣告 |
| [FUNCTIONEX](../functions/FUNCTIONEX.md) | 呼叫外部程式庫函式 |
| [FWRITE](../functions/FWRITE.md) | 寫入檔案 |
| [FWRITE2](../functions/FWRITE2.md) | 寫入檔案（附換行） |
| [FWRITEBIN](../functions/FWRITEBIN.md) | 將資料以二進位格式寫入檔案 |
| [FWRITEDECODE](../functions/FWRITEDECODE.md) | 轉換解碼格式後寫入 |
| [FWRITEJSON](../functions/FWRITEJSON.md) | 將值轉換為 JSON 並寫入檔案（Tc602-1 以後） |
| [FWRITETOML](../functions/FWRITETOML.md) | 將雜湊轉換為 TOML 並寫入檔案（Tc602-5 以後） |
| [FWRITEXML](../functions/FWRITEXML.md) | 將元素的雜湊轉換為 XML 並寫入檔案（Tc602-1 以後） |
| [FWRITEYAML](../functions/FWRITEYAML.md) | 將值轉換為 YAML 並寫入檔案（Tc602-5 以後） |

## G-I

| 函式 | 說明 |
|------|------|
| [GETCALLSTACK](../functions/GETCALLSTACK.md) | 取得呼叫堆疊 |
| [GETDELIM](../functions/GETDELIM.md) | 取得目前的分隔符號 |
| [GETENV](../functions/GETENV.md) | 取得環境變數 |
| [GETERRORLOG](../functions/GETERRORLOG.md) | 取得錯誤記錄 |
| [GETFUNCINFO](../functions/GETFUNCINFO.md) | 取得函式資訊 |
| [GETFUNCLIST](../functions/GETFUNCLIST.md) | 取得使用者自訂函式清單 |
| [GETLASTERROR](../functions/GETLASTERROR.md) | 取得最後的錯誤碼 |
| [GETMEMINFO](../functions/GETMEMINFO.md) | 取得記憶體資訊 |
| [GETSECCOUNT](../functions/GETSECCOUNT.md) | 取得秒數計數 |
| [GETSETTING](../functions/GETSETTING.md) | 取得設定值 |
| [GETSTRBYTES](../functions/GETSTRBYTES.md) | 傳回字串的位元組數 |
| [GETSYSTEMFUNCLIST](../functions/GETSYSTEMFUNCLIST.md) | 取得系統函式清單 |
| [GETTICKCOUNT](../functions/GETTICKCOUNT.md) | 取得計時器計數 |
| [GETTIME](../functions/GETTIME.md) | 取得目前時間 |
| [GETTIMEZONE](../functions/GETTIMEZONE.md) | 取得本地時區資訊 |
| [GETTYPE](../functions/GETTYPE.md) | 傳回變數的型別 |
| [GETTYPEEX](../functions/GETTYPEEX.md) | 詳細傳回變數的型別 |
| [GETVARLIST](../functions/GETVARLIST.md) | 取得全域變數清單 |
| [HAN2ZEN](../functions/HAN2ZEN.md) | 將半形字元轉換為全形字元 |
| [HASH_EXIST](../functions/HASH_EXIST.md) | 確認雜湊中是否有鍵（Tc600-3 以後） |
| [HASH_KEYS](../functions/HASH_KEYS.md) | 以陣列傳回雜湊的鍵（Tc600-3 以後） |
| [HASH_SIZE](../functions/HASH_SIZE.md) | 傳回雜湊的元素數量（Tc600-3 以後） |
| [HASH_SPLIT](../functions/HASH_SPLIT.md) | 分割字串並建立雜湊（Tc600-3 以後） |
| [HASH_VALUES](../functions/HASH_VALUES.md) | 以陣列傳回雜湊的值（Tc600-3 以後） |
| [HEXSTRTOI](../functions/HEXSTRTOI.md) | 將十六進位字串轉換為整數 |
| [IARRAY](../functions/IARRAY.md) | 通用陣列的初始值 |
| [IHASH](../functions/IHASH.md) | 建立雜湊（Tc600-3 以後） |
| [INSERT](../functions/INSERT.md) | 在字串中插入字串 |
| [ISEVALUABLE](../functions/ISEVALUABLE.md) | 確認能否以 EVAL 評估 |
| [ISFUNC](../functions/ISFUNC.md) | 確認函式是否存在 |
| [ISGLOBALDEFINE](../functions/ISGLOBALDEFINE.md) | 確認全域定義是否存在 |
| [ISINTSTR](../functions/ISINTSTR.md) | 確認是否為整數字串 |
| [ISREALSTR](../functions/ISREALSTR.md) | 確認是否為實數字串 |
| [ISVAR](../functions/ISVAR.md) | 確認變數是否存在 |

## J-P

| 函式 | 說明 |
|------|------|
| [LETTONAME](../functions/LETTONAME.md) | 動態指定變數名稱並指派 |
| [LICENSE](../functions/LICENSE.md) | 顯示授權資訊 |
| [LINT.GetFuncUsedBy](../functions/LINT.GetFuncUsedBy.md) | 取得函式的使用位置（LINT） |
| [LINT.GetGlobalVarLetted](../functions/LINT.GetGlobalVarLetted.md) | 取得全域變數的指派位置（LINT） |
| [LINT.GetGlobalVarUsedBy](../functions/LINT.GetGlobalVarUsedBy.md) | 取得全域變數的使用位置（LINT） |
| [LINT.GetLocalVarLetted](../functions/LINT.GetLocalVarLetted.md) | 取得區域變數的指派位置（LINT） |
| [LINT.GetLocalVarUsedBy](../functions/LINT.GetLocalVarUsedBy.md) | 取得區域變數的使用位置（LINT） |
| [LINT.GetUserDefFuncUsedBy](../functions/LINT.GetUserDefFuncUsedBy.md) | 取得使用者自訂函式的使用位置（LINT） |
| [LINT.GetVarRefs](../functions/LINT.GetVarRefs.md) | 逐一取得變數、函式的出現位置及區塊（LINT） |
| [LOADLIB](../functions/LOADLIB.md) | 載入外部程式庫 |
| [LOG](../functions/LOG.md) | 傳回自然對數 |
| [LOG10](../functions/LOG10.md) | 傳回常用對數 |
| [LOGGING](../functions/LOGGING.md) | 輸出至記錄 |
| [LSO](../functions/LSO.md) | 傳回最後選取的選項索引 |
| [MKDIR](../functions/MKDIR.md) | 建立目錄 |
| [OUTPUTNUM](../functions/OUTPUTNUM.md) | 設定數值的輸出格式 |
| [PARSEHEADER](../functions/PARSEHEADER.md) | 將類似 HTTP、SHIORI 標頭的內容轉換為雜湊或陣列（Tc602-3 以後） |
| [PARSEHTML](../functions/PARSEHTML.md) | 將 HTML 字串轉換為雜湊（Tc605-1 以後） |
| [PARSEJSON](../functions/PARSEJSON.md) | 將 JSON 字串轉換為雜湊或陣列（Tc601-1 以後） |
| [PARSETOML](../functions/PARSETOML.md) | 將 TOML 字串轉換為雜湊（Tc602-5 以後） |
| [PARSEXML](../functions/PARSEXML.md) | 將 XML 字串轉換為雜湊（Tc601-1 以後） |
| [PARSEYAML](../functions/PARSEYAML.md) | 將 YAML 字串轉換為雜湊或陣列（Tc602-5 以後） |
| [POW](../functions/POW.md) | 傳回次方 |
| [PROCESSGLOBALDEFINE](../functions/PROCESSGLOBALDEFINE.md) | 處理全域定義 |

## Q-S

| 函式 | 說明 |
|------|------|
| [RAND](../functions/RAND.md) | 產生亂數 |
| [READFMO](../functions/READFMO.md) | 從 FMO 讀取資料 |
| [REPLACE](../functions/REPLACE.md) | 取代字串 |
| [REQUESTLIB](../functions/REQUESTLIB.md) | 向外部程式庫傳送請求 |
| [RESTOREVAR](../functions/RESTOREVAR.md) | 還原變數 |
| [RE_ASEARCH](../functions/RE_ASEARCH.md) | 使用正規表示式搜尋陣列 |
| [RE_ASEARCHEX](../functions/RE_ASEARCHEX.md) | 使用正規表示式搜尋陣列（全部符合） |
| [RE_GETLEN](../functions/RE_GETLEN.md) | 傳回正規表示式符合項目的長度 |
| [RE_GETPOS](../functions/RE_GETPOS.md) | 傳回正規表示式符合項目的位置 |
| [RE_GETSTR](../functions/RE_GETSTR.md) | 傳回正規表示式符合的字串 |
| [RE_GREP](../functions/RE_GREP.md) | 使用正規表示式篩選 |
| [RE_MATCH](../functions/RE_MATCH.md) | 確認是否符合正規表示式 |
| [RE_OPTION](../functions/RE_OPTION.md) | 設定正規表示式選項 |
| [RE_REPLACE](../functions/RE_REPLACE.md) | 使用正規表示式取代 |
| [RE_REPLACEEX](../functions/RE_REPLACEEX.md) | 使用正規表示式取代（擴充） |
| [RE_SEARCH](../functions/RE_SEARCH.md) | 使用正規表示式搜尋 |
| [RE_SPLIT](../functions/RE_SPLIT.md) | 使用正規表示式分割 |
| [RMDIR](../functions/RMDIR.md) | 刪除目錄 |
| [ROUND](../functions/ROUND.md) | 四捨五入 |
| [SAVEVAR](../functions/SAVEVAR.md) | 儲存變數 |
| [SERIALIZEVAR](../functions/SERIALIZEVAR.md) | 將變數值轉換為存檔格式的字串（Tc607-3 以後） |
| [SETDELIM](../functions/SETDELIM.md) | 設定分隔符號 |
| [SETGLOBALDEFINE](../functions/SETGLOBALDEFINE.md) | 設定全域定義 |
| [SETLASTERROR](../functions/SETLASTERROR.md) | 設定最後的錯誤碼 |
| [SETSETTING](../functions/SETSETTING.md) | 變更設定值 |
| [SETTAMAHWND](../functions/SETTAMAHWND.md) | 設定玉的視窗控制代碼 |
| [SIN](../functions/SIN.md) | 傳回正弦值 |
| [SINH](../functions/SINH.md) | 傳回雙曲正弦值 |
| [SLEEP](../functions/SLEEP.md) | 暫停處理 |
| [SPLIT](../functions/SPLIT.md) | 分割字串並傳回陣列 |
| [SPLITPATH](../functions/SPLITPATH.md) | 分解路徑 |
| [SQLCLOSE](../functions/SQLCLOSE.md) | 關閉 SQLite 資料庫（Tc602-11 以後） |
| [SQLEXEC](../functions/SQLEXEC.md) | 執行 SQL（Tc602-11 以後） |
| [SQLOPEN](../functions/SQLOPEN.md) | 開啟 SQLite 資料庫（Tc602-11 以後） |
| [SQLQUERY](../functions/SQLQUERY.md) | 執行 SQL 並傳回結果列（Tc602-11 以後） |
| [SQRT](../functions/SQRT.md) | 傳回平方根 |
| [SRAND](../functions/SRAND.md) | 設定亂數種子 |
| [STRDECODE](../functions/STRDECODE.md) | 解碼字串 |
| [STRDIGEST](../functions/STRDIGEST.md) | 計算字串的雜湊值 |
| [STRENCODE](../functions/STRENCODE.md) | 編碼字串 |
| [STRFORM](../functions/STRFORM.md) | 產生格式化字串 |
| [STRLEN](../functions/STRLEN.md) | 傳回字串長度 |
| [STRSTR](../functions/STRSTR.md) | 搜尋字串 |
| [SUBSTR](../functions/SUBSTR.md) | 取得子字串 |

## T-Z

| 函式 | 說明 |
|------|------|
| [TAN](../functions/TAN.md) | 傳回正切值 |
| [TANH](../functions/TANH.md) | 傳回雙曲正切值 |
| [THREADCLOSE](../functions/THREADCLOSE.md) | 捨棄執行緒的記錄（Tc608-1 以後） |
| [THREADJOIN](../functions/THREADJOIN.md) | 等待執行緒結束（Tc608-1 以後） |
| [THREADRESULT](../functions/THREADRESULT.md) | 傳回已結束執行緒中函式的傳回值（Tc608-1 以後） |
| [THREADSTART](../functions/THREADSTART.md) | 在不同的執行緒中執行函式（Tc608-1 以後） |
| [THREADSTATE](../functions/THREADSTATE.md) | 傳回執行緒的狀態（Tc608-1 以後） |
| [THREADSTOP](../functions/THREADSTOP.md) | 要求執行緒中斷（Tc608-1 以後） |
| [TOAUTO](../functions/TOAUTO.md) | 自動將值轉換為適當的型別 |
| [TOAUTOEX](../functions/TOAUTOEX.md) | TOAUTO 的擴充版 |
| [TOBINSTR](../functions/TOBINSTR.md) | 將整數轉換為二進位字串 |
| [TOHEXSTR](../functions/TOHEXSTR.md) | 將整數轉換為十六進位字串 |
| [TOINT](../functions/TOINT.md) | 將值轉換為整數 |
| [TOLOWER](../functions/TOLOWER.md) | 將字串轉換為小寫 |
| [TOREAL](../functions/TOREAL.md) | 將值轉換為實數 |
| [TOSTR](../functions/TOSTR.md) | 將值轉換為字串 |
| [TOUPPER](../functions/TOUPPER.md) | 將字串轉換為大寫 |
| [TRANSLATE](../functions/TRANSLATE.md) | 轉換字串 |
| [UNDEFFUNC](../functions/UNDEFFUNC.md) | 刪除函式定義 |
| [UNDEFGLOBALDEFINE](../functions/UNDEFGLOBALDEFINE.md) | 刪除全域定義 |
| [UNLOADLIB](../functions/UNLOADLIB.md) | 卸載外部程式庫 |
| [ZEN2HAN](../functions/ZEN2HAN.md) | 將全形字元轉換為半形字元 |
