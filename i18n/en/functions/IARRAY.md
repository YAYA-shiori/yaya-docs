# IARRAY
**Category:** 配列操作

## Signature
```
IARRAY
IARRAY()
```

## Parameters
None

## Returns
Empty generic array

## Description
Returns an empty generic array.

Its main uses are as follows:

**1. Initializing an array**

If you add elements with `,=` without initializing the array, an unwanted empty string element is created at index 0. Initializing with IARRAY prevents this.

**2. Removing elements**

Assigning IARRAY to an array element completely removes that element and shifts subsequent elements (without leaving an empty string behind). If you assign an empty string to remove an element, the empty string remains at that position and the number of elements does not decrease. However, from Tc603-1 onward, if the element is an array or hash ([nested](../grammar/13-nesting.md)), it is replaced with an empty array rather than being removed. To remove a nested element, specify a range, as in `_a[1, 1] = IARRAY`.

When an element is completely removed, the elements after it shift forward and their positions change. Do not use `IARRAY` if the array element indices must not change.

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
- YAYA: Available from the initial release
- AYA: 5.8 and later
