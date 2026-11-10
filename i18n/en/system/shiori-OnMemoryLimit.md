# shiori.OnMemoryLimit

## Overview

A user-defined function called when the memory limit is reached.

## Signature

```
shiori.OnMemoryLimit()
```

## Parameters

None

## Returns

The return value is ignored by the system.

## Notes

- Implementing this function is optional. You do not need to define it in a dictionary if no error handling is needed.
- You can use the `GETCALLSTACK` function to identify the location of the problem.
- This function is called when memory runs out during execution. However, it cannot catch a stack overflow.

## Compatibility

- YAYA: Tc567-2 and later

## See Also

- [shiori.OnMemoryError](./shiori-OnMemoryError.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
