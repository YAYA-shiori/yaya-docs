# GETTYPE
**Category:** 型取得/変換

## Signature
```
GETTYPE( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | Value, variable, or expression whose type to check |

## Returns
- 0: Internal error (failure)
- 1: Integer
- 2: Floating-point number
- 3: String
- 4: Generic array
- 5: Hash (Tc600-3 and later)

## Description
Gets the data type of the specified value.

For backward compatibility, a generic array with one element returns the type of its first (and only) element. To check the type of a generic array with one element accurately, using `GETTYPEEX` is recommended.

This behavior also applies when the only element is an array or hash ([nesting](../grammar/13-nesting.md)); 4 or 5 is returned, respectively.

```
GETTYPE(PARSEJSON('[[1,2]]'))     // 4
GETTYPE(PARSEJSON('[{"a":1}]'))   // 5
```

## Compatibility
- YAYA: Available since the initial release
- AYA: 5.8 and later
- Tc600-3: Changed to return 5 for hashes
- Tc602-10: Fixed an issue where 0 was returned for a generic array with one element whose only element was an array or hash (now returns 4 or 5)

## See Also
- GETTYPEEX
- IHASH
