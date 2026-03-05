# SIN
**Category:** 数学関数
**Source:** マニュアル/関数/SIN

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
