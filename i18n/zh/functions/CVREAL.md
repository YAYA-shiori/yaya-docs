# CVREAL

**Category:** 型取得/変換

## Signature

```
CVREAL(var)
```

## Parameters

| 参数 | 说明 |
|-----------|-------------|
| *var* | 要转换的变量。将实数格式的字符串类型转换为实数类型并重新存储。对于非数值字符串，将其转换为实数类型并存储 "0.000000"。 |

## Returns

无返回值（VOID）。

## Description

指定存储实数格式字符串的变量时，会将其转换为实数并重新存储。指定存储其他字符串的变量时，会将变量类型设为实数，并存储 `0.000000`。

## Example

```
_val = '3.1415' // 文字列として代入
CVREAL(_val)
GETTYPE(_val) // "2" を出力（実数型になった）
_val          // "3.141500" を出力（実数型になった）
```

## Compatibility

- YAYA: 从初版开始支持
- AYA: 5.8 及以上版本

## See Also

- CVINT
- CVSTR
- CVAUTO
