# IARRAY
**Category:** 配列操作

## Signature
```
IARRAY
IARRAY()
```

## Parameters
無

## Returns
空的通用陣列

## Description
傳回空的通用陣列。

主要用途如下兩種：

**1. 初始化陣列**

未初始化就使用 `,=` 新增元素時，會在索引 0 產生不需要的空字串元素。使用 IARRAY 初始化即可避免這種情況。

**2. 刪除元素**

將 IARRAY 指派給陣列元素，即可完全刪除該元素並將後續元素向前移動（不會留下空字串）。若指派空字串並以為已刪除，元素位置上仍會留下空字串，元素數量也不會減少。不過在 Tc603-1 以後，若該元素是陣列或雜湊（[巢狀](../grammar/13-nesting.md)），就不會刪除，而會取代為空陣列。要刪除巢狀元素時，請以範圍指定寫成 `_a[1, 1] = IARRAY`。

完全刪除元素後，後面的元素會向前移動，因此位置也會改變。如果陣列的索引編號不能改變，請勿使用 `IARRAY`。

## Example
```
// 初期化なしの場合（望ましくない結果）
_myarray ,= "hoge"
_myarray ,= "hogehoge"
// 結果: ("","hoge","hogehoge")

// IARRAYで初期化した場合
_myarray = IARRAY
_myarray ,= "hoge"
_myarray ,= "hogehoge"
// 結果: ("hoge","hogehoge")

// 要素の削除
_myarray = ("hoge","hogehoge")
_myarray[0] = IARRAY
// 結果: ("hogehoge") — 要素が削除されてシフト
```

## Compatibility
- YAYA: 從初期版本起即可使用
- AYA: 5.8 以後
