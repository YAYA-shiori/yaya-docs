# ZEN2HAN
**Category:** 文字列操作

## Signature
```
ZEN2HAN( src [ , type ] )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| src | String to convert |
| type | (Optional) Specify the character types to convert, separated by commas. If omitted, all types are converted |

### Values that can be specified for type
| Value | Target character type |
|----|-----------|
| `number` | Digits (0–9) |
| `alphabet` | Alphabetic characters |
| `symbol` | Symbols and punctuation |
| `kana` | Katakana and punctuation |

## Returns
- Success: Converted string
- Failure: VOID

## Description
Converts full-width alphanumeric characters and katakana in a string to half-width characters. The type parameter can be used to limit the character types to be converted.

## Example
```
ZEN2HAN('２００７ABCアイウエオ', 'number,alphabet')
// "2007ABCアイウエオ" (数字と英字のみ変換、カタカナは変換しない)
```

## Compatibility
- YAYA: TC513-901 and later

## See Also
- HAN2ZEN
- TRANSLATE
