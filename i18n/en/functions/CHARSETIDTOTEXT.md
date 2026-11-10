# CHARSETIDTOTEXT

**Category:** メタ操作・特殊関数

## Signature

```
CHARSETIDTOTEXT(id)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| id | An integer representing a character encoding ID |

## Returns

On success: a string representing a character encoding
On failure: the string "default"

## Description

Converts a character encoding ID to a string representing a character encoding.

## Example

```
CHARSETIDTOTEXT(0) // "Shift_JIS" を返す
CHARSETIDTOTEXT(1) // "UTF-8" を返す
```

## Compatibility

- YAYA: Available since the initial release

## See Also

- CHARSETTEXTTOID
