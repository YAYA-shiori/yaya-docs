# SETDELIM
**Category:** 配列操作
**Source:** マニュアル/関数/SETDELIM

## Signature
```
SETDELIM( array , delim )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| array | デリミタを設定する単純配列変数 |
| delim | 設定するデリミタ文字列 |

## Returns
なし

## Description
変数の標準デリミタ（単純配列の区切り文字）を設定します。デフォルトのデリミタはカンマ（,）です。

**注意:** 両引数は関数に直接指定する必要があります。以下のような方法では正しく動作しません:

```
// 不正な使い方（動作しない）
_i = (var, "/")
SETDELIM(_i)
```

```
// 正しい使い方
SETDELIM(var, "/")
```

## Compatibility
- YAYA: 初期バージョンより対応
- AYA: 5.8以降

## See Also
- GETDELIM
