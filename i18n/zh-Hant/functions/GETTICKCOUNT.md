# GETTICKCOUNT
**Category:** システム情報

## Signature
```
GETTICKCOUNT( [ flag ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| flag | 目前實際上沒有作用。過去指定非 0 值時會傳回 `GetTickCount() >> 31` 的第 32 位元值，曾用於長時間測量 |

## Returns
OS 啟動後經過的時間（毫秒）

## Description
以毫秒為單位傳回 OS 啟動後經過的時間。

在 Windows XP 以前的版本中，約 24 日 20 小時後會重設為 0。Vista 以後的版本和其他 OS 沒有此限制。

## Compatibility
- YAYA：從初期版本開始即可使用
- AYA 5.8：可以使用

## See Also
- GETTIME
- GETSYSTEMFUNCLIST
