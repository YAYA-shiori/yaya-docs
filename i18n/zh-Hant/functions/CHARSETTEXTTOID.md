# CHARSETTEXTTOID

**Category:** メタ操作・特殊関数

## Signature

```
CHARSETTEXTTOID(string)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | 表示字元編碼的字串 |

## Returns

成功時：表示字元編碼 ID 的整數
失敗時：-1（警告 W0012，GETLASTERROR 為 12）

將表示字元編碼的字串轉換為字元編碼 ID。可用的名稱請參閱[字元編碼名稱](../grammar/11-character-encoding.md#文字コードの名前)。不區分大小寫。空字串會轉換為 127（作業系統預設值）。

## Example

```
CHARSETTEXTTOID('Shift_JIS')  // 0 を返す
CHARSETTEXTTOID('UTF-8')      // 1 を返す
CHARSETTEXTTOID('UTF8')       // 1 を返す
CHARSETTEXTTOID('UTF-16')     // -1 を返す（W0012）
```

## Compatibility

- YAYA: 初版起即可使用
- Tc574-8 / Tc603-1: 遇到不明名稱時，改為傳回 -1 並發出警告 W0012，而非傳回 127

## See Also

- CHARSETIDTOTEXT
