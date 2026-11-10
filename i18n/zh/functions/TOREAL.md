# TOREAL
**Category:** 型取得/変換

## Signature
```
TOREAL( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要转换的字符串或整数 |

## Returns
- 成功：转换后的实数值
- 失败：0.0

## Description
将字符串或整数转换为实数（浮点数）。

## Example
```
_s = '1.00005'
_d = TOREAL( _s )
_d // 1.000050 (実数)

_i = 1
_d = TOREAL( _i )
_d // 1.000000 (実数)
```

## Compatibility
- YAYA：从初始版本起
- AYA：5.8 及以后

## See Also
- TOINT
- TOSTR
