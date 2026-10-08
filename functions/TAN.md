# TAN
**Category:** 数学関数

## Signature
```
TAN(rad)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | ラジアン単位の角度値 |

## Returns
- 成功時: タンジェントの値（実数）
- 失敗時: 0.0

## Description
タンジェントを返します。引数の単位はラジアンです。

ラジアンは角度の単位のひとつで、180 度が π ラジアン（π は約 3.14159265358）にあたる。度からラジアンにするには `度 * 3.14159265358 / 180` と計算する（90 度なら約 1.5708）。

## Example
```
_rad = 45 * 3.14159265358 / 180  // 45°をラジアンに変換
TAN(_rad)  // 約 1.000000 を返す
```

## Compatibility
- YAYA: 初期バージョンより利用可能
- AYA: 5.8以降

## See Also
- SIN, COS（三角関数）
- ASIN, ACOS, ATAN（逆三角関数）
- SINH, COSH, TANH（双曲線関数）
