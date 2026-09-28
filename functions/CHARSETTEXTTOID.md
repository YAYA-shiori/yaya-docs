# CHARSETTEXTTOID

**Category:** メタ操作・特殊関数

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
失敗時：-1（警告 W0012、GETLASTERROR は 12）

文字コードを表す文字列を文字コードIDに変換する。使える名前は [文字コードの名前](../grammar/11-character-encoding.md#文字コードの名前) を参照。大文字小文字は区別しない。空文字列は 127（OSデフォルト）になる。

## Example

```
CHARSETTEXTTOID('Shift_JIS')  // 0 を返す
CHARSETTEXTTOID('UTF-8')      // 1 を返す
CHARSETTEXTTOID('UTF8')       // 1 を返す
CHARSETTEXTTOID('UTF-16')     // -1 を返す（W0012）
```

## Compatibility

- YAYA: 初版から利用可能
- Tc574-8 / Tc603-1: 知らない名前のときに、127 ではなく -1 を返して警告 W0012 を出すようにした

## See Also

- CHARSETIDTOTEXT
