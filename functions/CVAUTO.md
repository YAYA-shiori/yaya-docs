# CVAUTO

**Category:** 型取得/変換
**Source:** マニュアル/関数/CVAUTO

## Signature

```
CVAUTO(_var_)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 変換対象の変数 |
| strict_convert | （省略可、デフォルト: 0）0以外の場合、変換後の値を文字列に戻したときに元の値と一致する場合のみ変換を行う |

## Returns

戻り値なし（変数をその場で変換する）

文字列形式の変数を、整数または実数として解釈できる場合に変換する（Tc571-2）。どちらの型としても解釈できない場合は変更されない。汎用配列変数を渡した場合の動作は未定義。

## Example

```
_val = '3.14159'
CVAUTO(_val)
GETTYPE(_val) // 2 を返す（実数型であることを示す）
```

## Compatibility

- YAYA: TC516-901以降

## See Also

- CVREAL
- CVINT
- CVSTR
- CVAUTOEX
- TOAUTO
