# FCOPY

**Category:** ファイル操作

## Signature

```
FCOPY( path, dir )
```

## Parameters

| 引數 | 說明 |
|-----------|-------------|
| path | 來源檔案名稱。可指定完整路徑或相對路徑（以 DLL 載入位置為基準）。 |
| dir | 目的地目錄名稱 |

## Returns

- `1`: 成功
- `0`: 失敗

## Description

複製檔案。路徑可指定完整路徑。若為相對路徑，則以 DLL 載入時傳入的位置（通常是 DLL 所在位置）為基準。

## Compatibility

- YAYA: 自初版起支援
- AYA: 5.8 以後

## See Also

- FMOVE
- FRENAME
- FDEL
