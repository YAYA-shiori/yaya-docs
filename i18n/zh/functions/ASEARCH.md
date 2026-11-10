# ASEARCH

**Category:** 配列操作

## Signature

```
ASEARCH(key, array)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| key | 要搜索的键值（字符串） |
| array | 通用数组（不能使用简易数组） |

## Returns

成功时：返回第一个找到的元素的序号（从 0 开始）
未找到时：-1

## Description

按照与 `==` 相同的规则比较 `key` 和各个元素，并返回第一个匹配元素的位置。

从 Tc600-3 起，以下方面有所改变。

- 元素为哈希时，按内容进行比较（将哈希传给 `key` 时，可以找到内容相同的哈希元素）
- `key` 和元素都为 VOID 时也视为匹配（此前会返回 -1）

## Example

```
_array = ('さくら','まゆら','ねここ')
ASEARCH('まゆら', _array)  // 1 を出力
```

## Compatibility

- YAYA：从初始版本起可用
- AYA：版本 5.8 及以上
- Tc600-3：改为按内容比较哈希元素；改为将两个 VOID 视为匹配

## See Also

- ASEARCHEX
- RE_ASEARCH
