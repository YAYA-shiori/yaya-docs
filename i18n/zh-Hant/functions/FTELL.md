# FTELL

**Category:** ファイル操作

## Signature

```
FTELL(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 以 FOPEN 指定的檔名 |

## Returns

- 成功時：從檔案開頭算起的位元組偏移量（目前的檔案位置）
- 失敗時：-1

在非二進位模式下，換行字元的自動轉換可能會導致 FSEEK/FTELL 無法如預期運作。若要使用這些函式，建議在 FOPEN 中指定二進位模式。

## Description

取得檔案讀寫時的位置（檔案位置指示器）。

## See Also

- FSEEK
- FOPEN
