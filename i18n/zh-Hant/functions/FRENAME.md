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

變更檔案名稱。可以指定完整路徑。若指定相對路徑，則以 DLL load 傳入的位置（通常是 DLL 所在位置）為基準。

## Compatibility

- YAYA：從初次發行起即可使用
- AYA：5.8 版以後

## See Also

- FCOPY
- FMOVE
- FDEL
