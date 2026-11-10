# HEXSTRTOI
**Category:** 文字列操作

## Signature
```
HEXSTRTOI( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要转换的十六进制数值字符串 |

## Returns
- 成功时：转换后的数值（整数）
- 失败时：0

## Description
将十六进制数值字符串转换为整数。如果字符串以 `0x` 前缀开头，则忽略该前缀。

## Example
```
_hex = '1E'
_i = HEXSTRTOI( _hex )
// _i は 30（16進数 1E = 10進数 30）
```

## Compatibility
- YAYA: 从初始版本起可用
  - Tc547-1及之后：可处理开头的 `0x` 前缀
- AYA: 5.8及之后

## See Also
- BINSTRTOI
- TOHEXSTR
