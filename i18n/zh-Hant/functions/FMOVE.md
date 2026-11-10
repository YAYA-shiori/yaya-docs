# FMOVE

**Category:** ファイル操作

## Signature

```
FMOVE( path , dir )
```

## Parameters

| 引數 | 說明 |
|-----------|-------------|
| path | 來源檔案名稱。可指定完整路徑。相對路徑以 DLL 載入位置為基準 |
| dir | 目的地目錄名稱 |

## Returns

- 成功時：1
- 失敗時：0

## Description

移動檔案。路徑可指定完整路徑。若為相對路徑，則以 DLL 載入時傳入的位置（通常是 DLL 所在位置）為基準。

## Compatibility

- YAYA: 自首次釋出起即可使用
- AYA: 5.8 版以後

## See Also

- FCOPY
- FRENAME
- FDEL
