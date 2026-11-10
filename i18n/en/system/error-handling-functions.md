# Error Handling Functions

## Overview

Error handling functions are user-defined functions that are called automatically when an error occurs while a script is running.

Implementing these functions is optional. The script works normally even if they are not defined in the dictionary, but they can be useful for debugging and analyzing errors in the user’s environment.

## Common Characteristics

All error handling functions have the following characteristics:

- **Optional to implement** — You do not need to define them in the dictionary if error handling is unnecessary
- **Return value ignored** — The system ignores the return value
- Use the **`GETCALLSTACK`** function to identify the location of a problem

## List of Error Handling Functions

| Function | Description |
|------|------|
| [shiori.OnCallLimit](./shiori-OnCallLimit.md) | When the call depth reaches its limit |
| [shiori.OnLoopLimit](./shiori-OnLoopLimit.md) | When the number of loop iterations reaches its limit |
| [shiori.OnMemoryError](./shiori-OnMemoryError.md) | When a memory error occurs |
| [shiori.OnMemoryLimit](./shiori-OnMemoryLimit.md) | When the memory limit is reached |

## Related

- [GETCALLSTACK](../functions/GETCALLSTACK.md)
