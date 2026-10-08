# ASIN

**Category:** 数学関数

## Signature

```
ASIN(val)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | アークサインを計算する実数値。-1.0 ≤ val ≤ 1.0 の範囲 |

## Returns

成功時：アークサインの値をラジアンで返す（実数）
失敗時：0.0

## Description

アークサインをラジアンで返す。

返り値の単位はラジアン。度にするには `ラジアン * 180 / 3.14159265358` と計算する。ラジアンは角度の単位のひとつで、180 度が π ラジアン（π は約 3.14159265358）にあたる。

## Example

```
_d = ASIN(0.5)           // 0.523599 (ラジアン) を返す
_d * 180 / 3.14159265358 // 度に変換：30.000000
```

## Compatibility

- YAYA: 初期リリースから利用可能
- AYA: バージョン 5.8 以降

## See Also

- ACOS
- ATAN
- SIN
- COS
- TAN
- SINH
- COSH
- TANH
