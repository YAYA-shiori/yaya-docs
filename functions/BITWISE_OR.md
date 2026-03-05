# BITWISE_OR

**Category:** ビット演算
**Source:** マニュアル/関数/BITWISE_OR

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

演算前に符号付き32ビット整数に変換される。

## Example

```
_val1 = 28  // 2進数: 11100
_val2 = 9   // 2進数: 01001
BITWISE_OR( _val1, _val2 )  // 29 (2進数: 11101) を出力
```

## Compatibility

- YAYA: TC513-901 以降

## See Also

- BITWISE_AND
- BITWISE_XOR
- BITWISE_NOT
- BITWISE_SHIFT
