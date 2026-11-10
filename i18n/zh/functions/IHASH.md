# IHASH
**Category:** ハッシュ操作

## Signature
```
IHASH( [key1, value1, key2, value2, ...] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key*n* | 键 |
| value*n* | 对应于 key*n* 的值 |

## Returns
哈希。没有参数时返回空哈希。

## Description
将键和值交替排列，创建哈希。

- 与其他函数一样，参数中的通用数组会展开。`IHASH("x", (1,2,3))` 与 `IHASH("x",1,2,3)` 等效，会生成两个元素：`x=1` 和 `2=3`。要将数组作为哈希的值，应在创建哈希后赋给相应元素（`_h["x"] = (1,2,3)`）
- 将哈希作为参数传入时，不会展开，而是直接成为键或值（嵌套）
- 参数个数为奇数时，会发出警告 W0020，最后一个键的值为 VOID
- 被视为相同的键出现两次或更多次时，保留第一个键和值

键匹配和排列顺序的规则请参阅[哈希](../grammar/12-hash.md)。

## Example
```
_h = IHASH("name", "さくら", "age", 16)
_h["name"]              // "さくら"

_e = IHASH()            // 空のハッシュ
_e["k"] = (1, 2, 3)     // 値に配列を入れる

IHASH(9, "i9", "9", "s9")   // 9 と "9" は同じキーなので 9=i9 だけ
```

## Compatibility
- YAYA: Tc600-3及之后

## See Also
- HASH_SPLIT
- HASH_KEYS
- HASH_VALUES
- HASH_EXIST
- HASH_SIZE
- IARRAY
