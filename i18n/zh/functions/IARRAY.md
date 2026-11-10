# IARRAY
**Category:** 配列操作

## Signature
```
IARRAY
IARRAY()
```

## Parameters
无

## Returns
空通用数组

## Description
返回空通用数组。

主要用途有以下两种：

**1. 初始化数组**

如果不进行初始化就使用 `,=` 添加元素，索引0处会生成不需要的空字符串元素。使用 IARRAY 初始化即可避免这种情况。

**2. 删除元素**

将 IARRAY 赋给数组元素，可以彻底删除该元素，并将后续元素向前移动（不会留下空字符串）。如果赋入空字符串，以为这样就删除了元素，那么该位置仍会留下空字符串，元素数也不会减少。不过在 Tc603-1及之后，如果该元素是数组或哈希（[嵌套](../grammar/13-nesting.md)），则不会删除，而是替换为空数组。删除嵌套元素时，应使用范围指定，写作 `_a[1, 1] = IARRAY`。

彻底删除元素后，后面的元素会向前移动，位置也会改变。如果数组的索引编号不能改变，请勿使用 `IARRAY`。

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
- YAYA: 从初始版本起可用
- AYA: 5.8及之后
