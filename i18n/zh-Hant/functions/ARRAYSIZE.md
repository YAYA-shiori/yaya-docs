# ARRAYSIZE

**Category:** 配列操作

## Signature

```
ARRAYSIZE(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 簡易陣列（字串）或通用陣列 |

## Returns

成功時：元素數量
失敗時：0

## Description

傳回簡易陣列或通用陣列的元素數量。

## Example

```
_array = ('さくら','まゆら','ねここ') // 汎用配列を代入
ARRAYSIZE( _array ) // 要素数「3」を出力
```

## Compatibility

- YAYA: 從初始版本起即可使用
- AYA: 5.8 版以後

## See Also

- ARRAYDEDUP
- ASEARCH
