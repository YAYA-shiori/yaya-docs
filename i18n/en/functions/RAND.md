# RAND
**Category:** 数学関数

## Signature
```
RAND([max])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| max | (Optional) Upper limit for the random number. Generates a value in the range 0 to (max-1). If omitted, the default is 100 (generates a value from 0 to 99) |

## Returns
- Success: A random integer within the specified range
- Failure: 0

## Description
Generates a random integer. Works independently without initializing the seed. You can also set the seed with SRAND, but this is not required for basic use.

## Compatibility
- YAYA: Available since the initial release
- AYA: Available since version 5.8

## See Also
- SRAND
