# FWRITE2
**Category:** ファイル操作

## Signature
```
FWRITE2( path, string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 以 FOPEN 開啟的檔案路徑（相對於 yaya.dll 的路徑） |
| string | 要寫入的字串 |

## Returns
無（VOID）

## Description
將一行寫入檔案的函式。必須事先以 FOPEN 開啟檔案。

寫入時會將字元編碼從 YAYA 內部格式轉換為 FCHARSET 指定的格式。與 FWRITE 不同，**行尾不會附加換行字元**。

若要自動附加換行字元，請使用 FWRITE。

## Compatibility
- YAYA：從初期版本起即可使用
- AYA：5.8 以後

## See Also
- FWRITE
- FREAD
- FWRITEBIN
- FOPEN
