# RE_REPLACE
**Category:** 正規表現

## Signature
```
RE_REPLACE( string , regexp , replace [, count] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String to process (for numeric variables, conversion to a string type using TOSTR is recommended) |
| regexp | Regular expression pattern |
| replace | Replacement string (metacharacters cannot be used) |
| count | Number of replacements (omitted or negative means replace all) |

## Returns
- Success: The replaced string
- No match: The original string (unchanged)

## Description
Replaces portions of the target string that match the regular expression. Metacharacters cannot be used in the replacement string. To use metacharacters, use RE_REPLACEEX.

You can get details about the match using RE_GETSTR, RE_GETPOS, and RE_GETLEN.

## Compatibility
- YAYA: Supported since the initial version (the count parameter is available from Tc548-1 onward)
- AYA: 5.8 onward
- Tc606-6: Changed the regular expression engine to uka_regexp (syntax similar to PCRE2). Subroutine calls in patterns can be resolved using variables and functions ([Regular expressions](../grammar/14-regular-expressions.md))

## See Also
- REPLACE
- RE_REPLACEEX
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [Regular expressions](../grammar/14-regular-expressions.md)
