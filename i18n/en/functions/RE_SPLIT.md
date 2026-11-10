# RE_SPLIT
**Category:** 正規表現

## Signature
```
RE_SPLIT( string , regexp [, max] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String to split |
| regexp | Regular expression pattern used to split the string |
| max | Maximum number of splits (omitted or 0 means split all) |

## Returns
- Success: A generic array containing the split strings
- Failure: An empty generic array

## Description
Splits the target string using a regular expression pattern and returns the result as a generic array.

If `max` is specified, splitting stops after that number of splits, and the remainder is combined into the last element (`RE_SPLIT('a,b,c,d', ',', 2)` returns `a` and `b,c,d`).

You can get details about the split results using RE_GETSTR, RE_GETPOS, and RE_GETLEN.

## Compatibility
- YAYA: Supported since the initial version (the max parameter is available from Tc536-1 onward)
- Tc606-6: Changed the regular expression engine to uka_regexp (syntax similar to PCRE2). Subroutine calls in patterns can be resolved using variables and functions ([Regular expressions](../grammar/14-regular-expressions.md))

## See Also
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [Regular expressions](../grammar/14-regular-expressions.md)
