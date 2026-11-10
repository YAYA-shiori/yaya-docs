# BITWISE_SHIFT

**Category:** ビット演算

## Signature

```
BITWISE_SHIFT(var, shift)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| var | 要進行位元移位的數值 |
| shift | 移位的位元數。正值表示左移，負值表示右移 |

## Returns

成功時：位元移位運算的數值結果
失敗時：VOID

## Description

對 `var` 執行位元移位運算。運算前會先轉換為整數（帶正負號的 64 位元整數；Tc566-1 之前為帶正負號的 32 位元整數）。

使用 `shift` 指定移位的位元數。`shift` 為正值時會左移，為負值時會右移。右移時是算術移位還是邏輯移位，取決於實作方式。目前發行的 Windows 版 `yaya.dll` 使用算術移位（`BITWISE_SHIFT(-8, -1)` 的結果為 `-4`）。

## Example

```
_var = 0x7fffffff
_result = BITWISE_SHIFT(_var, -2)
// _result は 0x1fffffff になる
```

## Compatibility

- YAYA: TC513-901 以後
- Tc566-1: 配合整數改為 64 位元，運算也改為以 64 位元進行

## See Also

- BITWISE_AND
- BITWISE_OR
- BITWISE_XOR
- BITWISE_NOT
