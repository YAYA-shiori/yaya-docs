# SLEEP
**Category:** デバッグ

## Signature
```
SLEEP(millisecond)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| millisecond | 等待時間（毫秒） |

## Returns
- 成功時：0
- 失敗時：-1

## Description
暫停處理指定的毫秒數。

指定較長的等待時間會導致整個應用程式凍結，因此建議僅用於短時間等待或偵錯用途。

從透過 [THREADSTART](THREADSTART.md) 啟動的執行緒呼叫時，等待期間其他執行緒（包括來自 SSP 的 `request`）仍可執行。若透過 [THREADSTOP](THREADSTOP.md) 或 `unload` 要求中斷，函式會在等待途中返回。

## Compatibility
- YAYA：Tc564-1 以後
- Tc608-1：從工作執行緒呼叫時，等待期間其他執行緒仍可執行，且收到中斷要求時會在等待途中返回

## See Also
- THREADSTART
