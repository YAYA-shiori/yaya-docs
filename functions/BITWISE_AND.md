# BITWISE_AND

**Category:** ビット演算

## Signature

```
BITWISE_AND( var1 , var2 )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var1 | 数値 |
| var2 | 数値 |

## Returns

成功時：ビットAND演算の数値結果
失敗時：VOID

## Description

`var1` と `var2` のビット AND演算を行う。演算の前に、それぞれを整数（符号付き64ビット）に変換する（Tc566-1より前は符号付き32ビット）。

## Example

```
_val1 = 30  // 2進数: 11110
_val2 = 13  // 2進数: 01101
BITWISE_AND(_val1, _val2)  // 12 (2進数: 01100) を出力
```

## Compatibility

- YAYA: TC513-901 以降
- Tc566-1: 整数が64ビットになったのに合わせて、演算も64ビットで行う

## See Also

- BITWISE_OR
- BITWISE_XOR
- BITWISE_NOT
- BITWISE_SHIFT
