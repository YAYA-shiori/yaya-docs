# RMDIR
**Category:** ファイル操作

## Signature
```
RMDIR( path )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| path | 要刪除的目錄路徑（絕對路徑或相對路徑。相對路徑以 DLL 載入位置為基準） |

## Returns
- **1**: 刪除成功
- **0**: 失敗

## Description
刪除目錄。只能刪除空目錄。若嘗試刪除包含檔案的目錄，會發生錯誤。

## Compatibility
- YAYA: 自初始版本起支援
- AYA: 5.8 以後

## See Also
- MKDIR
