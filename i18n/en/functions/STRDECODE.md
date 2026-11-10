# STRDECODE
**Category:** 文字列操作

## Signature
```
STRDECODE(string [, code] [, type])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | String to decode |
| code | Character encoding ID to use for conversion (defaults to 0), or a character encoding name ([character encoding names](../grammar/11-character-encoding.md#文字コードの名前)). If the name is unknown, issues warning W0012 and returns 0 |
| type | Decoding format. Specify `url` (URL encoding) or `base64` (Base64). Defaults to `url` |

## Returns
- On success: Decoded string
- On failure: 0

## Description
Decodes a string using the specified character encoding and encoding format. See [character encoding names](../grammar/11-character-encoding.md#文字コードの名前) for character encoding IDs.

## Compatibility
- YAYA: Tc521-1 or later (renamed from `GETSTRURLDECODE` in Tc532-1)
- Tc574-8 / Tc603-1: Now issues warning W0012 and returns 0 when given an unknown character encoding name (previously, it issued no warning and treated the name as the OS default)

## See Also
- STRENCODE (encoding function)
