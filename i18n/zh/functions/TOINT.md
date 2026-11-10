# TOINT
**Category:** 型取得/変換

## Signature
```
TOINT( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要转换的字符串或实数 |

## Returns
- 成功：转换后的整数值
- 失败：0

## Description
将字符串或实数转换为整数。小数点后的部分会直接截断。

Tc542-4 之前的版本具有相当于 FLOOR() 的行为（错误），从 Tc542-4 起则与其他语言一样，直接截断小数点后的部分。

## Example
```
_i = '100'       // 文字列を代入
_j = _i + 1
// "1001" (文字列の連結になってしまう)

_i = '100'
_j = TOINT( _i ) + 1
// 101 (整数に変換してから加算)

_i = 1.1
_j = TOINT( _i )
// 1

_i = -1.1
_j = TOINT( _i )
// -1 (Tc542-4以降の動作)
```

## Compatibility
- YAYA：从初始版本起
- AYA：5.8 及以后
- Tc542-4 及以后：更改负数小数的截断行为
- Tc574-4 / Tc602-6：修复了数字后面跟着 `a`（`A`）的字符串会将 `a` 读取为数位 10，导致 `TOINT('1a')` 得到 20 的问题（现在会得到 1）

## See Also
- TOSTR
- TOREAL
