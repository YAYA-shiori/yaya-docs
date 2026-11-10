# CHARSETTEXTTOID

**Category:** メタ操作・特殊関数

## Signature

```
CHARSETTEXTTOID(string)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | 表示字符编码的字符串 |

## Returns

成功时：表示字符编码 ID 的整数
失败时：-1（警告 W0012，GETLASTERROR 为 12）

将表示字符编码的字符串转换为字符编码 ID。可用名称请参阅[字符编码名称](../grammar/11-character-encoding.md#文字コードの名前)。不区分大小写。空字符串对应 127（OS 默认值）。

## Example

```
CHARSETTEXTTOID('Shift_JIS')  // 0 を返す
CHARSETTEXTTOID('UTF-8')      // 1 を返す
CHARSETTEXTTOID('UTF8')       // 1 を返す
CHARSETTEXTTOID('UTF-16')     // -1 を返す（W0012）
```

## Compatibility

- YAYA: 从初版起可用
- Tc574-8 / Tc603-1: 名称无法识别时，改为返回 -1（而非 127）并发出警告 W0012

## See Also

- CHARSETIDTOTEXT
