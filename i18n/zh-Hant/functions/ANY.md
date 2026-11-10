# ANY

**Category:** 文字列操作

## Signature

```
ANY(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 隨機選取的對象。可以是字串、通用陣列、整數或實數 |

## Returns

成功時：隨機選出的其中一個元素
失敗時：VOID

將字串視為簡易陣列時，會從中隨機傳回 1 個元素。通用陣列也會隨機傳回 1 個元素。若為數值型別（整數或實數），則原樣傳回該值。選出元素的索引可透過 LSO 函式取得。

## Example

```
_array = ('さくら','まゆら','ねここ')
ANY(_array)  // 「まゆら」などランダムな要素を返す

_str = 'さくら,まゆら,ねここ'
ANY(_str)    // 「ねここ」などランダムな要素を返す

LSO          // 2（「ねここ」のインデックス）を返す
```

## Compatibility

- YAYA: 從初始版本起即可使用
- AYA: 5.8 版以後

## See Also

- LSO
