# ACOS

**Category:** 数学関数

## Signature

```
ACOS( val )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| val | アークコサインを計算する実数値。-1.0 ≦ val ≦ 1.0 の範囲 |

## Returns

成功時：アークコサインの値をラジアンで返す（実数）
失敗時：0.0

## Description

アークコサインをラジアンで返す。

返り値の単位はラジアン。度にするには `ラジアン * 180 / 3.14159265358` と計算する。ラジアンは角度の単位のひとつで、180 度が π ラジアン（π は約 3.14159265358）にあたる。

## Example

```
_d = ACOS( 0.5 )    // 約 1.047198 (ラジアン) を返す
_d * 180 / 3.14159265358  // 約 60 度に変換
```

## Compatibility

- YAYA: 初期リリースから利用可能
- AYA: バージョン 5.8 以降

## See Also

- ASIN
- ATAN
- SIN
- COS
- TAN
- SINH
- COSH
- TANH
