# BITWISE_OR

**Category:** ビット演算

## Signature

```
BITWISE_OR( var1 , var2 )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var1 | 數值 |
| var2 | 數值 |

## Returns

成功時：位元 OR 運算的數值結果
失敗時：VOID

## Description

對 `var1` 和 `var2` 執行位元 OR 運算。運算前會先分別轉換為整數（帶正負號的 64 位元；Tc566-1 以前為帶正負號的 32 位元）。

## Example

```
_val1 = 28  // 2進数: 11100
_val2 = 9   // 2進数: 01001
BITWISE_OR( _val1, _val2 )  // 29 (2進数: 11101) を出力
```

## Compatibility

- YAYA：Tc513-901 以後
- Tc566-1：配合整數改為 64 位元，運算也改為 64 位元

## See Also

- BITWISE_AND
- BITWISE_XOR
- BITWISE_NOT
- BITWISE_SHIFT
