# CVREAL

**Category:** 型取得/変換

## Signature

```
CVREAL(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| *var* | The variable to convert. Converts a string in real-number format to a real number and stores it back in the variable. If the string is non-numeric, converts it to a real number and stores "0.000000". |

## Returns

There is no return value (VOID).

## Description

When you specify a variable containing a string in real-number format, it is converted to a real number and stored back in the variable. If you specify a variable containing any other string, the variable's type is changed to real and `0.000000` is stored.

## Example

```
_val = '3.1415' // 文字列として代入
CVREAL(_val)
GETTYPE(_val) // "2" を出力（実数型になった）
_val          // "3.141500" を出力（実数型になった）
```

## Compatibility

- YAYA: Supported since the first release
- AYA: 5.8 and later

## See Also

- CVINT
- CVSTR
- CVAUTO
