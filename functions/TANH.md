# TANH
**Category:** 数学関数

## Signature
```
TANH(rad)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | ラジアン単位の角度値 |

## Returns
- 成功時: 双曲線タンジェント（実数）
- 失敗時: 0.0

## Description
双曲線タンジェント（ハイパーボリック関数）を返します。引数の単位はラジアンです。

ラジアンは角度の単位のひとつで、180 度が π ラジアン（π は約 3.14159265358）にあたる。度からラジアンにするには `度 * 3.14159265358 / 180` と計算する（90 度なら約 1.5708）。

## Example
```
_rad = 45 * 3.14159265358 / 180  // 45°をラジアンに変換
TANH(_rad)  // 約 0.655794 を返す
```

## Compatibility
- YAYA: Tc522-1以降

## See Also
- SIN, COS, TAN（三角関数）
- ASIN, ACOS, ATAN（逆三角関数）
- SINH, COSH（双曲線関数）
