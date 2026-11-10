# GETTICKCOUNT
**Category:** システム情報

## Signature
```
GETTICKCOUNT( [ flag ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| flag | Currently has no practical effect. Historically, specifying a nonzero value returned the 32nd bit value of `GetTickCount() >> 31` and was used for measuring long durations |

## Returns
Elapsed time since the OS was started, in milliseconds

## Description
Returns the elapsed time since the OS was started, in milliseconds.

On Windows XP and earlier, the value resets to 0 after approximately 24 days and 20 hours. This limitation does not apply to Vista and later or to other OSes.

## Compatibility
- YAYA: Available since the initial version
- AYA 5.8: Available

## See Also
- GETTIME
- GETSYSTEMFUNCLIST
