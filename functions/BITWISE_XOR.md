# BITWISE_XOR

**Category:** ビット演算

## Signature

```
BITWISE_XOR( var1 , var2 )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var1 | ビット演算を行う値 |
| var2 | ビット演算を行う値 |

## Returns

成功時：ビットXOR演算の結果（数値）
失敗時：VOID

## Description

`var1` と `var2` のビット XOR演算を行う。演算の前に、それぞれを整数（符号付き64ビット）に変換する（Tc566-1より前は符号付き32ビット）。

## Example

```
_val1 = 28 // binary: 11100
_val2 = 9  // binary: 01001
BITWISE_XOR( _val1, _val2 ) // returns 21 (binary: 10101)
```

## Compatibility

- YAYA: TC513-901以降
- Tc566-1: 整数が64ビットになったのに合わせて、演算も64ビットで行う

## See Also

- BITWISE_AND
- BITWISE_OR
- BITWISE_NOT
- BITWISE_SHIFT
