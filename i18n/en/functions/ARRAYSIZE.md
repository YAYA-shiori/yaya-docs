# ARRAYSIZE

**Category:** 配列操作

## Signature

```
ARRAYSIZE(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | Simple array (string) or generic array |

## Returns

On success: Number of elements
On failure: 0

## Description

Returns the number of elements in a simple array or generic array.

## Example

```
_array = ('さくら','まゆら','ねここ') // 汎用配列を代入
ARRAYSIZE( _array ) // 要素数「3」を出力
```

## Compatibility

- YAYA: Available since the initial release
- AYA: Version 5.8 and later

## See Also

- ARRAYDEDUP
- ASEARCH
