# THREADCLOSE
**Category:** スレッド

## Signature
```
THREADCLOSE( id )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | The thread ID returned by [THREADSTART](THREADSTART.md) |

## Returns
| Value | Meaning |
|----|------|
| 0 | Discarded the record for a finished thread |
| 1 | The thread is still running, so requested that it be interrupted. The record will be discarded when it finishes |
| -1 | No thread with that ID |

If an argument is missing or is not an integer, emits warning W0008 / W0009 and returns -1.

## Description
Discards the thread's record (state and return value). For a running thread, requests an interruption just like [THREADSTOP](THREADSTOP.md), then discards the record when the thread finishes. After the record is discarded, passing that ID to [THREADSTATE](THREADSTATE.md) or similar functions returns -1.

Even if you do not discard them, records for finished threads are removed from oldest to newest when their number exceeds 256. Discard threads whose results you have finished using to ensure their records do not remain.

## Example
```
_id = THREADSTART('Work.Add', 3, 4)
_r = THREADJOIN(_id)
_v = THREADRESULT(_id)
_r = THREADCLOSE(_id)
```

## Compatibility
- Tc608-1 and later

## See Also
- THREADSTART
- THREADSTOP
- THREADSTATE
