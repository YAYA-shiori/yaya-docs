# CVREAL

**Category:** 型取得/変換
**Source:** マニュアル/関数/CVREAL

## Signature

```
CVREAL(_var_)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| _var_ | 変換対象の変数。文字列型の実数形式を実数型に変換して格納しなおす。非数値文字列の場合は実数型に変換し "0.000000" を格納する。 |

## Returns

返り値はありません（VOID）。

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
