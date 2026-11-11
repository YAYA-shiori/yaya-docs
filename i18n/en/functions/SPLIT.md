# SPLIT
**Category:** 文字列操作

## Signature
```
SPLIT(src, delim [, max])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | String to split (it is recommended to convert numeric variables with TOSTR before passing them) |
| delim | Delimiter string |
| max | Maximum number of splits (if omitted or set to 0, splits the entire string) |

## Returns
- On success: A generic array containing the split string elements
- On failure: An empty array

## Description
Splits a string and returns the result as a generic array. It is faster than RE_SPLIT because it does not perform regular expression processing.

If `max` is specified, splitting stops at that number, and the remaining part is combined into the last element. If `max` is set to 1, no splitting is performed; the result is simply a string assignment.

## Example
```
_array = SPLIT("A//B//C//D//E", "//", 3)
// 結果: ("A", "B", "C//D//E")
```

## Compatibility
- YAYA: Available since the initial version
- AYA: 5.8 and later

## See Also
- RE_SPLIT (splits using regular expressions)
