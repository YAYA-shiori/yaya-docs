# CHRCODE

**Category:** 文字列操作

## Signature

```
CHRCODE( string [ , pos ] )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | Text containing the character whose character code you want to retrieve |
| pos | (Optional) Character position from which to retrieve the character code (zero-based). Defaults to 0 |

## Returns

On success: A number representing the character code
On failure: 0

Returns the UCS-2 character code. ASCII characters (single-byte alphanumeric characters) are compatible with ASCII codes.

## Example

```
CHRCODE('A')      // 65 を返す
CHRCODE('ABC', 2) // 67（文字'C'）を返す
CHRCODE('伺')     // 20282 を返す
```

## Compatibility

- YAYA: Available since the first release
- AYA: Version 5.8 and later

## See Also

- CHR
