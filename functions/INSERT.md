# INSERT
**Category:** 文字列操作
**Source:** マニュアル/関数/INSERT

## Signature
```
INSERT( src , pos , insert )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | 挿入先の元の文字列 |
| pos | 挿入位置（0=先頭） |
| insert | 挿入する文字列 |

## Returns
- 成功時: 挿入後の文字列
- エラー時: VOID

## Description
文字列 `src` の `pos` で指定した位置に、文字列 `insert` を挿入する。位置0は文字列の先頭を表す。

## Compatibility
- YAYA: 初期から利用可能
- AYA: 5.8以降
