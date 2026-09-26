# HASH_KEYS
**Category:** ハッシュ操作
**Source:** マニュアル/関数/HASH_KEYS

## Signature
```
HASH_KEYS( hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| hash | ハッシュ |

## Returns
キーの汎用配列。キーの順に並ぶ。

## Description
ハッシュのキーを汎用配列で返す。並びは挿入した順ではなく、キーの順（数値 < 文字列）になる。

引数がハッシュでないときは警告 W0009 を出す。

## Example
```
_h = IHASH("b", 1, "a", 2, 10, 3, 9, 4)
HASH_KEYS(_h)   // 9,10,a,b
```

## Compatibility
- YAYA: Tc600-3以降

## See Also
- HASH_VALUES
- IHASH
