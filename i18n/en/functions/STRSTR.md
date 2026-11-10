# STRSTR
**Category:** 文字列操作

## Signature
```
STRSTR(src, search, pos)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | The string to search |
| search | The substring to search for |
| pos | Search start position (0-based) |

## Returns
- If found: the character position where the substring begins (0-based)
- If not found: -1

## Description
Searches a string for a substring and returns the character position where it is found.

## Compatibility
- YAYA: Available since the initial version
- AYA: 5.8 and later

## See Also
- STRLEN (get string length)
- SUBSTR (substring retrieval)
