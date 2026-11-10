# THREADJOIN
**Category:** スレッド

## Signature
```
THREADJOIN( id [, timeout ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | [THREADSTART](THREADSTART.md) 傳回的執行緒 ID |
| timeout | 等待時間上限（毫秒）。省略時會一直等待，直到執行緒結束 |

## Returns
| 值 | 意義 |
|----|------|
| 1 | 執行緒已結束（包含原本就已結束的情況） |
| 0 | 已逾時，執行緒仍未結束 |
| -1 | 沒有該 ID 的執行緒 |
| -2 | 無法等待自身 |

引數不足或不是整數時，會發出警告 W0008 / W0009 並傳回 -1。

## Description
等待執行緒結束。等待期間，其他執行緒仍可執行。若等待中的執行緒收到中斷要求，也會停止等待並返回。

執行緒結束後，可透過 [THREADRESULT](THREADRESULT.md) 取得其傳回值。

!!! warning "請勿在主機的 request 中長時間等待"
    在 SSP 傳來的 `request` 中長時間等待 `THREADJOIN`，會使 SSP 在此期間停止回應。這不只會使 SSP 視窗的處理停止，該執行緒嘗試送出的通訊（例如工作執行緒呼叫的 [DIRECTSSTP](DIRECTSSTP.md)）也會因 SSP 無法回應而逾時。請使用較短的 `timeout`，或改用 [THREADSTATE](THREADSTATE.md) 檢查狀態。

## Example
```
_id = THREADSTART('Work.Add', 3, 4)
_r = THREADJOIN(_id, 1000)
if _r == 1 {
	THREADRESULT(_id)   // 7
}
```

## Compatibility
- Tc608-1 以後

## See Also
- THREADSTART
- THREADSTATE
- THREADRESULT
- THREADSTOP
