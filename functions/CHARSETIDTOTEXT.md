# CHARSETIDTOTEXT

**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/CHARSETIDTOTEXT

## Signature

```
CHARSETIDTOTEXT(id)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| id | 文字コードIDを表す整数 |

## Returns

成功時：文字コードを表す文字列
失敗時："default" という文字列

## Example

```
CHARSETIDTOTEXT(0) // "Shift_JIS" を返す
CHARSETIDTOTEXT(1) // "UTF-8" を返す
```

## Compatibility

- YAYA: 初版から利用可能

## See Also

- CHARSETTEXTTOID
