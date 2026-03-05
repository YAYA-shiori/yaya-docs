# TAN
**Category:** 数学関数
**Source:** マニュアル/関数/TAN

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
