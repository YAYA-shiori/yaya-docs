# RE_GETLEN
**Category:** 正規表現

## Signature
```
RE_GETLEN
RE_GETLEN()
```

## Parameters
None

## Returns
A generic array listing the lengths of the parts matched by `( )` in the regular expression.

| Element | Contents |
|------|------|
| Element 0 | Length of the part matched by the entire regular expression |
| Element n | Length of the part matched by the nth parenthesized group |

- Lengths are measured in characters.
- Returns `IARRAY` if no regular expression function has been executed or no string has matched.
- For `RE_REPLACE`・`RE_REPLACEEX`・`RE_SPLIT`, returns the length of the part matched by the entire regular expression, not the individual groups.

## Description
Gets the results of regular expression functions. Use it together with `RE_GETPOS` and `RE_GETSTR`.

## Compatibility
- YAYA: Available since the initial release
- AYA: Available since version 5.8

## See Also
- RE_GETPOS
- RE_GETSTR
- [Regular expressions](../grammar/14-regular-expressions.md)
