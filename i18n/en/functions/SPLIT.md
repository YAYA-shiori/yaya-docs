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
| max | Maximum number of splits (if omitted or 0, split completely) |

## Returns
- On success: a generic array containing the split string elements
- On failure: an empty array

## Description
Splits a string and returns it as a generic array. Because it does not perform regular expression processing, it is faster than RE_SPLIT.

If `max` is specified, splitting stops at that number, and the remaining portion is combined into the last element.

## Example
```
_array = SPLIT("A//B//C//D//E", "//", 3)
// 結果: ("A", "B", "C//D//E")
```

## Compatibility
- YAYA: Available since the initial version
- AYA: 5.8 and later

## See Also
- RE_SPLIT (splitting using regular expressions)
