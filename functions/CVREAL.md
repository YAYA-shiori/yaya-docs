# CVREAL

**Category:** 型取得/変換

## Signature

```
CVREAL(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| *var* | 変換対象の変数。文字列型の実数形式を実数型に変換して格納しなおす。非数値文字列の場合は実数型に変換し "0.000000" を格納する。 |

## Returns

返り値はありません（VOID）。

## Description

実数値の形式を持つ文字列が格納された変数を指定すると、実数に変換して格納しなおす。それ以外の文字列が格納された変数を指定したときは、変数の型を実数にしたうえで `0.000000` を格納する。

## Example

```
_val = '3.1415' // 文字列として代入
CVREAL(_val)
GETTYPE(_val) // "2" を出力（実数型になった）
_val          // "3.141500" を出力（実数型になった）
```

## Compatibility

- YAYA: 初版より対応
- AYA: 5.8以降

## See Also

- CVINT
- CVSTR
- CVAUTO
