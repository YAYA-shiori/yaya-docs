# BITWISE_OR

**Category:** ビット演算

## Signature

```
BITWISE_OR( var1 , var2 )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var1 | 数値 |
| var2 | 数値 |

## Returns

成功時：ビットOR演算の数値結果
失敗時：VOID

## Description

`var1` と `var2` のビット OR演算を行う。演算の前に、それぞれを整数（符号付き64ビット）に変換する（Tc566-1より前は符号付き32ビット）。

## Example

```
_val1 = 28  // 2進数: 11100
_val2 = 9   // 2進数: 01001
BITWISE_OR( _val1, _val2 )  // 29 (2進数: 11101) を出力
```

## Compatibility

- YAYA: TC513-901 以降
- Tc566-1: 整数が64ビットになったのに合わせて、演算も64ビットで行う

## See Also

- BITWISE_AND
- BITWISE_XOR
- BITWISE_NOT
- BITWISE_SHIFT
