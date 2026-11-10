# BINSTRTOI

**Category:** 文字列操作

## Signature

```
BINSTRTOI(string)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | 要转换的二进制数字符串 |

## Returns

成功时：转换后的数值
失败时：0

## Description

将表示二进制数的字符串转换为整数。

## Example

```
_bin = '11110'
_i = BINSTRTOI(_bin)
_i // 30 を出力（2進数 11110 = 10進数 30）
```

## Compatibility

- YAYA：从初始版本起可用
- AYA：版本 5.8 及以上

## See Also

- HEXSTRTOI
- TOBINSTR
