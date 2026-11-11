# RE_REPLACE
**Category:** 正規表現

## Signature
```
RE_REPLACE( string , regexp , replace [, count] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | The string to process (for numeric variables, converting them to strings with TOSTR is recommended) |
| regexp | Regular expression pattern |
| replace | Replacement string (metacharacters cannot be used) |
| count | Number of replacements (omitted or negative values replace all matches) |

## Returns
- Success: The replaced string
- No match: The original string (unchanged)

## Description
Replaces parts of the string to process that match the regular expression. Metacharacters cannot be used in the replacement string. To use metacharacters, use RE_REPLACEEX.

Details about matches can be obtained with RE_GETSTR, RE_GETPOS, and RE_GETLEN. When this function is used, those functions return the nth content matched by the entire regular expression in the target string, rather than the content of each `( )`.

## Compatibility
- YAYA: Supported since the initial version (the count parameter is supported from Tc548-1 onward)
- AYA: 5.8 and later
- Tc606-6: Changed the regular expression engine to uka_regexp (syntax similar to PCRE2). Subroutine calls in patterns can be resolved using variables and functions ([Regular Expressions](../grammar/14-regular-expressions.md))

## See Also
- REPLACE
- RE_REPLACEEX
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [Regular Expressions](../grammar/14-regular-expressions.md)
