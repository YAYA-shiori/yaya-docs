# CVREAL

**Category:** 型取得/変換

## Signature

```
CVREAL(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| *var* | 要轉換的變數。將實數形式的字串型轉換為實數型，並重新存入。若為非數值字串，則轉換為實數型並存入 "0.000000"。 |

## Returns

沒有傳回值（VOID）。

## Description

指定存有實數形式字串的變數時，會轉換為實數並重新存入。指定存有其他字串的變數時，會將變數型別設為實數，並存入 `0.000000`。

## Example

```
_val = '3.1415' // 文字列として代入
CVREAL(_val)
GETTYPE(_val) // "2" を出力（実数型になった）
_val          // "3.141500" を出力（実数型になった）
```

## Compatibility

- YAYA：從初版起支援
- AYA：5.8 版以後

## See Also

- CVINT
- CVSTR
- CVAUTO
