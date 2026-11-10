# RE_ASEARCH
**Category:** 正規表現

## Signature
```
RE_ASEARCH(key, array)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key | The regular expression pattern to search for |
| array | The generic array to search (simple arrays are not supported) |

## Returns
- The index (0-based) of the first matching element
- If no element matches: -1

## Description
Searches a generic array for values that match the specified regular expression, even partially, and returns only the first match.

**Note:** `RE_GETSTR`・`RE_GETPOS`・`RE_GETLEN` cannot be used. To get all matches, use `RE_ASEARCHEX`.

## Example
```
_array = ('さくら','まゆら','ねここ')
RE_ASEARCH('^ま', _array) // Returns: 1
```
Searches for an element beginning with "ま" and finds index 1 (the second element).

## Compatibility
- YAYA: Available since version Tc539-1
- Tc606-6: Changed the regular expression engine to uka_regexp (syntax similar to PCRE2). Subroutine calls in patterns can be resolved with variables and functions ([regular expressions](../grammar/14-regular-expressions.md))

## See Also
- ASEARCH
- RE_ASEARCHEX
- [Regular expressions](../grammar/14-regular-expressions.md)
