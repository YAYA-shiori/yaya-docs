# HASH_VALUES
**Category:** ハッシュ操作

## Signature
```
HASH_VALUES( hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| hash | ハッシュ |

## Returns
値の汎用配列。キーの順に並ぶ。

## Description
ハッシュの値を汎用配列で返す。並びは [HASH_KEYS](HASH_KEYS.md) と同じキーの順になる。

値が配列のときは、その配列を1つの要素として含む（入れ子の配列になる）。そのため、戻り値の要素数はハッシュの要素数と同じになる。

引数がハッシュでないときは警告 W0009 を出す。

## Example
```
_h = IHASH("a", 1)
_h["b"] = (1, 2)
_v = HASH_VALUES(_h)
ARRAYSIZE(_v)   // 2
_v[1]           // 配列 (1,2)
TOSTR(_v)       // "1,1,2"
```

## Compatibility
- YAYA: Tc600-3以降

## See Also
- HASH_KEYS
- IHASH
- [値の入れ子と多次元代入](../grammar/13-nesting.md)
