# IHASH
**Category:** ハッシュ操作

## Signature
```
IHASH( [key1, value1, key2, value2, ...] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key*n* | キー |
| value*n* | key*n* に対応する値 |

## Returns
ハッシュ。引数が無ければ空のハッシュ。

## Description
キーと値を交互に並べてハッシュを作る。

- 引数の汎用配列は、ほかの関数と同じく展開される。`IHASH("x", (1,2,3))` は `IHASH("x",1,2,3)` と同じになり、`x=1`、`2=3` の2要素になる。ハッシュの値に配列を入れたいときは、作ったあとで要素に代入する（`_h["x"] = (1,2,3)`）
- 引数にハッシュを渡すと、展開されずにそのままキーや値になる（入れ子）
- 引数の数が奇数のときは警告 W0020 を出し、最後のキーの値は VOID になる
- 同じキーとみなされるものが2回以上出てきたときは、最初のキーと値が残る

キーの一致と並び順の規則は [ハッシュ](../grammar/12-hash.md) を参照。

## Example
```
_h = IHASH("name", "さくら", "age", 16)
_h["name"]              // "さくら"

_e = IHASH()            // 空のハッシュ
_e["k"] = (1, 2, 3)     // 値に配列を入れる

IHASH(9, "i9", "9", "s9")   // 9 と "9" は同じキーなので 9=i9 だけ
```

## Compatibility
- YAYA: Tc600-3以降

## See Also
- HASH_SPLIT
- HASH_KEYS
- HASH_VALUES
- HASH_EXIST
- HASH_SIZE
- IARRAY
