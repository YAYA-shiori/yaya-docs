# BITWISE_NOT

**Category:** ビット演算

## Signature

```
BITWISE_NOT( var )
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 要運算的數值 |

## Returns

成功時：位元 NOT 運算後的數值結果
失敗時：VOID

## Description

對 `var` 執行位元 NOT 運算。運算前會先轉換為整數（帶正負號的 64 位元；Tc566-1 以前為帶正負號的 32 位元）。

## Example

```
_val = 28          // 2進数: 00011100
BITWISE_NOT(_val)  // -29 (2進数: 11100011) を返す
```

## Compatibility

- YAYA：Tc513-901 以後
- Tc566-1：配合整數改為 64 位元，運算也改為 64 位元

## See Also

- BITWISE_AND
- BITWISE_OR
- BITWISE_XOR
- BITWISE_SHIFT
