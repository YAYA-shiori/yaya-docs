# INSERT
**Category:** 文字列操作

## Signature
```
INSERT( src , pos , insert )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | Original string to insert into |
| pos | Insertion position (0 = start). Negative values are treated as offsets from the end (from Tc574-8 / Tc603-1 onward) |
| insert | String to insert |

## Returns
- On success: string after insertion
- On error: VOID

## Description
Inserts the string `insert` into the string `src` at the position specified by `pos`. Position 0 represents the beginning of the string.

If `pos` is negative, the insertion position is calculated by adding the number of characters in `src` to it (for example, -1 inserts before the last character). If the result is still negative, the string is inserted at the beginning; if it is greater than the number of characters in `src`, it is inserted at the end.

```
INSERT('abc', 1, 'X')    // aXbc
INSERT('abc', -1, 'X')   // abXc
INSERT('abc', 10, 'X')   // abcX
INSERT('abc', -10, 'X')  // Xabc
```

## Compatibility
- YAYA: Available from the initial release
- AYA: 5.8 and later
- Tc574-8 / Tc603-1: Negative positions are counted from the end, and out-of-range positions are clamped to the beginning or end (previously, an error interrupted processing). Numeric values passed as `insert` are also inserted (previously, nothing was inserted)
