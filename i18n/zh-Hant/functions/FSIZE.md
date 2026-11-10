# FSIZE

**Category:** ファイル操作

## Signature

```
FSIZE(path)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| path | 要取得大小的檔案路徑。可指定完整路徑。相對路徑以 DLL 的載入位置為基準 |

## Returns

- 成功時：表示檔案大小的非負整數（位元組數）
- 失敗時：-1

## Description

取得檔案大小。可以指定完整路徑。若指定相對路徑，則以 DLL load 傳入的位置（通常是 DLL 所在位置）為基準。

## Compatibility

- YAYA：從初次發行起即可使用
- AYA：5.8 版以後

## See Also

- FATTRIB
- FSEEK
- FTELL
