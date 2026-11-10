# 字元編碼相關

## 內部字元編碼

YAYA 使用 **UCS-2** 作為內部字元編碼。進行辭典操作、檔案 I/O、與外部程式庫互動時，所有字串都會自動轉換為 UCS-2 或從 UCS-2 轉換。

## 字元編碼 ID 系統

部分函式會以數值 ID 參照字元編碼。可用名稱指定的函式，請使用文字表示名稱（[字元編碼名稱](#文字コードの名前)）：

| 編碼 | 文字表示 | ID |
|----------------|------------|-----|
| Shift JIS | Shift_JIS | 0 |
| UTF-8 | UTF-8 | 1 |
| EUC-JP | EUC-JP | 2 |
| Big5 | Big5 | 3 |
| GB2312 | GB2312 | 4 |
| EUC-KR | EUC-KR | 5 |
| ISO-2022-JP (JIS) | ISO-2022-JP | 6 |
| 二進位 | binary | 126 |
| OS 預設 | default（OSNative 也相同） | 127 |

## 字元編碼名稱

以名稱指定字元編碼時，請使用上表中的文字表示。大小寫不區分。

將無法使用的名稱（例如 `UTF-16`、`ISO-8859-1`）傳給系統函式時，會發出警告 W0012 並失敗（GETLASTERROR 為 12）。失敗時的行為請參閱各函式的頁面。在 Tc574-8 / Tc603-1 之前，會將其視為 OS 預設，且不會發出警告。

在設定檔（例如 `charset`）中寫入無法使用的名稱時，和以往相同，不會發出警告，而會使用 OS 預設。

## 二進位編碼的特殊情況

二進位格式是「將 UCS-2 字串的低位元組直接作為位元組序列的特殊字元編碼」。這是為了不經轉換地交換資料，專為 `FWRITEBIN`、`FREADBIN` 等函式設計。

**重要限制：**即使在二進位模式下，YAYA 也無法處理字串中的空值位元組（0x00）。此外，`FUNCTIONEX` 等現有系統辭典也不預期會收到二進位字串值。

## 相關

- [CHARSETLIB](../functions/CHARSETLIB.md)
- [CHARSETLIBEX](../functions/CHARSETLIBEX.md)
- [CHARSETIDTOTEXT](../functions/CHARSETIDTOTEXT.md)
- [CHARSETTEXTTOID](../functions/CHARSETTEXTTOID.md)
- [FCHARSET](../functions/FCHARSET.md)
- [STRENCODE](../functions/STRENCODE.md)
- [STRDECODE](../functions/STRDECODE.md)
