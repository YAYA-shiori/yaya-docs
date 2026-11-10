# shiori.OnMemoryError

## Overview

A user-defined function called when a memory error occurs.

## Signature

```
shiori.OnMemoryError()
```

## Parameters

None

## Returns

The return value is ignored by the system.

## Notes

- Implementing this function is optional. If it is not defined, the system only generates an error log.
- You can use the `GETCALLSTACK` function to identify the location of the problem.

## Compatibility

- YAYA: Tc567-2 and later

## See Also

- [shiori.OnMemoryLimit](./shiori-OnMemoryLimit.md)
- [GETCALLSTACK](../functions/GETCALLSTACK.md)
