# TOHEXSTR
**Category:** 文字列操作

## Signature
```
TOHEXSTR( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 要转换的整数值 |

## Returns
- 成功：十六进制数字字符串
- 失败：VOID

## Description
将整数转换为十六进制数字字符串。

## Example
```
_i = 30
_hex = TOHEXSTR( _i )
_hex // "1E" (10進数30 = 16進数1E)
```

## Compatibility
- YAYA：从初始版本起
- AYA：5.8 及以后
- Tc574-4 / Tc602-5：修复了整数最小值（-9223372036854775808）只显示为 `-` 的问题

## See Also
- TOBINSTR
- HEXSTRTOI
