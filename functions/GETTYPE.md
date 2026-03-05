# GETTYPE
**Category:** 型取得/変換
**Source:** マニュアル/関数/GETTYPE

## Signature
```
GETTYPE( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 型を調べる値・変数・式 |

## Returns
- 0: 内部エラー（失敗）
- 1: 整数
- 2: 浮動小数点数
- 3: 文字列
- 4: 汎用配列

## Description
指定した値のデータ型を取得する。

「要素数1の汎用配列は、その最初の（唯一の）要素の型を返します」という後方互換性のための動作がある。要素数1の汎用配列の型を正確に調べたい場合は `GETTYPEEX` を使用することが推奨される。

## Compatibility
- YAYA: 初期から利用可能
- AYA: 5.8以降

## See Also
- GETTYPEEX
