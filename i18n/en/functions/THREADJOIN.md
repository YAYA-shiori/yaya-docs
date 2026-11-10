# THREADJOIN
**Category:** スレッド

## Signature
```
THREADJOIN( id [, timeout ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | The thread ID returned by [THREADSTART](THREADSTART.md) |
| timeout | Maximum wait time in milliseconds. If omitted, waits until the thread finishes |

## Returns
| Value | Meaning |
|----|------|
| 1 | The thread has finished (including if it had already finished) |
| 0 | Timed out and the thread is still running |
| -1 | No thread with that ID |
| -2 | Cannot wait for itself |

If an argument is missing or is not an integer, emits warning W0008 / W0009 and returns -1.

## Description
Waits until the thread finishes. Other threads can run while this thread is waiting. If the waiting thread is asked to stop, it also stops waiting and returns.

Get the return value after the thread finishes with [THREADRESULT](THREADRESULT.md).

!!! warning "Do not wait for a long time inside a host request"
    Waiting for a long time with `THREADJOIN` inside an SSP `request` stops SSP from responding during that time. This not only stops SSP window processing; communication sent by that thread (such as a call to [DIRECTSSTP](DIRECTSSTP.md) made by a worker) will time out because SSP cannot respond. Use a short `timeout` or check the status with [THREADSTATE](THREADSTATE.md).

## Example
```
_id = THREADSTART('Work.Add', 3, 4)
_r = THREADJOIN(_id, 1000)
if _r == 1 {
	THREADRESULT(_id)   // 7
}
```

## Compatibility
- Tc608-1 and later

## See Also
- THREADSTART
- THREADSTATE
- THREADRESULT
- THREADSTOP
