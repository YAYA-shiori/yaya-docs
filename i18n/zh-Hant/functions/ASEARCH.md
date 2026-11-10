# ASEARCH

**Category:** 配列操作

## Signature

```
ASEARCH(key, array)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| key | 要搜尋的鍵值（字串） |
| array | 通用陣列（不可使用簡易陣列） |

## Returns

成功時：傳回第一個找到的元素索引（從 0 開始）
找不到時：-1

## Description

依照與 `==` 相同的規則比較 `key` 與各元素，並傳回第一個符合元素的位置。

Tc600-3 以後有以下變更。

- 元素是雜湊時，會比較內容（將雜湊傳給 `key` 時，會找到內容相同的雜湊元素）
- `key` 與元素都是 VOID 時，也會視為符合（此前會傳回 -1）

## Example

```
_array = ('さくら','まゆら','ねここ')
ASEARCH('まゆら', _array)  // 1 を出力
```

## Compatibility

- YAYA：從初始版本起即可使用
- AYA：版本 5.8 以後
- Tc600-3：改為依內容比較雜湊元素，並將 VOID 彼此視為符合

## See Also

- ASEARCHEX
- RE_ASEARCH
