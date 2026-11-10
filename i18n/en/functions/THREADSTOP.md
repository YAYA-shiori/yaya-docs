# THREADSTOP
**Category:** スレッド

## Signature
```
THREADSTOP( id )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | Thread ID returned by [THREADSTART](THREADSTART.md) |

## Returns
| Value | Meaning |
|----|------|
| 1 | Requested interruption |
| 0 | The thread has already finished |
| -1 | No thread with that ID |

If an argument is missing or is not an integer, warning W0008 / W0009 is issued and -1 is returned.

## Description
Requests that a thread be interrupted. Returns immediately without waiting for it to finish. To check whether it has finished, use [THREADSTATE](THREADSTATE.md) or [THREADJOIN](THREADJOIN.md).

At the next statement boundary (including the end of a `while` / `for` iteration), the thread exits the current function in the same way as `return`; the caller function exits in the same way, and the thread finishes. A thread waiting in [SLEEP](SLEEP.md) or [THREADJOIN](THREADJOIN.md) stops waiting and returns. The interrupted thread's state becomes 2, and [THREADRESULT](THREADRESULT.md) returns an empty value.

The thread does not stop in the middle of a single system function call (such as a large regular expression or `REQUESTLIB`); it stops after the call finishes.

## Example
```
OnClose
{
	_r = THREADSTOP(work.id)
	_r = THREADJOIN(work.id, 2000)   // 2 秒まで終わりを待つ
}
```

## Compatibility
- Tc608-1 and later

## See Also
- THREADSTART
- THREADSTATE
- THREADJOIN
- THREADCLOSE
