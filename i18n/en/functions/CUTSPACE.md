# CUTSPACE

**Category:** 文字列操作

## Signature

```
CUTSPACE(string)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | The string to process |

## Returns

On success: The string with leading and trailing whitespace characters (half-width spaces, full-width spaces, and tabs) removed
On failure: VOID

Removes whitespace characters from both ends of a string. Whitespace within the string, such as spaces between words, is preserved.

## Example

```
CUTSPACE(' さくら  まゆら   ') // 「さくら  まゆら」を返す
```

## Compatibility

- YAYA: Available since the first release
- AYA: Version 5.8 and later
