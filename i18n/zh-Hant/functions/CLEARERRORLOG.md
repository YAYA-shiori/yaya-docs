# CLEARERRORLOG

**Category:** デバッグ

## Signature

```
CLEARERRORLOG()
```

## Parameters

無

## Returns

空陣列

清除 YAYA 內部處理時累積的錯誤與警告記錄。執行後，GETERRORLOG 傳回的錯誤陣列會變成空陣列。

## Description

清除 YAYA 內部發生的錯誤與警告記錄。執行後，透過 GETERRORLOG 取得的錯誤陣列會變成空陣列。

## Compatibility

- YAYA: Tc567-2 版以後

## See Also

- GETERRORLOG
