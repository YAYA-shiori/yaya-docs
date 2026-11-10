# ARRAYSIZE

**Category:** 配列操作

## Signature

```
ARRAYSIZE(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 简易数组（字符串）或通用数组 |

## Returns

成功时：元素数
失败时：0

## Description

返回简易数组或通用数组的元素数。

## Example

```
_array = ('さくら','まゆら','ねここ') // 汎用配列を代入
ARRAYSIZE( _array ) // 要素数「3」を出力
```

## Compatibility

- YAYA：从初始版本起可用
- AYA：5.8 及更高版本

## See Also

- ARRAYDEDUP
- ASEARCH
