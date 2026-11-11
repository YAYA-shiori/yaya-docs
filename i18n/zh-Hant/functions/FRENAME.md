# FRENAME

**Category:** ファイル操作

## Signature

```
FRENAME( from , to )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| from | 變更前的檔名。可指定完整路徑。相對路徑以 DLL 的載入位置為基準 |
| to | 變更後的檔名 |

## Returns

- 成功時：1
- 失敗時：0

## Description

變更檔案名稱。路徑可指定為完整路徑。若為相對路徑，則以 DLL load 傳入的位置（通常是 DLL 所在位置）為基準。

以 `FOPEN` 開啟中的檔案無法變更名稱，並會傳回 0。重新命名之前，請先使用 `FCLOSE` 關閉檔案。

## Compatibility

- YAYA：自首次發布起可使用
- AYA：5.8 版以後

## See Also

- FCOPY
- FMOVE
- FDEL
