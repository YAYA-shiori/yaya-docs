# HASH_SIZE
**Category:** ハッシュ操作
**Source:** マニュアル/関数/HASH_SIZE

## Signature
```
HASH_SIZE( hash )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| hash | ハッシュ |

## Returns
要素数（整数）

## Description
ハッシュの要素数を返す。

引数がハッシュでないときは警告 W0009 を出す。

## Example
```
_h = IHASH("a", 1, "b", 2)
HASH_SIZE(_h)   // 2
```

## Compatibility
- YAYA: Tc600-3以降

## See Also
- ARRAYSIZE
- IHASH
