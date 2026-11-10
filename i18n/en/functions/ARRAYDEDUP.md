# ARRAYDEDUP

**Category:** 配列操作

## Signature

```
ARRAYDEDUP(array)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| array | Generic array |

## Returns

Returns a generic array with duplicate elements removed.

## Description

When elements are considered equal, the first one is retained. The resulting order is not the same as the original order; it follows the same order as [hash keys](../grammar/12-hash.md#並び順).

Starting with Tc600-3, element equality and ordering follow the same rules as hash keys.

- Integers, real numbers, and strings representing integers in canonical form are considered equal if their values are the same (`1`, `1.0`, and `"1"` are equal)
- Numbers are ordered before strings
- Array and hash elements are compared by content. Hashes with the same content are merged into one; hashes with different content are retained
- VOID values are considered equal to each other

The results for arrays containing a single type (only integers, only real numbers, or only strings) are unchanged from before.

## Example

```
ARRAYDEDUP((3, 1, 2, 1))                    // 1,2,3
ARRAYDEDUP((10, "9", 9, "a", 1.0, 1, "1"))  // 1.000000,9,10,a （Tc600-3以降）
```

## Compatibility

- YAYA: Tc568-1 and later
- Tc600-3: Fixed results for mixed-type arrays that depended on their order, and changed comparisons to follow the same rules as hash keys

## See Also

- ARRAYSIZE
