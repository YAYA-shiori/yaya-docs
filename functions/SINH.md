# SINH
**Category:** 数学関数
**Source:** マニュアル/関数/SINH

## Signature
```
SINH(rad)
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | ラジアン単位の角度値 |

## Returns
- 成功時: 双曲線正弦（実数）
- 失敗時: 0.0

## Description
双曲線正弦（ハイパーボリック関数）を計算して返します。引数の単位はラジアンです。

## Example
```
_rad = 30 * 3.14159265358 / 180  // 30°をラジアンに変換
SINH(_rad)                        // 約 0.547853 を返す
```

## Compatibility
- YAYA: Tc522-1以降

## See Also
- SIN, COS, TAN（三角関数）
- ASIN, ACOS, ATAN（逆三角関数）
- COSH, TANH（双曲線関数）
