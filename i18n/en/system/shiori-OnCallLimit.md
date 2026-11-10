# shiori.OnCallLimit

## Overview

A user-defined function called when the call depth limit is reached.

## Signature

```
shiori.OnCallLimit(_filename_, _linenum_)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| *filename* | The name of the dictionary file where the error occurred |
| *linenum* | The line number where the error occurred |

## Returns

The return value is ignored by the system.

## Notes

- Implementing this function is optional. You do not need to define it in a dictionary if no error handling is needed.
- You can use the `GETCALLSTACK` function to identify the location of the problem.
- The call depth limit can be changed using [`fncdepth`](../grammar/01-basic-settings.md#fncdepth-depth) in the basic settings (default: 32 levels).
- This function is also called when the remaining stack space is low, even if the call depth limit has not been reached (Tc607-4 and later). If the stack runs even lower while this function is running, the call is stopped without calling this function again, and only an error log (E0097) is generated.

## Compatibility

- YAYA: Tc564-2 and later
- Tc607-4: Changed to also call this function when the remaining stack space is low (before this, setting `fncdepth` to 0 caused the baseware itself to crash)

## See Also

- [shiori.OnLoopLimit](./shiori-OnLoopLimit.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
