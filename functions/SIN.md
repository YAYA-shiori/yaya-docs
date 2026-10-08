# SIN
**Category:** 数学関数

## Signature
```
SIN( rad )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| rad | ラジアン単位の角度（数値） |

## Returns
- 成功: サイン値（実数）
- 失敗: 0.0

## Description
サインの値を返します。引数の単位はラジアンです。

ラジアンは角度の単位のひとつで、180 度が π ラジアン（π は約 3.14159265358）にあたる。度からラジアンにするには `度 * 3.14159265358 / 180` と計算する（90 度なら約 1.5708）。

## Example
```
_rad = 30 * 3.14159265358 / 180  // 30度をラジアンに変換
SIN( _rad )  // → 0.500000
```

## Compatibility
- YAYA: 初期バージョンより対応
- AYA: 5.8以降

## See Also
- COS
- TAN
- ASIN
- ACOS
- ATAN
- SINH
- COSH
- TANH
