# ROUND
**Category:** 数学関数

## Signature
```
ROUND( val )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| val | Real number to round |

## Returns
- On success: Rounded real number
- On failure: 0.0

## Description
Rounds the fractional part of a real number.

Note the behavior at negative halfway values:
- `ROUND(-1.5)` → `-1.0` (not -2.0)
- `ROUND(-1.55)` → `-2.0`

## Example
| Input | Output | Notes |
|------|------|------|
| 1.55 | 2.0 | 1.5 or greater |
| 1.45 | 1.0 | Less than 1.5 |
| 1.5  | 2.0 | Exactly 0.5 |
| -1.5 | -1.0 | Negative halfway value |
| -1.55 | -2.0 | Negative value |

## Compatibility
- YAYA: Supported since the initial version
- AYA: 5.8 and later

## See Also
- CEIL
- FLOOR
