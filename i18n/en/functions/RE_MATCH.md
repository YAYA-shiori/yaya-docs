# RE_MATCH
**Category:** 正規表現

## Signature
```
RE_MATCH( string , regexp )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String to match |
| regexp | Regular expression pattern |

## Returns
- **1**: The entire string matches the pattern exactly
- **0**: No match

## Description
Checks whether the target string matches the regular expression exactly. Use RE_SEARCH to check for a partial match.

You can get details about the match using RE_GETSTR, RE_GETPOS, and RE_GETLEN.

## Example
```
RE_MATCH("50kg", "(\d+) *kg")
// → 1

RE_MATCH("50cm", "(\d+) *kg")
// → 0
```

## Compatibility
- YAYA: Supported since the initial version
- AYA: 5.8 onward
- Tc606-6: Changed the regular expression engine to uka_regexp (syntax similar to PCRE2). Subroutine calls in patterns can be resolved using variables and functions ([Regular expressions](../grammar/14-regular-expressions.md))

## See Also
- RE_SEARCH
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [Regular expressions](../grammar/14-regular-expressions.md)
