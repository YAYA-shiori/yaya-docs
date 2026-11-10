# CVSTR

**Category:** 型取得/変換

## Signature

```
CVSTR(var)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| *var* | 要轉換的變數。轉換為字串型後重新存入同一個變數。 |

## Returns

沒有傳回值（VOID）。

## Description

指定變數作為引數時，會將其值轉換為字串並重新存入。

## Example

```
_val = 3.1415  // 実数として格納
CVSTR(_val)
GETTYPE(_val)  // "3" を出力（文字列型になった）
_val           // "3.141500" を出力（文字列表現に変換された）
```

## Compatibility

- YAYA：從初版起支援
- AYA：5.8 版以後

## See Also

- CVINT
- CVREAL
- CVAUTO
