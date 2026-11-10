# TOBINSTR
**Category:** 文字列操作

## Signature
```
TOBINSTR( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 要转换的整数值 |

## Returns
- 成功：二进制数字字符串
- 失败：VOID

## Description
将整数转换为二进制数字字符串。

## Example
```
_i = 30
_bin = TOBINSTR( _i )
_bin // "11110" (10進数30 = 2進数11110)
```

## Compatibility
- YAYA：从初始版本起
- AYA：5.8 及以后
- Tc574-4 / Tc602-5：修复了整数最小值（-9223372036854775808）只显示为 `-` 的问题

## See Also
- TOHEXSTR
- BINSTRTOI
