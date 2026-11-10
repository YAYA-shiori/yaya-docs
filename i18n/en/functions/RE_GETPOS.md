# RE_GETPOS
**Category:** 正規表現

## Signature
```
RE_GETPOS
RE_GETPOS()
```

## Parameters
None

## Returns
A generic array listing the positions matched by `( )` in the regular expression.

| Element | Contents |
|------|------|
| Element 0 | Position where the entire regular expression pattern matched |
| Element n | Position where the nth parenthesized group matched |

- Positions are represented as the number of characters from the beginning (0-based).
- Returns `IARRAY` if no regular expression function has been executed or no matching string was found.
- For `RE_REPLACE`・`RE_REPLACEEX`・`RE_SPLIT`, returns the match position of the entire regular expression, not the individual groups.

## Description
Gets the results of a regular-expression function (match position information).

## Compatibility
- YAYA: Available since the initial release
- AYA: Available from version 5.8 onward

## See Also
- RE_GETSTR
- RE_GETLEN
- [Regular expressions](../grammar/14-regular-expressions.md)
