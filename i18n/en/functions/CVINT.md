# CVINT

**Category:** 型取得/変換

## Signature

```
CVINT(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | The variable to convert to an integer |

## Returns

No return value (converts the variable in place)

Converts a variable containing a string in integer form to an actual integer. The fractional part is truncated.

## Example

```
_val = '583'
CVINT(_val)
GETTYPE(_val) // 1 を返す（整数型）

_val = '583.12'
CVINT(_val)
GETTYPE(_val) // 1 を返す（整数型）
_val // 583 を返す（小数部分は除去される）
```

## Compatibility

- YAYA: Available since the first release
- AYA: Version 5.8 and later
- Tc574-4 / Tc602-6: Fixed an issue where a string followed by `a` (`A`) after a number was read as though `a` represented the digit 10, causing `'1a'` to become 20 (it now becomes 1)

## See Also

- CVREAL
- CVSTR
- CVAUTO
