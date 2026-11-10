# ASEARCHEX

**Category:** 配列操作

## Signature

```
ASEARCHEX(key, array)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| key | The string value to search for |
| array | Generic array (simple arrays cannot be used) |

## Returns

Returns a generic array containing the order numbers (zero-based) of all matching elements. Returns an empty array if there are no matching elements.

## Description

Searches a generic array for all elements whose values match.

## Example

```
_tea = ("鉄観音", "烏龍", "やぶきた", "烏龍", "ジャスミン")
ipod = ASEARCHEX("烏龍", _tea)
// ipod には (1,3) という汎用配列が格納される
```

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later

## See Also

- ASEARCH
- RE_ASEARCHEX
