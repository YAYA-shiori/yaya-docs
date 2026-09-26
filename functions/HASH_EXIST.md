# HASH_EXIST
**Category:** ハッシュ操作
**Source:** マニュアル/関数/HASH_EXIST

## Signature
```
HASH_EXIST( key, hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| key | 調べるキー |
| hash | ハッシュ |

## Returns
- 1: キーがある
- 0: キーが無い

## Description
ハッシュにキーがあるかどうかを返す。引数の順は**キー、ハッシュ**の順（ASEARCH と同じ）なので注意。

`h[キー]` はキーが無くても空文字列を返すので、「値が空文字列」と「キーが無い」を区別したいときにこの関数を使う。

キーの一致は [ハッシュのキーの規則](../grammar/12-hash.md#キーの一致) に従う。`key` が配列やハッシュのときは警告 W0009 を出す。

## Example
```
_h = IHASH("a", "", 1, "x")
HASH_EXIST("a", _h)   // 1
HASH_EXIST("b", _h)   // 0
HASH_EXIST("1", _h)   // 1 （1 と "1" は同じキー）
```

## Compatibility
- YAYA: Tc600-3以降

## See Also
- HASH_KEYS
- HASH_SIZE
- IHASH
