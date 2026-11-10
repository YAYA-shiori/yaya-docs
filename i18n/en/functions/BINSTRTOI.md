# BINSTRTOI

**Category:** 文字列操作

## Signature

```
BINSTRTOI(string)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | The binary string to convert |

## Returns

On success: The converted number
On failure: 0

## Description

Converts a string representing a binary number to an integer.

## Example

```
_bin = '11110'
_i = BINSTRTOI(_bin)
_i // 30 を出力（2進数 11110 = 10進数 30）
```

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later

## See Also

- HEXSTRTOI
- TOBINSTR
