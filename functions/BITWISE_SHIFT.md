# BITWISE_SHIFT

**Category:** ビット演算

## Signature

```
BITWISE_SHIFT(var, shift)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | シフト対象の数値 |
| shift | シフトするビット数。正の値の場合は左シフト、負の値の場合は右シフト |

## Returns

成功時：ビットシフト演算の数値結果
失敗時：VOID

## Description

`var` のビットシフト演算を行う。演算の前に、整数（符号付き64ビット）に変換する（Tc566-1より前は符号付き32ビット）。

`shift` でシフトするビット数を指定する。`shift` が正の場合は左シフト、負の場合は右シフトになる。右シフトの場合、算術シフトになるか論理シフトになるかは処理系依存。現在配布されている Windows 用の `yaya.dll` では算術シフトになる（`BITWISE_SHIFT(-8, -1)` は `-4`）。

## Example

```
_var = 0x7fffffff
_result = BITWISE_SHIFT(_var, -2)
// _result は 0x1fffffff になる
```

## Compatibility

- YAYA: TC513-901 以降
- Tc566-1: 整数が64ビットになったのに合わせて、演算も64ビットで行う

## See Also

- BITWISE_AND
- BITWISE_OR
- BITWISE_XOR
- BITWISE_NOT
