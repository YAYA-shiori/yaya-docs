# REPLACE
**Category:** 文字列操作

## Signature
```
REPLACE( src , before , after [ , count ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | The string to transform |
| before | The substring to search for |
| after | The replacement substring |
| count | (Optional) Number of replacements. If less than 0 or omitted, replaces all matching occurrences |

## Returns
- Success: The string after replacement
- Failure: The original src string (unchanged)

## Description
Replaces parts of a string. All occurrences of the specified string are replaced. You can limit the number of replacements by specifying `count`.

## Example
```
_tehai = '4m4m5m5m6m6m2p3p3p4p1s1s1s'
_tsumo = '4p'
_dahai = '1s'
_tehai = REPLACE(_tehai, _dahai, _tsumo, 1)
_tehai // '4m4m5m5m6m6m2p3p3p4p4p1s1s'
```

## Compatibility
- YAYA: Available since the initial release (the count parameter was added in Tc548-1)
- AYA: Available since version 5.8
