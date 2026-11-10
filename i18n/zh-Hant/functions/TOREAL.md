# TOREAL
**Category:** 型取得/変換

## Signature
```
TOREAL( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 要轉換的字串或整數 |

## Returns
- 成功：轉換後的實數值
- 失敗：0.0

## Description
將字串或整數轉換為實數（浮點數）。

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
- YAYA：自初期版本起
- AYA：5.8 以後

## See Also
- TOINT
- TOSTR
