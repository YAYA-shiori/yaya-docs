# SUBSTR
**Category:** 文字列操作

## Signature
```
SUBSTR(src, pos, len)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | Source string |
| pos | Starting position (zero-based; negative values are offsets from the end) |
| len | Number of characters to retrieve |

## Returns
- On success: the retrieved substring
- If pos exceeds the string length: an empty string `""`
- If pos + len exceeds the end of the string: retrieves through the end
- On error: VOID

## Description
Extracts a substring from a string. If a negative value is specified for `pos`, it is treated as an offset from the end of the string (for example, -2 is the second-to-last character).

## Example
```
SUBSTR("HOGE", -2, 1)  // 結果: "G"（末尾から2番目の文字）
```

## Compatibility
- YAYA: Available since the initial version
- AYA: 5.8 and later (negative pos values are not supported)

## See Also
- STRSTR (substring search)
- STRLEN (string length)
