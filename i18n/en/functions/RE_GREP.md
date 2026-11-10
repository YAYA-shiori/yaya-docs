# RE_GREP
**Category:** 正規表現

## Signature
```
RE_GREP( string , regexp )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String to process |
| regexp | Regular expression pattern to match |

## Returns
- 1 or greater: Number of matching portions (if matches were found)
- 0: No matching portions were found

## Description
Searches the target string for all portions that match the regular expression. You can get detailed results using `RE_GETSTR`・`RE_GETPOS`・`RE_GETLEN`.

## Compatibility
- YAYA: Available since the initial release
- AYA: Available from version 5.8 onward
- Tc606-6: Changed the regular expression engine to uka_regexp (syntax similar to PCRE2). Subroutine calls in patterns can be resolved using variables and functions ([Regular expressions](../grammar/14-regular-expressions.md))

## See Also
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [Regular expressions](../grammar/14-regular-expressions.md)
