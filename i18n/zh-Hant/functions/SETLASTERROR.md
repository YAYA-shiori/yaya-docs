# SETLASTERROR
**Category:** デバッグ

## Signature
```
SETLASTERROR( code )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| code | 要設定的錯誤碼（整數值） |

## Returns
無

## Description
設定系統函式的錯誤碼。可在執行 YAYA 指令碼時手動設定錯誤狀態。

可搭配 GETLASTERROR 管理系統層級的錯誤狀態。

## Compatibility
- YAYA：從初始版本起支援
- AYA：5.8 以後

## See Also
- GETLASTERROR
