# ASEARCHEX

**Category:** 配列操作

## Signature

```
ASEARCHEX(key, array)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| key | 要搜尋的字串值 |
| array | 通用陣列（不可使用簡易陣列） |

## Returns

傳回一個通用陣列，其中存放所有符合元素的索引（從 0 開始）。若沒有符合的元素，則傳回空陣列。

## Description

從通用陣列中搜尋所有值相符的元素。

## Example

```
_tea = ("鉄観音", "烏龍", "やぶきた", "烏龍", "ジャスミン")
ipod = ASEARCHEX("烏龍", _tea)
// ipod には (1,3) という汎用配列が格納される
```

## Compatibility

- YAYA：從初始版本起即可使用
- AYA：版本 5.8 以後

## See Also

- ASEARCH
- RE_ASEARCHEX
