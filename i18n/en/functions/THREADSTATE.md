# THREADSTATE
**Category:** スレッド

## Signature
```
THREADSTATE( id )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | Thread ID returned by [THREADSTART](THREADSTART.md) |

## Returns
An integer representing the thread's state.

| Value | Meaning |
|----|------|
| -1 | No thread with that ID (it was discarded with [THREADCLOSE](THREADCLOSE.md), or its old record was removed) |
| 0 | Running (including waiting for its turn to execute) |
| 1 | Finished executing the function |
| 2 | Interrupted ([THREADSTOP](THREADSTOP.md), [THREADCLOSE](THREADCLOSE.md), or unload) |
| 3 | Finished with an error (including a forcibly terminated thread) |

If an argument is missing or is not an integer, warning W0008 / W0009 is issued and -1 is returned.

## Description
Checks whether a thread is running or has finished. It returns immediately without waiting, so it is useful for checking repeatedly from `OnSecondChange` or similar events. To wait until a thread finishes, use [THREADJOIN](THREADJOIN.md).

!!! note "To avoid blocking SSP responses"
    If [THREADJOIN](THREADJOIN.md) waits for a long time inside the host's `request`, SSP responses will be blocked. In processing that responds to SSP, check with `THREADSTATE` and defer further work until the next opportunity if the thread has not finished.

## Example
```
OnSecondChange
{
	if THREADSTATE(work.id) == 1 {
		'終わりました: ' + TOSTR(THREADRESULT(work.id))
	}
}
```

## Compatibility
- Tc608-1 and later

## See Also
- THREADSTART
- THREADJOIN
- THREADRESULT
