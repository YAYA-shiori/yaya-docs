# TOAUTO
**Category:** 型取得/変換
**Source:** マニュアル/関数/TOAUTO

## Signature
```
TOAUTO( string )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | 変換したい文字列 |

## Returns
- 整数に解釈できる場合: 整数値
- 実数に解釈できる場合（整数変換が失敗した場合）: 実数値
- どちらにも解釈できない場合: 元の文字列をそのまま返す

## Description
文字列に対して自動的な型変換を試みる関数。整数への変換を優先的に試み、失敗した場合に実数への変換を試みる。どちらの変換も成功しない場合は、元の文字列をそのまま返す。

一般配列を引数として渡した場合の動作は未定義。

## Compatibility
- YAYA: TC516-901 以降

## See Also
- TOINT
- TOREAL
- TOSTR
- TOAUTOEX
- CVAUTO
