# SRAND
**Category:** 数学関数

## Signature
```
SRAND( [seed] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| seed | Random number seed (accepts an integer, real number, or string). If omitted, initializes the seed randomly using the current time |

## Returns
- On success: 1
- On failure: 0

## Description
Sets the seed for integer random numbers. If the argument is omitted, initializes the seed based on the current time.

The system dictionary may use the RAND function, so take care to consider the scope of any effects when using SRAND.

## Compatibility
- YAYA: Tc551-1 or later

## See Also
- RAND (random number generation)
