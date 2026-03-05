# BITWISE_XOR

**Category:** ビット演算
**Source:** マニュアル/関数/BITWISE_XOR

## Signature

```
BITWISE_XOR( var1 , var2 )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var1 | ビット演算を行う値（符号付き32ビット整数に変換される） |
| var2 | ビット演算を行う値（符号付き32ビット整数に変換される） |

## Returns

成功時：ビットXOR演算の結果（数値）
失敗時：VOID

## Example

```
_val1 = 28 // binary: 11100
_val2 = 9  // binary: 01001
BITWISE_XOR( _val1, _val2 ) // returns 21 (binary: 10101)
```

## Compatibility

- YAYA: TC513-901以降

## See Also

- BITWISE_AND
- BITWISE_OR
- BITWISE_NOT
- BITWISE_SHIFT
