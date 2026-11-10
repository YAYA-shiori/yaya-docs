# TOINT
**Category:** 型取得/変換

## Signature
```
TOINT( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String or real number to convert |

## Returns
- Success: Converted integer value
- Failure: 0

## Description
Converts a string or real number to an integer. The fractional part is simply truncated.

In versions up to Tc542-4, it behaved like FLOOR() (a bug), but from Tc542-4 onward, it simply truncates the fractional part, as in other languages.

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
- YAYA: Since the initial version
- AYA: 5.8 and later
- Tc542-4 and later: Changed how negative fractional values are truncated
- Tc574-4 / Tc602-6: Fixed an issue where a string with `a` (`A`) after a digit was read with `a` as the digit 10, causing `TOINT('1a')` to return 20 instead of 1

## See Also
- TOSTR
- TOREAL
