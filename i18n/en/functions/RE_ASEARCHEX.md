# RE_ASEARCHEX
**Category:** 正規表現

## Signature
```
RE_ASEARCHEX( key , array )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key | The regular expression pattern to search for |
| array | The generic array to search (simple arrays are not supported) |

## Returns
A generic array listing the ordinals of matching elements (0-based). Returns an empty array if no elements match.

**Note:** `RE_GETSTR`・`RE_GETPOS`・`RE_GETLEN` cannot be used.

## Description
Searches a generic array for **all** values that match the specified regular expression, even partially.

## Example
```
_tea = ("鉄観音", "烏龍", "やぶきた", "烏龍", "ジャスミン")
ipod = RE_ASEARCHEX("^烏", _tea)
// ipod は (1,3) になる（"烏"で始まる要素のインデックス）
```

## Compatibility
- YAYA: Available since the initial release
- AYA: Available since version 5.8
- Tc606-6: Changed the regular expression engine to uka_regexp (syntax similar to PCRE2). Subroutine calls in patterns can be resolved with variables and functions ([regular expressions](../grammar/14-regular-expressions.md))

## See Also
- ASEARCHEX
- RE_ASEARCH
- [Regular expressions](../grammar/14-regular-expressions.md)
