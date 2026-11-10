# ASEARCH

**Category:** 配列操作

## Signature

```
ASEARCH(key, array)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| key | The key value to search for (string) |
| array | Generic array (simple arrays cannot be used) |

## Returns

On success: The order number of the first matching element (zero-based)
If no match is found: -1

## Description

Compares `key` with each element using the same rules as `==` and returns the position of the first match.

Starting with Tc600-3, the following behavior changed.

- Hash elements are compared by content (passing a hash as `key` finds an element that is a hash with the same content)
- If both `key` and an element are VOID, they are considered to match (previously, the result was -1)

## Example

```
_array = ('さくら','まゆら','ねここ')
ASEARCH('まゆら', _array)  // 1 を出力
```

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later
- Tc600-3: Changed hash elements to be compared by content and VOID values to be considered equal

## See Also

- ASEARCHEX
- RE_ASEARCH
