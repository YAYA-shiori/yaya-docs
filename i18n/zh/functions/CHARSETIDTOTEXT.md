# CHARSETIDTOTEXT

**Category:** メタ操作・特殊関数

## Signature

```
CHARSETIDTOTEXT(id)
```

## Parameters

| 参数 | 说明 |
|-----------|-------------|
| id | 表示字符编码 ID 的整数 |

## Returns

成功时：表示字符编码的字符串
失败时：字符串 "default"

## Description

将字符编码 ID 转换为表示字符编码的字符串。

## Example

```
CHARSETIDTOTEXT(0) // "Shift_JIS" を返す
CHARSETIDTOTEXT(1) // "UTF-8" を返す
```

## Compatibility

- YAYA：从初版起即可使用

## See Also

- CHARSETTEXTTOID
- [字符编码的名称](../grammar/11-character-encoding.md#文字コードの名前)
