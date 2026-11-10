# THREADRESULT
**Category:** スレッド

## Signature
```
THREADRESULT( id )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| id | The thread ID returned by [THREADSTART](THREADSTART.md) |

## Returns
The return value of the thread's function.

Returns an empty value (VOID) in the following cases:

- The thread is still running
- The thread was interrupted or ended with an error ([THREADSTATE](THREADSTATE.md) is 2 or 3)
- No thread with that ID

If an argument is missing or is not an integer, emits warning W0008 / W0009 and returns an empty value.

## Description
Gets the value returned by a thread's function when it finishes successfully. If the function has multiple possible outputs (selected at random), this is the one selected when it finishes.

You can also write to a global variable instead of receiving the return value. See [THREADSTART](THREADSTART.md).

## Example
```
_id = THREADSTART('Work.Add', 3, 4)
_r = THREADJOIN(_id)
THREADRESULT(_id)   // 7
```

## Compatibility
- Tc608-1 and later

## See Also
- THREADSTART
- THREADJOIN
- THREADSTATE
