# HASH_SPLIT
**Category:** ハッシュ操作
**Source:** マニュアル/関数/HASH_SPLIT

## Signature
```
HASH_SPLIT( str, sep1, sep2 )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| str | 分割する文字列 |
| sep1 | 要素の区切り |
| sep2 | キーと値の区切り |

## Returns
ハッシュ

## Description
文字列を `sep1` で要素に分け、各要素を `sep2` でキーと値に分けてハッシュを作る。

- 空の要素は飛ばす
- `sep2` を含まない要素は、キーだけの要素になる（値は VOID）
- キーが空の要素（`=x` など）は捨てる
- 最初の `sep2` で分ける。`d=4=5` はキー `d`、値 `4=5` になる
- `sep1` か `sep2` が空文字列のときは警告 W0010 を出し、空のハッシュを返す

## Example
```
_h = HASH_SPLIT("a=1,b=2,,c,=x,d=4=5", ",", "=")
// a=1,b=2,c=,d=4=5 （要素数 4）
```

## Compatibility
- YAYA: Tc600-3以降

## See Also
- IHASH
- SPLIT
