# GETDELIM
**Category:** 配列操作
**Source:** マニュアル/関数/GETDELIM

## Signature
```
GETDELIM( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | デリミタを調べたい単純配列変数 |

## Returns
指定した変数に設定されているデリミタ文字列。

## Description
変数に設定されているデリミタ（単純配列の区切り文字）を取得する関数。デフォルトのデリミタはカンマ（`,`）。

SETDELIMで変更されたデリミタを確認するために使用する。

## Compatibility
- YAYA: 初期バージョンから使用可能
- AYA: バージョン5.8以降

## See Also
- SETDELIM
