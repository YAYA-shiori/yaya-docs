# BITWISE_AND

**Category:** ビット演算
**Source:** マニュアル/関数/BITWISE_AND

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

演算前に符号付き32ビット整数に変換される。

## Example

```
_val1 = 30  // 2進数: 11110
_val2 = 13  // 2進数: 01101
BITWISE_AND(_val1, _val2)  // 12 (2進数: 01100) を出力
```

## Compatibility

- YAYA: TC513-901 以降

## See Also

- BITWISE_OR
- BITWISE_XOR
- BITWISE_NOT
- BITWISE_SHIFT
