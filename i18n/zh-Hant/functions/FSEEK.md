# FSEEK

**Category:** ファイル操作

## Signature

```
FSEEK(path, offset, origin)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 以 FOPEN 指定的檔名 |
| offset | 移動的位元組數 |
| origin | 指定移動起點的字串。`SEEK_CUR` 或 `current`（目前位置）、`SEEK_END` 或 `end`（檔案結尾）、`SEEK_SET` 或 `start`（檔案開頭） |

## Returns

- 成功時：1
- 失敗時：0

在非二進位模式下，換行字元的自動轉換可能會導致 FSEEK/FTELL 無法如預期運作。若要使用這些函式，建議在 FOPEN 中指定二進位模式。

## Description

移動檔案讀寫時的位置（檔案位置指示器）。

## See Also

- FTELL
- FOPEN
