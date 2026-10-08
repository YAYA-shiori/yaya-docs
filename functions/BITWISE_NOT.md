# BITWISE_NOT

**Category:** ビット演算

## Signature

```
BITWISE_NOT( var )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 演算対象の数値 |

## Returns

成功時：ビットNOT演算後の数値結果
失敗時：VOID

## Description

`var` のビット NOT 演算を行う。演算の前に、整数（符号付き64ビット）に変換する（Tc566-1より前は符号付き32ビット）。

## Example

```
_val = 28          // 2進数: 00011100
BITWISE_NOT(_val)  // -29 (2進数: 11100011) を返す
```

## Compatibility

- YAYA: TC513-901 以降
- Tc566-1: 整数が64ビットになったのに合わせて、演算も64ビットで行う

## See Also

- BITWISE_AND
- BITWISE_OR
- BITWISE_XOR
- BITWISE_SHIFT
