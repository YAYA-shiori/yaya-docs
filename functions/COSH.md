# COSH

**Category:** 数学関数
**Source:** マニュアル/関数/COSH

## Signature

```
COSH(rad)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| rad | ラジアン単位の角度値 |

## Returns

成功時：ハイパボリック・コサイン（双曲線関数）の値を表す実数
失敗時：0.0

ハイパボリック・コサイン（双曲線関数）を返す。引数の単位はラジアン。

## Example

```
_rad = 60 * 3.14159265358 / 180  // 60° をラジアンに変換
COSH(_rad)  // 約 1.600287 を返す
```

## Compatibility

- YAYA: TC522-1以降

## See Also

- SIN
- COS
- TAN
- ASIN
- ACOS
- ATAN
- SINH
- TANH
