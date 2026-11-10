# CHR

**Category:** 文字列操作

## Signature

```
CHR( val [, val ... ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | UCS-2 character code value (number). Multiple values can be specified |

## Returns

On success: The converted character or string (a string whose length equals the number of arguments)
On failure: VOID

## Description

When a UCS-2 code is specified as a number, the corresponding single character is returned as a string. Multiple numbers can be specified; in that case, a string whose length equals the number of arguments is returned (passing a generic array returns a string). UCS-2 codes are compatible with ASCII codes in the ASCII range.

## Example

```
CHR(65)      // "A" を返す
CHR(20282)   // "伺" を返す
```

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later

## See Also

- CHRCODE
