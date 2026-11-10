# FSTATUS

**Category:** ファイル操作

## Signature

```
FSTATUS(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 以 FOPEN 指定的檔名 |

## Returns

傳回前一次檔案 I/O 操作（例如 FOPEN、FREAD、FWRITE、FSEEK、FTELL）的結果狀態。

| 傳回值 | 意義 |
|--------|------|
| 0 | 正常結束（沒有錯誤） |
| -1 | 發生錯誤 |
| 1 | 已到達檔案結尾（EOF） |

## Description

取得檔案讀寫函式（FOPEN、FREAD 系列、FWRITE 系列、FSEEK、FTELL）前一次操作的狀態。

## Compatibility

- YAYA：Tc573-3 以後

## See Also

- FOPEN
- FSEEK
- FTELL
