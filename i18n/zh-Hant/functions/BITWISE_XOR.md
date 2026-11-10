# BITWISE_XOR

**Category:** ビット演算

## Signature

```
BITWISE_XOR( var1 , var2 )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var1 | 要進行位元運算的值 |
| var2 | 要進行位元運算的值 |

## Returns

成功時：位元 XOR 運算的結果（數值）
失敗時：VOID

## Description

對 `var1` 和 `var2` 執行位元 XOR 運算。運算前會分別將兩者轉換為整數（帶正負號的 64 位元整數；Tc566-1 之前為帶正負號的 32 位元整數）。

## Example

```
_val1 = 28 // binary: 11100
_val2 = 9  // binary: 01001
BITWISE_XOR( _val1, _val2 ) // 21 を返す（2進数: 10101）
```

## Compatibility

- YAYA: TC513-901 以後
- Tc566-1: 配合整數改為 64 位元，運算也改為以 64 位元進行

## See Also

- BITWISE_AND
- BITWISE_OR
- BITWISE_NOT
- BITWISE_SHIFT
