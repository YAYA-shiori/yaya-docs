# HAN2ZEN
**Category:** 文字列操作

## Signature
```
HAN2ZEN( src [ , type ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | String to convert |
| type | (Optional) Character types to convert, specified as a comma-separated list. If omitted, converts all types |

Values that can be specified for `type`:
| Value | Target |
|----|------|
| `number` | Digits (0–9) |
| `alphabet` | Alphabetic characters |
| `symbol` | Symbols, etc. |
| `kana` | Katakana, punctuation, etc. |

## Returns
- On success: Converted string
- On failure: VOID

## Description
Converts half-width alphabetic characters, digits, and katakana in a string to full-width characters. Use `type` to limit the character types to convert.

## Example
```
_result = HAN2ZEN('2007ABC', 'number,alphabet')
// 結果: "２００７ＡＢＣ"
```

## Compatibility
- YAYA: TC513-901 and later

## See Also
- ZEN2HAN
- TRANSLATE
