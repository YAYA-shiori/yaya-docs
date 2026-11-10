# RE_GETSTR
**Category:** 正規表現

## Signature
```
RE_GETSTR
RE_GETSTR()
```

## Parameters
None

## Returns
A generic array containing the matched substrings.

| Element | Contents |
|------|------|
| Element 0 | String matched by the entire regular expression |
| Element n | Substring matched by the nth parenthesized group |

- Returns `IARRAY` if no regular expression function has been executed or no matching string was found.
- For `RE_REPLACE`・`RE_REPLACEEX`・`RE_SPLIT`, returns an array containing the string matched by the entire regular expression, rather than the individual groups.

## Description
Gets the results of a regular-expression function.

## Example
```
RE_MATCH("x > 15.7", "x *> *([\d\.]+)")
_array = RE_GETSTR
// _array は ("x > 15.7", "15.7") になる
```

## Compatibility
- YAYA: Available since the initial release
- AYA: Available from version 5.8 onward

## See Also
- RE_GETPOS
- RE_GETLEN
- [Regular expressions](../grammar/14-regular-expressions.md)
