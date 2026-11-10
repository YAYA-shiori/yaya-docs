# SETDELIM
**Category:** 配列操作

## Signature
```
SETDELIM( array , delim )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| array | Simple array variable whose delimiter to set |
| delim | Delimiter string to set |

## Returns
None

## Description
Sets the variable's default delimiter (the separator for simple arrays). The default delimiter is a comma (,).

**Note:** Both arguments must be specified directly in the function call. The following approaches will not work correctly:

```
// 不正な使い方（動作しない）
_i = (var, "/")
SETDELIM(_i)
```

```
// 正しい使い方
SETDELIM(var, "/")
```

## Compatibility
- YAYA: Supported since the initial version
- AYA: 5.8 and later

## See Also
- GETDELIM
