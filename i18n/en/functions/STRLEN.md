# STRLEN
**Category:** 文字列操作

## Signature
```
STRLEN(string)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | The string whose character count to get |

## Returns
- On success: the number of characters (integer)
- On failure: 0

## Description
Returns the number of characters in a string. It returns the character count, not the byte count, so multibyte characters such as kanji count as one character.

## Compatibility
- YAYA: Available since the initial version
- AYA: 5.8 and later

## See Also
- STRSTR (substring search)
- SUBSTR (substring retrieval)
- GETSTRBYTES (get byte count)
