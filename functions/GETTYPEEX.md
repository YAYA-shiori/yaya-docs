# GETTYPEEX
**Category:** 型取得/変換
**Source:** マニュアル/関数/GETTYPEEX

## Signature
```
GETTYPEEX( var )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| var | 型を調べる変数の名前（文字列として渡す） |

## Returns
- 0: 内部エラー（失敗）
- 1: 整数
- 2: 実数
- 3: 文字列
- 4: 汎用配列

## Description
指定した変数のデータ型を取得する。`GETTYPE` との主な違いは、引数に変数そのものではなく**変数名を文字列として**渡す点にある。

要素数1の汎用配列についても正確に型を返すため、`GETTYPE` では後方互換動作により正しく判定できないケースでこちらを使用する。

## Compatibility
- YAYA: Tc537-3以降

## See Also
- GETTYPE
- GETVARLIST
