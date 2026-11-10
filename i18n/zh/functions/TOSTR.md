# TOSTR
**Category:** 型取得/変換

## Signature
```
TOSTR( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 要转换的整数、实数或通用数组 |

## Returns
- 成功：转换后的字符串
- 失败：VOID

## Description
将整数、实数或通用数组转换为字符串。传入通用数组时，会返回以逗号连接各个元素的字符串。

## Example
```
_i = 100
_result = TOSTR( _i )
// "100"

_array = ('さくら','ねここ','まゆら')
_result = TOSTR( _array )
// "さくら,ねここ,まゆら"
```

## Compatibility
- YAYA：从初始版本起
- AYA：5.8 及以后
- Tc574-4 / Tc602-5：修复了整数最小值（-9223372036854775808）只显示为 `-` 的问题
- Tc574-4 / Tc601-1：修复了将大于等于 1e57 的实数转换为字符串时，末尾有时会混入乱码的问题

## See Also
- TOINT
- TOREAL
