# BITWISE_NOT

**Category:** ビット演算
**Source:** マニュアル/関数/BITWISE_NOT

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

演算前に符号付き32ビット整数に変換される。

## Example

```
_val = 28          // 2進数: 00011100
BITWISE_NOT(_val)  // -29 (2進数: 11100011) を返す
```

## Compatibility

- YAYA: TC513-901 以降

## See Also

- BITWISE_AND
- BITWISE_OR
- BITWISE_XOR
- BITWISE_SHIFT
