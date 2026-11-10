# CHARSETTEXTTOID

**Category:** メタ操作・特殊関数

## Signature

```
CHARSETTEXTTOID(string)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| string | A string representing a character code |

## Returns

On success: An integer representing a character code ID
On failure: -1 (warning W0012; GETLASTERROR returns 12)

Converts a string representing a character code to a character code ID. See [Character Code Names](../grammar/11-character-encoding.md#文字コードの名前) for the supported names. Case is ignored. An empty string becomes 127 (OS default).

## Example

```
CHARSETTEXTTOID('Shift_JIS')  // 0 を返す
CHARSETTEXTTOID('UTF-8')      // 1 を返す
CHARSETTEXTTOID('UTF8')       // 1 を返す
CHARSETTEXTTOID('UTF-16')     // -1 を返す（W0012）
```

## Compatibility

- YAYA: Available since the first release
- Tc574-8 / Tc603-1: Changed so that an unknown name returns -1 instead of 127 and issues warning W0012

## See Also

- CHARSETIDTOTEXT
