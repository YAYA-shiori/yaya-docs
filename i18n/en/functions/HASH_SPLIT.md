# HASH_SPLIT
**Category:** ハッシュ操作

## Signature
```
HASH_SPLIT( str, sep1, sep2 )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | String to split |
| sep1 | Element separator |
| sep2 | Key-value separator |

## Returns
Hash

## Description
Splits a string into elements using `sep1`, then splits each element into a key and value using `sep2` to create a hash.

- Empty elements are skipped
- An element that does not contain `sep2` becomes a key-only element (its value is VOID)
- Elements with an empty key (such as `=x`) are discarded
- Splitting occurs at the first `sep2`. `d=4=5` becomes key `d` and value `4=5`
- If `sep1` or `sep2` is an empty string, warning W0010 is issued and an empty hash is returned

## Example
```
_h = HASH_SPLIT("a=1,b=2,,c,=x,d=4=5", ",", "=")
// a=1,b=2,c=,d=4=5 （要素数 4）
```

## Compatibility
- YAYA: Tc600-3 and later

## See Also
- IHASH
- SPLIT
