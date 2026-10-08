# COS

**Category:** 数学関数

## Signature

```
COS(rad)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| rad | ラジアン単位の角度 |

## Returns

成功時：コサイン値を表す実数
失敗時：0.0

## Description

コサインを返す。引数の単位はラジアン。

ラジアンは角度の単位のひとつで、180 度が π ラジアン（π は約 3.14159265358）にあたる。度からラジアンにするには `度 * 3.14159265358 / 180` と計算する（90 度なら約 1.5708）。

## Example

```
_rad = 60 * 3.14159265358 / 180  // 60° をラジアンに変換
COS(_rad)  // 0.500000 を返す
```

## Compatibility

- YAYA: 初版から利用可能
- AYA: バージョン5.8以降

## See Also

- SIN
- TAN
- ASIN
- ACOS
- ATAN
- SINH
- COSH
- TANH
