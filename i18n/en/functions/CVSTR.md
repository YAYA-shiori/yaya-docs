# CVSTR

**Category:** 型取得/変換

## Signature

```
CVSTR(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| *var* | The variable to convert. Converts it to a string and stores it back in the same variable. |

## Returns

No return value (VOID).

## Description

When you specify a variable as the argument, its value is converted to a string and stored back in the variable.

## Example

```
_val = 3.1415  // 実数として格納
CVSTR(_val)
GETTYPE(_val)  // "3" を出力（文字列型になった）
_val           // "3.141500" を出力（文字列表現に変換された）
```

## Compatibility

- YAYA: Supported since the initial release
- AYA: 5.8 and later

## See Also

- CVINT
- CVREAL
- CVAUTO
