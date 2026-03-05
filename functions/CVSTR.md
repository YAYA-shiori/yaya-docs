# CVSTR

**Category:** 型取得/変換
**Source:** マニュアル/関数/CVSTR

## Signature

```
CVSTR(_var_)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| _var_ | 変換対象の変数。文字列型に変換して同じ変数に格納しなおす。 |

## Returns

返り値はありません（VOID）。

## Example

```
_val = 3.1415  // 実数として格納
CVSTR(_val)
GETTYPE(_val)  // "3" を出力（文字列型になった）
_val           // "3.141500" を出力（文字列表現に変換された）
```

## Compatibility

- YAYA: 初版より対応
- AYA: 5.8以降

## See Also

- CVINT
- CVREAL
- CVAUTO
