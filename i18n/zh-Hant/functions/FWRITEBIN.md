# FWRITEBIN
**Category:** ファイル操作

## Signature
```
FWRITEBIN( path, string [, char] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 以 FOPEN 指定的檔名 |
| string | 要寫入的字串 |
| char | 取代位元組值 0x00 的字元（省略時為半形空格） |

## Returns
無

## Description
不進行字元編碼轉換而寫入資料的函式。必須事先以 FOPEN 開啟檔案。

若未以二進位模式開啟，會進行換行碼轉換。

由於 YAYA 的字串無法包含 null 位元組，`char` 指定的字元會轉換為位元組值 0。

## Compatibility
- YAYA：Tc516-901 以後

## See Also
- FWRITE
- FREADBIN
- FOPEN
