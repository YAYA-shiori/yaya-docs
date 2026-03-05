# BITWISE_SHIFT

**Category:** ビット演算
**Source:** マニュアル/関数/BITWISE_SHIFT

## Signature

```
BITWISE_SHIFT(var, shift)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | シフト対象の数値（符号付き32ビット整数に変換される） |
| shift | シフトするビット数。正の値の場合は左シフト、負の値の場合は右シフト |

## Returns

成功時：ビットシフト演算の数値結果
失敗時：VOID

右シフト時の動作は実装依存。Windows版では算術シフトが使用される。

## Example

```
_var = 0x7fffffff
_result = BITWISE_SHIFT(_var, -2)
// _result は 0x1fffffff になる
```

## Compatibility

- YAYA: TC513-901 以降

## See Also

- BITWISE_AND
- BITWISE_OR
- BITWISE_XOR
- BITWISE_NOT
