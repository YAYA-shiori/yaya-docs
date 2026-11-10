# SETDELIM
**Category:** 配列操作

## Signature
```
SETDELIM( array , delim )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| array | 要設定分隔符號的簡易陣列變數 |
| delim | 要設定的分隔符號字串 |

## Returns
無

## Description
設定變數的預設分隔符號（簡易陣列的分隔字元）。預設分隔符號為逗號（,）。

**注意：**兩個引數都必須直接指定給函式。以下列方式使用時無法正確運作：

```
// 不正な使い方（動作しない）
_i = (var, "/")
SETDELIM(_i)
```

```
// 正しい使い方
SETDELIM(var, "/")
```

## Compatibility
- YAYA：從初始版本起支援
- AYA：5.8 以後

## See Also
- GETDELIM
