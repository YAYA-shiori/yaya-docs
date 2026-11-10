# SLEEP
**Category:** デバッグ

## Signature
```
SLEEP(millisecond)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| millisecond | Wait duration (in milliseconds) |

## Returns
- On success: 0
- On failure: -1

## Description
Pauses processing for the specified number of milliseconds.

Long waits will freeze the entire application, so use this function only for short waits or debugging.

When called from a thread started with [THREADSTART](THREADSTART.md), other threads (including `request` from SSP) can run while it waits. If interruption is requested by [THREADSTOP](THREADSTOP.md) or `unload`, the function returns before the wait is complete.

## Compatibility
- YAYA: Tc564-1 and later
- Tc608-1: Updated so other threads can run during the wait when called from a worker thread, and so the function returns early if interrupted

## See Also
- THREADSTART
