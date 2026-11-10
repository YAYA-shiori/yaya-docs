# STRENCODE
**Category:** 文字列操作

## Signature
```
STRENCODE(string [, code] [, type])
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| string | The string to encode |
| code | Character encoding ID to use (defaults to 0), or a character encoding name ([Character encoding names](../grammar/11-character-encoding.md#文字コードの名前)). If the name is unknown, emits warning W0012 and returns 0 |
| type | Encoding format. Specify `url` (URL encoding), `form` (form encoding, which converts spaces to +), or `base64` (Base64). Defaults to `url` |

## Returns
- On success: the encoded string
- On failure: 0

## Description
Encodes a string using the specified character encoding and encoding format. For character encoding IDs, see [Character encoding names](../grammar/11-character-encoding.md#文字コードの名前).

## Compatibility
- YAYA: Available from Tc521-1 onward (renamed from `GETSTRURLENCODE` in Tc532-1)
- Tc574-8 / Tc603-1: Changed to emit warning W0012 and return 0 when given an unknown character encoding name (previously, it emitted no warning and treated the name as the OS default)

## See Also
- STRDECODE (decoding function)
