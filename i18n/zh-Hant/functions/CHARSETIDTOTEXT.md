# CHARSETIDTOTEXT

**Category:** メタ操作・特殊関数

## Signature

```
CHARSETIDTOTEXT(id)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| id | 表示字元編碼 ID 的整數 |

## Returns

成功時：表示字元編碼的字串
失敗時：字串 "default"

## Description

將字元編碼 ID 轉換為表示字元編碼的字串。

## Example

```
CHARSETIDTOTEXT(0) // "Shift_JIS" を返す
CHARSETIDTOTEXT(1) // "UTF-8" を返す
```

## Compatibility

- YAYA: 從初版起即可使用

## See Also

- CHARSETTEXTTOID
- [字元編碼的名稱](../grammar/11-character-encoding.md#文字コードの名前)
