# IARRAY
**Category:** 配列操作

## Signature
```
IARRAY
IARRAY()
```

## Parameters
なし

## Returns
空の汎用配列

## Description
空の汎用配列を返す。

主な用途は以下の2つ:

**1. 配列の初期化**

初期化せずに `,=` で要素を追加すると、インデックス0に不要な空文字列要素が生成される。IARRAYで初期化することでこれを防ぐことができる。

**2. 要素の削除**

配列要素にIARRAYを代入することで、その要素を完全に削除し、後続の要素をシフトすることができる（空文字列を残さない）。ただし Tc603-1以降、その要素が配列やハッシュ（[入れ子](../grammar/13-nesting.md)）のときは、削除されずに空の配列に置き換わる。入れ子の要素を削除するときは範囲指定で `_a[1, 1] = IARRAY` と書く。

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
- YAYA: 初期から利用可能
- AYA: 5.8以降
