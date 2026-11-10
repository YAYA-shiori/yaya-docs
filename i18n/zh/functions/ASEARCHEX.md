# ASEARCHEX

**Category:** 配列操作

## Signature

```
ASEARCHEX(key, array)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| key | 要搜索的字符串值 |
| array | 通用数组（不能使用简易数组） |

## Returns

返回一个通用数组，其中存放所有匹配元素的序号（从 0 开始）。没有匹配元素时，返回空数组。

## Description

在通用数组中搜索所有值匹配的元素。

## Example

```
_tea = ("鉄観音", "烏龍", "やぶきた", "烏龍", "ジャスミン")
ipod = ASEARCHEX("烏龍", _tea)
// ipod には (1,3) という汎用配列が格納される
```

## Compatibility

- YAYA：从初始版本起可用
- AYA：版本 5.8 及以上

## See Also

- ASEARCH
- RE_ASEARCHEX
