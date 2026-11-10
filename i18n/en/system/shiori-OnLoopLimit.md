# shiori.OnLoopLimit

## Overview

A user-defined function called when the number of loop iterations reaches the limit.

## Signature

```
shiori.OnLoopLimit(_filename_, _linenum_)
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
- The loop limit can be changed using [`looplimit`](../grammar/01-basic-settings.md#looplimit-count) in the basic settings (default: 1000000). `foreach` is not subject to this limit.
- This function is called only when a loop is stopped after reaching the limit. It is not called for a `for` / `while` loop that ends naturally after exactly the limit number of iterations.

## Compatibility

- YAYA: Tc564-2 and later
- The default loop limit was changed from 10000 to 1000000 in Tc574-10 / Tc606-4.
- Before Tc574-10 / Tc606-4, this function could also be called for a `for` / `while` loop that ended naturally (or used `break` / `return`) after reaching a number of iterations between just below the limit and the limit itself.

## See Also

- [shiori.OnCallLimit](./shiori-OnCallLimit.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
