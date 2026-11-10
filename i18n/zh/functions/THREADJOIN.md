# THREADJOIN
**Category:** スレッド

## Signature
```
THREADJOIN( id [, timeout ] )
```

## Parameters
| 参数 | 说明 |
|-----------|-------------|
| id | [THREADSTART](THREADSTART.md) 返回的线程 ID |
| timeout | 等待时间上限（毫秒）。省略时会一直等待，直到线程结束 |

## Returns
| 值 | 含义 |
|----|------|
| 1 | 线程已结束（包括调用时线程已经结束的情况） |
| 0 | 超时，线程仍未结束 |
| -1 | 不存在该 ID 对应的线程 |
| -2 | 不能等待自身 |

参数不足或不是整数时，会发出警告 W0008 / W0009 并返回 -1。

## Description
等待线程结束。等待期间，其他线程可以运行。即使等待方线程收到中断请求，也会停止等待并返回。

线程结束后的返回值可通过 [THREADRESULT](THREADRESULT.md) 获取。

!!! warning "不要在主机的 request 中长时间等待"
    在 SSP 发出的 `request` 中长时间等待 `THREADJOIN`，会导致 SSP 在此期间停止响应。这不仅会使 SSP 窗口的处理停止，尝试从该线程发送的通信（例如工作线程调用的 [DIRECTSSTP](DIRECTSSTP.md)）也会因 SSP 无法响应而超时。请使用较短的 `timeout`，或通过 [THREADSTATE](THREADSTATE.md) 检查线程状态。

## Example
```
_id = THREADSTART('Work.Add', 3, 4)
_r = THREADJOIN(_id, 1000)
if _r == 1 {
	THREADRESULT(_id)   // 7
}
```

## Compatibility
- Tc608-1 及以上

## See Also
- THREADSTART
- THREADSTATE
- THREADRESULT
- THREADSTOP
