# CHARSETTEXTTOID

**Category:** メタ操作・特殊関数
**Source:** マニュアル/関数/CHARSETTEXTTOID

## Signature

```
CHARSETTEXTTOID(string)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | 文字コードを表す文字列 |

## Returns

成功時：文字コードIDを表す整数
失敗時：127（OSデフォルトエンコーディングを表す）

文字コードを表す文字列を文字コードIDに変換する。

## Example

```
CHARSETTEXTTOID('Shift_JIS')  // 0 を返す
CHARSETTEXTTOID('UTF-8')      // 1 を返す
CHARSETTEXTTOID('UTF8')       // 1 を返す
```

## Compatibility

- YAYA: 初版から利用可能

## See Also

- CHARSETIDTOTEXT
