# TOAUTO
**Category:** 型取得/変換

## Signature
```
TOAUTO( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要转换的字符串 |

## Returns
- 可以解析为整数时：整数值
- 可以解析为实数时（整数转换失败时）：实数值
- 两者都无法解析时：原样返回输入字符串

## Description
尝试对字符串进行自动类型转换的函数。优先尝试转换为整数，失败时再尝试转换为实数。如果两种转换都不成功，则原样返回输入字符串。

将通用数组作为参数传入时，行为未定义。

## Compatibility
- YAYA：TC516-901 及更高版本

## See Also
- TOINT
- TOREAL
- TOSTR
- TOAUTOEX
- CVAUTO
