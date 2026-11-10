# CVSTR

**Category:** 型取得/変換

## Signature

```
CVSTR(var)
```

## Parameters

| 参数 | 说明 |
|-----------|-------------|
| *var* | 要转换的变量。将其转换为字符串类型并重新存储到同一变量中。 |

## Returns

无返回值（VOID）。

## Description

指定变量作为参数时，会将其值转换为字符串并重新存储。

## Example

```
_val = 3.1415  // 実数として格納
CVSTR(_val)
GETTYPE(_val)  // "3" を出力（文字列型になった）
_val           // "3.141500" を出力（文字列表現に変換された）
```

## Compatibility

- YAYA: 从初版开始支持
- AYA: 5.8 及以上版本

## See Also

- CVINT
- CVREAL
- CVAUTO
