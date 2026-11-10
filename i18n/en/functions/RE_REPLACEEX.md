# RE_REPLACEEX
**Category:** 正規表現

## Signature
```
RE_REPLACEEX( string , regexp , replace_ex [, count] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String to process (for numeric variables, conversion to a string type using TOSTR is recommended) |
| regexp | Regular expression pattern |
| replace_ex | Replacement string (Perl-style metacharacters such as `$0` and `$1` can be used) |
| count | Number of replacements (omitted or negative means replace all) |

## Returns
- Success: The replaced string
- Failure: The original string (unchanged)

## Description
Replaces portions of the target string that match the regular expression. Unlike RE_REPLACE, this function lets you use Perl-style metacharacters such as `$0` and `$1` in the replacement string.

When you use RE_REPLACEEX, RE_GETSTR, RE_GETPOS, and RE_GETLEN return information about the nth match of the entire regular expression pattern, rather than captures from the nth group.

## Compatibility
- YAYA: Supported since the initial version (the count parameter is available from Tc548-1 onward)
- Tc606-6: Changed the regular expression engine to uka_regexp (syntax similar to PCRE2). Subroutine calls in patterns can be resolved using variables and functions ([Regular expressions](../grammar/14-regular-expressions.md))

## See Also
- REPLACE
- RE_REPLACE
- RE_GETSTR
- RE_GETPOS
- RE_GETLEN
- [Regular expressions](../grammar/14-regular-expressions.md)
